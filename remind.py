"""Sends a daily WhatsApp reminder (via Meta's WhatsApp Cloud API) with today's menu for the cook."""
import datetime
import json
import os
import urllib.error
import urllib.request

# Edit this to your actual weekly menu
MENU = {
    "Monday":    "Dal tadka, jeera rice, bhindi",
    "Tuesday":   "Rajma chawal, salad",
    "Wednesday": "Paneer bhurji, roti",
    "Thursday":  "Chole, rice",
    "Friday":    "Aloo gobi, dal, roti",
    "Saturday":  "Khichdi, papad",
    "Sunday":    "Your choice / eat out",
}

TEMPLATE_NAME = os.environ.get("WA_TEMPLATE", "cook_reminder")
TEMPLATE_LANG = os.environ.get("WA_TEMPLATE_LANG", "en")
API_VERSION = os.environ.get("WA_API_VERSION", "v23.0")

# GitHub runners use UTC; shift to IST so the weekday is right
now_ist = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5, minutes=30)
today = now_ist.strftime("%A")

payload = {
    "messaging_product": "whatsapp",
    "to": os.environ["PHONE"].lstrip("+").replace(" ", ""),
    "type": "template",
    "template": {
        "name": TEMPLATE_NAME,
        "language": {"code": TEMPLATE_LANG},
        "components": [{
            "type": "body",
            "parameters": [
                {"type": "text", "text": today},        # {{1}}
                {"type": "text", "text": MENU[today]},  # {{2}}
            ],
        }],
    },
}

req = urllib.request.Request(
    f"https://graph.facebook.com/{API_VERSION}/{os.environ['WA_PHONE_NUMBER_ID']}/messages",
    data=json.dumps(payload).encode(),
    headers={
        "Authorization": f"Bearer {os.environ['WA_TOKEN']}",
        "Content-Type": "application/json",
    },
)
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        print(resp.status, resp.read().decode())
except urllib.error.HTTPError as e:
    print(e.code, e.read().decode())
    raise SystemExit(1)
