from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import ListView, View
from .models import CartItem
from product_management.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
import stripe
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CartItem, Order , OrderItem

stripe.api_key = settings.STRIPE_SECRET_KEY


class UserCartView(LoginRequiredMixin, ListView):
    model = CartItem
    context_object_name = "cart_items"
    template_name = "order_management/cart_page.html"

    def get_queryset(self):
        """Filter cart items to show only those belonging to the logged-in user."""
        return CartItem.objects.filter(user=self.request.user.customer)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = context["cart_items"]
        
        # Add total price for each item in the cart
        for item in cart_items:
            item.total_price = item.product.price * item.quantity  # Individual total

        # Calculate total cart price
        total_price = sum(item.total_price for item in cart_items)
        
        context["cart_items"] = cart_items  # Update cart items with total_price included
        context["total_price"] = total_price  # Overall cart total
        return context


    
class AddCartView(View):
    def post(self, request, product_id):
        print("Adding product to cart...")

        product = get_object_or_404(Product, id=product_id)

        # Ensure the user is a Customer
        if not hasattr(request.user, 'customer'):
            return HttpResponseForbidden("Only customers can add items to the cart.")

        customer = request.user.customer 
        cart_item, created = CartItem.objects.get_or_create(user=customer, product=product)
        
        if not created:
            cart_item.quantity += 1  
            cart_item.save()

        return redirect(reverse('homepage'))

    def get(self, request, product_id):
        return HttpResponseForbidden("Adding to cart is not allowed via GET request.")

class UpdateCartView(LoginRequiredMixin, View):
    def post(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user.customer)
        new_quantity = int(request.POST.get("quantity", 1))
        cart_item.quantity = max(1, new_quantity) 
        cart_item.save()
        return redirect("cart", pk=request.user.customer.id)

class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user.customer)
        cart_item.delete()
        return redirect("cart", pk=request.user.customer.id)
    
    
class PaymentSuccessView(View):
    def get(self, request):
        user = request.user.customer 
        cart_items = CartItem.objects.filter(user=user)

        if not cart_items.exists():
            return redirect("cart")

        with transaction.atomic():
            total_amount = sum(item.total_price() for item in cart_items)

            order = Order.objects.create(user=user, total_amount=total_amount, payment_status=True)

            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price,
                    vendor = cart_item.product.vendor
                )
            cart_items.delete()

        return render(request, "order_management/payment_success.html", {"order": order})
    
class OrderHistoryView(ListView):
    model = Order
    template_name = "order_management/order_history.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user.customer).order_by("-created_at")

class CheckoutView(View):
    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user.customer)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
            
        context = {
            "cart_items": cart_items,
            "total_price": total_price,  # Pass total price
        }
        return render(request, "order_management/checkout.html", context)
     
class CreateCheckoutSessionView(View):
    def post(self, request):
        cart_items = CartItem.objects.filter(user=request.user.customer)
        line_items = []

        for item in cart_items:
            line_items.append({
                "price_data": {
                    "currency": "usd",
                    "unit_amount": int(item.product.price * 100),  # Convert dollars to cents
                    "product_data": {
                        "name": item.product.name,
                    },
                },
                "quantity": item.quantity,
            })

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url="http://127.0.0.1:8000/payment_success/",
            cancel_url="http://127.0.0.1:8000/cart/",
        )

        return redirect(session.url, code=303)