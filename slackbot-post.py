import requests

# Webhook URL
# Typically something like: https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXXXX/XXXXXX...
url = 'https://slack.com/api/chat.postMessage'

# Bot User OAuth Access Token
headers = {
    'Authorization': 'Bearer xoxb-',
    'Content-type': 'application/json;charset=utf-8',
}

# Channel and the message the bot will post
payload = '{"channel" : "#test", "text": "Hello, Slack!"}'

requests.post(url, data=payload, headers=headers)
