import requests
import os
from dotenv import load_dotenv

load_dotenv()


WORKSPACE_ID = os.getenv('WORKSPACE_ID')
CHANNEL_ID = os.getenv('CHANNEL_ID')
WEBHOOK_TOKEN = os.getenv('WEBHOOK_TOKEN')

def send_slack_message_via_webhook(message):
    """
    Sends a message to Slack using the provided webhook URL.

    Parameters:
        message (str): The message text to send.
    """

    webhook_url = "https://hooks.slack.com/services/" + WORKSPACE_ID +  '/' + CHANNEL_ID + '/' + WEBHOOK_TOKEN

    payload = {
        "text": message  # The message to send
    }

    try:
        # Send a POST request to the Slack webhook URL
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()  # Raise an error for bad HTTP responses

        if response.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message. HTTP status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending message via webhook: {e}")


if __name__ == "__main__":
    # Example usage
    send_slack_message_via_webhook("Hello, this is a test message from Python using a webhook!")
