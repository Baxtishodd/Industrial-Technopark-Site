from django.shortcuts import render, redirect
import requests
import os
from dotenv import load_dotenv
from django.contrib import messages
from django.http import JsonResponse
from core.models import Management, Leadership

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def _send_telegram(name, email, phone, message):
    text = f"""
📩 New Inquiry

👤 Name: {name}
📧 Email: {email}
📞 Phone: {phone}

📝 Message:
{message}
"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(url, data={"chat_id": CHAT_ID, "text": text})
    return response.status_code == 200


def _handle_feedback_post(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    message = request.POST.get("message")

    if not name or not message:
        return JsonResponse({"status": "error", "message": "Name and message are required"}, status=400)

    try:
        success = _send_telegram(name, email, phone, message)
        if not success:
            return JsonResponse({"status": "error", "message": "Telegram send failed"}, status=500)
    except Exception:
        return JsonResponse({"status": "error", "message": "Server error"}, status=500)

    messages.success(request, "Message sent successfully")
    return redirect("feedback")


def home(request):
    if request.method == "POST":
        return _handle_feedback_post(request)
    return render(request, 'core/home.html')


def electric_power(request):
    return render(request, template_name='services/electric_power.html')


def security(request):
    return render(request, template_name='services/security.html')


def hot_water(request):
    return render(request, template_name='services/hot_water.html')


def steam_supply(request):
    return render(request, template_name='services/steam_supply.html')


def gas_supply(request):
    return render(request, template_name='services/gas_supply.html')


def dyeing_finishing(request):
    return render(request, template_name='projects/dyeing_finishing.html')


def flour_production(request):
    return render(request, template_name='projects/flour_production.html')


def power_generation(request):
    return render(request, template_name='projects/power_generation.html')


def garment_manufacturing(request):
    return render(request, template_name='projects/garment_manufacturing.html')


def oil_production(request):
    return render(request, template_name='projects/oil_production.html')


def location(request):
    return render(request, template_name='contact/location.html')


def feedback_view(request):
    if request.method == "POST":
        return _handle_feedback_post(request)
    return render(request, "contact/feedback.html")


def management_list(request):
    managements = Management.objects.all().order_by('order')
    return render(request, 'contact/management.html', {'managements': managements})


def leadership_list(request):
    leaderships = Leadership.objects.all().order_by('order')
    return render(request, 'contact/leadership.html', {'leaderships': leaderships})
