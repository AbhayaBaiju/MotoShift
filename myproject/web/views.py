from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
# Create your views here.
from .forms import QuoteForm
from .models import Shipment
CITIES = [
    "Bengaluru",
    "Mumbai",
    "Delhi NCR",
    "Hyderabad",
    "Chennai",
    "Pune",
    "Kolkata",
    "Ahmedabad",
    "Jaipur",
    "Kochi",
]
COMPETITORS = [
    {
        "name": "MoveMyCar.in & Gati KWE",
        "focus": "Cars + two-wheelers",
        "note": "Specialized auto-transport aggregators that connect verified vehicle carriers across major Indian cities.",
        "gaps": ["Car-first marketplace", "Limited two-wheeler UX"],
    },
    {
        "name": "Porter & NoBroker",
        "focus": "Intra-city logistics",
        "note": "Leading apps for vehicle and household shifting, strong on city moves rather than dedicated bike transit.",
        "gaps": ["Not bike-specialized", "Inter-city tracking varies"],
    },
    {
        "name": "Indian Railways Parcel",
        "focus": "Long-distance bikes",
        "note": "The most widely used traditional method — paperwork and drop-off at railway stations, no live GPS.",
        "gaps": ["Station drop-off", "No live tracking"],
    },
    {
        "name": "VRL / Agrim Logistics",
        "focus": "Carrier networks",
        "note": "Established logistics heavyweights with dedicated car and bike carrier trucks operating nationwide.",
        "gaps": ["Manual booking", "Insurance not instant"],
    },
]
def home(request):
    return render(
        request,
        "home.html",
        {
            "form": QuoteForm(),
            "cities": CITIES,
            "competitors": COMPETITORS,
        },
    )
@require_POST
def request_quote(request):
    form = QuoteForm(request.POST)
    if form.is_valid():
        quote = form.save()
        return JsonResponse(
            {
                "ok": True,
                "message": (
                    f"Quote locked in, {quote.name}. A MotoShift advisor will call "
                    f"{quote.phone} with a fare for {quote.pickup_city} → {quote.drop_city}."
                ),
            }
        )
    return JsonResponse({"ok": False, "errors": form.errors}, status=400)
def track_shipment(request):
    tracking_id = (request.GET.get("id") or "").strip().upper()
    if not tracking_id:
        return JsonResponse({"ok": False, "message": "Enter a tracking ID."}, status=400)
    shipment = Shipment.objects.filter(tracking_id__iexact=tracking_id).first()
    if not shipment:
        return JsonResponse(
            {"ok": False, "message": "No bike found. Try demo ID MOT-48291."},
            status=404,
        )
    return JsonResponse(
        {
            "ok": True,
            "tracking_id": shipment.tracking_id,
            "bike_model": shipment.bike_model,
            "origin": shipment.origin,
            "destination": shipment.destination,
            "status": shipment.get_status_display(),
            "status_key": shipment.status,
            "progress": shipment.progress,
            "eta_hours": shipment.eta_hours,
            "last_hub": shipment.last_hub,
            "insured": shipment.insured,
        }
    )