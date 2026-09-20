import os
import requests

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")


def send_alert():
    if not WEBHOOK_URL:
        print("❌ Error: WEBHOOK_URL secret is not set.")
        return

    data = {
        "content": "@everyone",
        "embeds": [
            {
                "title": "🚨 The New Experiment Event is Happening now 🚨",
                "description": "[Join Game](https://www.roblox.com/discover/?keyword=steal%20an%20egg)",
                "color": 15158332,
            }
        ],
    }

    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code in [200, 204]:
        print("✅ Alert sent successfully!")
    else:
        print(f"❌ Failed to send: {response.status_code} - {response.text}")


if __name__ == "__main__":
    send_alert()
    
