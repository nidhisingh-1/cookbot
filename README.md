# cookbot

Sends me a WhatsApp message every morning at 8:00 AM IST with today's menu, so I remember to tell the cook.
Uses Meta's official WhatsApp Cloud API (free test number) and runs on GitHub Actions.

## Setup
1. developers.facebook.com → My Apps → Create app (Business type) → add the **WhatsApp** product.
2. WhatsApp → API Setup: add and verify your own number as a recipient. Note the **Phone number ID**.
3. WhatsApp Manager → Message templates → create template:
   - Name `cook_reminder`, category **Utility**, language **English** (`en`)
   - Body: `Good morning! Today is {{1}}. Please tell the cook to make: {{2}}. Have a nice day!`
4. Business Settings → Users → System users → add an Admin system user → assign your app and WhatsApp account →
   Generate token (expiry: Never) with `whatsapp_business_messaging` and `whatsapp_business_management`.
5. Repo Settings → Secrets and variables → Actions → add:
   - `PHONE`: your number with country code, e.g. `919876543210`
   - `WA_PHONE_NUMBER_ID`: from step 2
   - `WA_TOKEN`: from step 4
6. Actions tab → "Cook reminder" → Run workflow, to test.

Edit `MENU` in `remind.py` to change dishes. Change the `cron` line in `.github/workflows/remind.yml` to change the time (UTC; IST = UTC + 5:30).
