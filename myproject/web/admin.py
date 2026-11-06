from django.contrib import admin

# Register your models here.
from .models import QuoteRequest, Shipment
@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "pickup_city", "drop_city", "bike_type", "created_at")
    list_filter = ("bike_type", "pickup_city", "drop_city")
    search_fields = ("name", "phone", "email")
@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ("tracking_id", "bike_model", "origin", "destination", "status", "progress")
    search_fields = ("tracking_id", "bike_model")