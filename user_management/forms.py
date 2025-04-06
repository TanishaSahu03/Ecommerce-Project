from django import forms
from .models import Customer, Vendor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class CustomerForm(UserCreationForm):

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your username"}
        ),
        help_text="",
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter password"}
        ),
        help_text="",
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm password"}
        ),
        help_text="",
    )

    class Meta:
        model = Customer
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
        exclude = (
            "last_login",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "groups",
            "user_permissions",
            "date_joined",
            "is_active",
            "is_superuser",
            "is_staff",
        )

        widgets = {
            # "username": forms.TextInput(
            #     attrs={"class": "form-control", "placeholder": "Enter your username"}
            # ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter your email"}
            ),
            # "password1": forms.PasswordInput(
            #     attrs={"class": "form-control", "placeholder": "Enter password"}
            # ),
            # "password2": forms.PasswordInput(
            #     attrs={"class": "form-control", "placeholder": "Confirm password"}
            # ),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter Username",
                "autocomplete": "off",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter Password"}
        )
    )


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["username", "first_name", "last_name", "email", "phone_number", "address"]

        help_texts = {
            "username": None,
        }

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your first name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your last name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter your email"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your phone number"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your address"}
            ),
            
        }


class VendorRegisterForm(CustomerForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your username"}
        ),
        help_text="",
    )
    store_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your store name"}
        ),
        help_text="",
    )
    tax_id = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your tax id"}
        ),
    )
    
    bank_account_number = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your bank account number"}
        ),
    )

    class Meta:
        model = Vendor
        fields = [
            "username",
            "email",
            "store_name",
            "business_license",
            "bank_account_number",
            "tax_id",
            "password1",
            "password2",
        ]
        widgets = {
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Enter your email"}
            ),
        }
