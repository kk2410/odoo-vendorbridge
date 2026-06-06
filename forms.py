from django.contrib import admin
from .models import Quotation

@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ['rfq', 'vendor', 'price', 'delivery_timeline', 'status', 'submission_date']
    list_filter = ['status']
    search_fields = ['rfq__rfq_number', 'vendor__company_name']
