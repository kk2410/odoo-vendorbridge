from django.contrib import admin
from .models import Vendor

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'category', 'gst_number', 'contact_person', 'email', 'rating', 'status']
    list_filter = ['category', 'status']
    search_fields = ['company_name', 'contact_person', 'email']
