from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "product_description", "price", "currency"]


class ProductEmailForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["email"]
