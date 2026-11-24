"""Sends a daily WhatsApp reminder (via CallMeBot) with today's menu for the cook."""
import datetime
import os
import urllib.parse
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

# GitHub runners use UTC; shift to IST so the weekday is right
now_ist = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5, minutes=30)
today = now_ist.strftime("%A")
msg = f"🍳 Tell the cook! Today ({today}): {MENU[today]}"

url = "https://api.callmebot.com/whatsapp.php?" + urllib.parse.urlencode({
    "phone": os.environ["PHONE"],
    "text": msg,
    "apikey": os.environ["APIKEY"],
})
with urllib.request.urlopen(url, timeout=30) as resp:
    print(resp.status, resp.read().decode()[:500])
