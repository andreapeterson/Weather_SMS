import requests
from twilio.rest import Client
import config

account_sid = config.TWILIO_ACCOUNT_SID
auth_token = config.TWILIO_AUTH_TOKEN

weather_parameters = {
    "lat": config.MY_LAT,
    "lon": config.MY_LONG,
    "appid": config.WEATHER_API_KEY,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get("https://api.openweathermap.org/data/2.8/onecall", params=weather_parameters)
response.raise_for_status()

data = response.json()

for item in range(0, 12):
    if (data["hourly"][0]["weather"][0]["id"]) < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="Good morning, there is rain forecasted in the next 12 hours. Schedule your run around it!",
            from_='+18663117738',
            to='+1 321 432 2740'
        )
        break
