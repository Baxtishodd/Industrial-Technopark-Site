from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings
import requests

from core.models import Leadership, Management


def _send_telegram(text: str) -> bool:
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        resp = requests.post(url, data={"chat_id": settings.TELEGRAM_CHAT_ID, "text": text}, timeout=10)
        return resp.status_code == 200
    except Exception:
        return False


def _build_message(name, email, phone, message):
    return (
        f"📩 New Inquiry\n\n"
        f"👤 Name: {name}\n"
        f"📧 Email: {email}\n"
        f"📞 Phone: {phone}\n\n"
        f"📝 Message:\n{message}"
    )


def home(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not message:
            return JsonResponse({"status": "error", "message": "Name and message are required"}, status=400)

        if not _send_telegram(_build_message(name, email, phone, message)):
            return JsonResponse({"status": "error", "message": "Telegram send failed"}, status=500)

        messages.success(request, "Message sent successfully")
        return redirect("home")

    return render(request, 'core/home.html')


# ─── Services ─────────────────────────────────────────────────────────────────

def electric_power(request):
    return render(request, 'services/electric_power.html')

def security(request):
    return render(request, 'services/security.html')

def hot_water(request):
    return render(request, 'services/hot_water.html')

def steam_supply(request):
    return render(request, 'services/steam_supply.html')

def gas_supply(request):
    return render(request, 'services/gas_supply.html')


# ─── Projects ─────────────────────────────────────────────────────────────────

def dyeing_finishing(request):
    return render(request, 'projects/dyeing_finishing.html')

def flour_production(request):
    return render(request, 'projects/flour_production.html')

def power_generation(request):
    return render(request, 'projects/power_generation.html')

def garment_manufacturing(request):
    return render(request, 'projects/garment_manufacturing.html')

def oil_production(request):
    return render(request, 'projects/oil_production.html')


# ─── Contact ──────────────────────────────────────────────────────────────────

def location(request):
    return render(request, 'contact/location.html')


def feedback_view(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not message:
            return JsonResponse({"status": "error", "message": "Name and message are required"}, status=400)

        if not _send_telegram(_build_message(name, email, phone, message)):
            return JsonResponse({"status": "error", "message": "Telegram send failed"}, status=500)

        messages.success(request, "Message sent successfully")
        return redirect("feedback")

    return render(request, "contact/feedback.html")


def management_list(request):
    managements = Management.objects.all().order_by('order')
    return render(request, 'contact/management.html', {'managements': managements})


def leadership_list(request):
    leaderships = Leadership.objects.all().order_by('order')
    return render(request, 'contact/leadership.html', {'leaderships': leaderships})
