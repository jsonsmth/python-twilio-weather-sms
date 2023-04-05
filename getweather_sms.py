import requests
import json
import sys
import os
from dotenv import load_dotenv
from twilio.rest import Client


def weather_emoji(weather):
    temp = weather['high_temperature']
    narrative = weather['narrative'].lower()

    emoji_list = []
    if temp is not None and temp > 90:
        emoji_list.append('🌶️')
    elif temp is not None and temp < 40:
        emoji_list.append('⛄')
    
    if 'rain' in narrative:
        emoji_list.append('☔')
    if 'snow' in narrative:
        emoji_list.append('❄️')
    if 'wind' in narrative:
        emoji_list.append('💨')
    if 'sunny' in narrative or 'clear' in narrative:
        emoji_list.append('☀️')
    if 'partly' in narrative or 'times' in narrative:
        emoji_list.append('☀️ ☁️')
    elif 'cloud' in narrative and 'sun' not in narrative:
        emoji_list.append('☁️')
    elif 'cloud' in narrative and 'sun' in narrative:
        emoji_list.append('☁️ ☀️')
    if 'thunder' in narrative or 'lightning' in narrative:
        emoji_list.append('⛈️')
    
    return ' '.join(emoji_list)



load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")
twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
destination_phone_number = os.getenv("DESTINATION_PHONE_NUMBER")

if len(sys.argv) > 1:
    zip_code = sys.argv[1]
else:
    zip_code = input("Enter your zip code: ")

url = f"https://api.weather.com/v3/wx/forecast/daily/5day?postalKey={zip_code}:US&units=e&language=en-US&format=json&apiKey={weather_api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.content)

    forecasts = data["dayOfWeek"]
    weather_data = []
    
    for i, forecast in enumerate(forecasts):
        if i > 2:
            break
        
        weather = {}
        weather["date"] = forecasts[i]
        weather["high_temperature"] = data["temperatureMax"][i]
        weather["low_temperature"] = data["temperatureMin"][i]
        weather["precipitation_chance"] = round(data["qpf"][i] * 100)
        weather["narrative"] = data["narrative"][i]
        weather_data.append(weather)

    # Combine all three forecasts into a single message
    sms_body = f"Weather forecast for {zip_code}:\n\n"
    for weather in weather_data:
        sms_body += f"{weather['date']}:\n"
        sms_body += f"High : {weather['high_temperature']}°F\n"
        sms_body += f"Low : {weather['low_temperature']}°F\n"
        sms_body += f"Precipitation : {weather['precipitation_chance']}%\n"
        sms_body += f"Conditions: {weather['narrative']}\n"
        sms_body += f"Emojis: {weather_emoji(weather)}\n\n"
  
    # Send a single SMS message with all three forecasts
    twilio_client = Client(twilio_account_sid, twilio_auth_token)
    message = twilio_client.messages.create(
        body=sms_body,
        from_=twilio_phone_number,
        to=destination_phone_number
    )
    
    print(f"Message sent with ID: {message.sid}")

else:
    print(f"Could not get weather information. Status code: {response.status_code}, response text: {response.text}")
