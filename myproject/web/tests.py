from django.test import TestCase

# Create your tests here.
from .models import QuoteRequest, Shipment
class HomeTests(TestCase):
    def test_home_renders(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "MotoShift")
        self.assertContains(response, "MoveMyCar")
    def test_quote_saves(self):
        response = self.client.post(
            reverse("quote"),
            {
                "name": "Asha",
                "phone": "9876543210",
                "pickup_city": "Pune",
                "drop_city": "Mumbai",
                "bike_type": "scooter",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(QuoteRequest.objects.filter(name="Asha").exists())
    def test_track_demo(self):
        Shipment.objects.create(
            tracking_id="MOT-48291",
            bike_model="RE 350",
            origin="Bengaluru",
            destination="Hyderabad",
            status="in_transit",
            progress=62,
            last_hub="Kurnool",
        )
        response = self.client.get(reverse("track"), {"id": "MOT-48291"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["ok"], True)