from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Vendor
from .forms import CustomerForm, LoginForm, UpdateForm, VendorRegisterForm
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages

User = get_user_model()

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "user_management/user_register.html"
    success_url = reverse_lazy("login")

class VenderCreateView(CreateView):
    model = Vendor
    form_class = VendorRegisterForm
    template_name = "user_management/vender_register.html"
    success_url = reverse_lazy("login")

class LoginView(LoginView):
    authentication_form = LoginForm
    template_name = "user_management/login.html"
    
    def get_success_url(self):
        return reverse_lazy("homepage")
    
    def form_valid(self, form):
        
        username = self.request.POST.get("username")
        password = self.request.POST.get("password")
        
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        messages.error(self.request, "Invalid credentials")
        return self.form_invalid(form)

class ProfileView(DetailView):
    model = Customer
    template_name = "user_management/profile.html"    
    
class ProfileVenderView(DetailView):
    model = Vendor
    template_name = "user_management/profile_vender.html"    
    
class UpdateView(UpdateView):
    model = Customer
    form_class = UpdateForm
    template_name = "user_management/profile_update.html"
    def get_success_url(self):
        return reverse("profile", kwargs={"pk": self.object.pk})
    
class LogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
class LogoutpageView(TemplateView):
    template_name = "user_management/user_logout.html"
    
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = "user_management/user_delete.html"
    success_url = reverse_lazy("register")
    