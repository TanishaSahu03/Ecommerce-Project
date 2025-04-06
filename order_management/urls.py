from django.urls import path
from . import views


urlpatterns = [
    path("cart/<int:pk>/", views.UserCartView.as_view(), name = "cart"),
    path("addcart/<int:product_id>/", views.AddCartView.as_view(), name="addcart"),
    path("update-cart/<int:item_id>/", views.UpdateCartView.as_view(), name="update_cart"),
    path("remove-from-cart/<int:item_id>/", views.RemoveFromCartView.as_view(), name="remove_from_cart"),
    path("orders/", views.OrderHistoryView.as_view(), name="order_history"),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    path("create-checkout-session/", views.CreateCheckoutSessionView.as_view(), name="create_checkout_session"),
    # path("payment-success/", views.payment_success, name="payment_success"),
    # path("payment-failed/", views.payment_failed, name="payment_failed"),
]
