from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # Landing, login, signup, etc.
    path('vendors/', include('vendors.urls')),
    path('rfq/', include('rfq.urls')),
    path('quotations/', include('quotations.urls')),
    path('approvals/', include('approvals.urls')),
    path('purchase-orders/', include('purchase_orders.urls')),
    path('invoices/', include('invoices.urls')),
    path('analytics/', include('analytics_app.urls')),
    path('notifications/', include('notifications_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
