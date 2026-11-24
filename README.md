# cookbot

Sends me a WhatsApp message every morning at 8:00 AM IST with today's menu, so I remember to tell the cook.

## Setup
1. Get a CallMeBot API key: see callmebot.com (WhatsApp API page), save their number, and send it `I allow callmebot to send me messages`.
2. In this repo: Settings → Secrets and variables → Actions → add `PHONE` (e.g. `+919876543210`) and `APIKEY`.
3. Actions tab → "Cook reminder" → Run workflow, to test.

Edit the `MENU` in `remind.py` to change dishes. Change the `cron` line in `.github/workflows/remind.yml` to change the time (it's in UTC; IST = UTC + 5:30).
