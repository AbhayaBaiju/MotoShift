from django.db import models

# Create your models here.
class QuoteRequest(models.Model):
    class BikeType(models.TextChoices):
        COMMUTER = "commuter", "Commuter"
        SCOOTER = "scooter", "Scooter"
        SPORTS = "sports", "Sports / Premium"
        EV = "ev", "Electric"
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    pickup_city = models.CharField(max_length=80)
    drop_city = models.CharField(max_length=80)
    bike_type = models.CharField(max_length=20, choices=BikeType.choices)
    pickup_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_at"]
    def __str__(self):
        return f"{self.name}: {self.pickup_city} → {self.drop_city}"
class Shipment(models.Model):
    class Status(models.TextChoices):
        BOOKED = "booked", "Booked"
        PICKED = "picked", "Picked up"
        IN_TRANSIT = "in_transit", "In transit"
        OUT_FOR_DELIVERY = "ofd", "Out for delivery"
        DELIVERED = "delivered", "Delivered"
    tracking_id = models.CharField(max_length=20, unique=True)
    bike_model = models.CharField(max_length=80)
    origin = models.CharField(max_length=80)
    destination = models.CharField(max_length=80)
    status = models.CharField(max_length=20, choices=Status.choices)
    progress = models.PositiveSmallIntegerField(default=0)
    eta_hours = models.PositiveSmallIntegerField(default=24)
    last_hub = models.CharField(max_length=80, blank=True)
    insured = models.BooleanField(default=True)
    def __str__(self):
        return self.tracking_id