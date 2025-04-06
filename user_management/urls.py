from django.urls import path, include
from . import views
from product_management.views import HomePageView, VendorOrdersView
from order_management.views import PaymentSuccessView
urlpatterns = [
    path("login/", views.LoginView.as_view(), name = "login"),
    path("register/", views.CustomerCreateView.as_view(), name = "register"),
    path("Logoutpage/", views.LogoutpageView.as_view(), name = "logoutpage"),
    path("profile/<int:pk>/", views.ProfileView.as_view(), name = "profile"),
    path("profile-vender/<int:pk>/", views.ProfileVenderView.as_view(), name = "profile-vender"),
    path("update/<int:pk>/", views.UpdateView.as_view(), name = "update"),
    path("delete/<int:pk>/", views.CustomerDeleteView.as_view(), name = "delete"),
    path("logout/", views.LogoutView.as_view(), name = "logout"),
    path("register-vender/", views.VenderCreateView.as_view(), name = "vender-register"),
    path("home/",HomePageView.as_view(), name="homepage"),
    path("payment_success/", PaymentSuccessView.as_view(), name="payment_success"),


]
