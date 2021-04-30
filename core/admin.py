from django.contrib import admin
from .models import Payment, Product, File

# Register your models here.

admin.site.register(Payment)
admin.site.register(File)
admin.site.register(Product)
