import requests
import os
from twilio.rest import Client

end_point = "https://api.openweathermap.org/data/2.5/onecall"

api_key = "fee6d4f382b427efb3bf774224e5ea78"
account_sid = "ACc8a2c18adc4a98dadd0a993f67808ec5"
auth_token = "6626c37df73d89dc0ee956a8f4e528ed"

params = {
    "lat":31.633980,
     "lon": 74.872261,
     "exclude": "current,minutely,daily",
     "appid" :api_key
}

response = requests.get(end_point, params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
         condition_code = hour_data["weather"][0]["id"]
         if int(condition_code) <700:
             will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It will rain outside take umbrella.",
        from_='+12672145457',
        to='+918437448151'
    )

print(message)

