from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, TemplateView, DeleteView
from django.views import View
from .models import Product, ProductImage
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin
from order_management.models import Order, OrderItem

class HomePageView(ListView):
    model = Product
    template_name = "product_management/home_page.html"
    context_object_name = "products"

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_management/product_form.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        product = form.save()
        product.vendor = self.request.user.vendor
        product.save()
        images = self.request.FILES.getlist('product_images')
        for img in images:
            ProductImage.objects.create(product=product, image=img)

        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['extra_image_field'] = True  
        return context
    
class ProductDetailView(DetailView):
    model = Product
    template_name = "product_management/product_detail.html"

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_management/product_delete.html"
    success_url = reverse_lazy("productdelete")
    
class Temp(TemplateView):
    template_name = "product_management/product_rud.html"
    
class VendorProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product_management/show_products.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(vendor=self.request.user.vendor)

class ProductSearchView(ListView):
    model = Product
    template_name = "product_management/product_search.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = Product.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(name__icontains=query)  
        return queryset
    
class VendorOrdersView(ListView):
    model = OrderItem
    template_name = "product_management/vendor_orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        return OrderItem.objects.filter(vendor=self.request.user.vendor)