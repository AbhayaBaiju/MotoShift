from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("quote/", views.request_quote, name="quote"),
    path("track/", views.track_shipment, name="track"),
]