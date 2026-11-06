from django import forms
from .models import QuoteRequest
INPUT = (
    "w-full rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm text-slate-800 "
    "outline-none transition focus:border-orange-400 focus:ring-4 focus:ring-orange-100"
)
class QuoteForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = [
            "name",
            "phone",
            "email",
            "pickup_city",
            "drop_city",
            "bike_type",
            "pickup_date",
            "notes",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT, "placeholder": "Your name"}),
            "phone": forms.TextInput(attrs={"class": INPUT, "placeholder": "10-digit mobile"}),
            "email": forms.EmailInput(attrs={"class": INPUT, "placeholder": "Email (optional)"}),
            "pickup_city": forms.TextInput(attrs={"class": INPUT, "placeholder": "Pickup city"}),
            "drop_city": forms.TextInput(attrs={"class": INPUT, "placeholder": "Drop city"}),
            "bike_type": forms.Select(attrs={"class": INPUT}),
            "pickup_date": forms.DateInput(attrs={"class": INPUT, "type": "date"}),
            "notes": forms.Textarea(
                attrs={
                    "class": INPUT + " min-h-[96px] resize-none",
                    "placeholder": "Bike model, packing preference…",
                    "rows": 3,
                }
            ),
        }