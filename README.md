# Weather SMS Script

This is a Python script that retrieves the 3-day weather forecast for a given ZIP code and sends it as an SMS message using the Twilio API.

## Getting Started

To use this script, you will need:

- A Weather Underground API key
- A Twilio API key, account SID, and auth token
- A Twilio phone number to send the SMS message from
- A destination phone number to send the SMS message to

### Getting a Weather Underground API Key

You can sign up for a free API key at https://www.wunderground.com/weather/api. Once you have an API key, you can set it as an environment variable named `WEATHER_API_KEY`.

### Getting a Twilio API Key, Account SID, and Auth Token

You can sign up for a free Twilio account at https://www.twilio.com/try-twilio. Once you have an account, you can obtain your account SID and auth token from the console dashboard. You will also need to create a Twilio phone number to send the SMS message from. Once you have these values, you can set them as environment variables named `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`, and `DESTINATION_PHONE_NUMBER`.

Once you have your API keys and Twilio account, populate a file called .env as follows:

```
WEATHER_API_KEY=[your Weather Underground API key]
TWILIO_ACCOUNT_SID=[your Twilio account SID]
TWILIO_AUTH_TOKEN=[your Twilio auth token]
TWILIO_PHONE_NUMBER=[your Twilio phone number]
DESTINATION_PHONE_NUMBER=[the phone number to send the SMS message to]
```

## Running the Script

Once you have set the required environment variables, you can run the script from the command line. If you do not provide a ZIP code as a command line argument, the script will prompt you to enter one.

```
python weather_sms.py [ZIP code]
```


The script will retrieve the 3-day weather forecast for the specified ZIP code and send it as a single SMS message. The message will include the date, high and low temperatures, chance of precipitation, current conditions, and a set of weather emojis based on the forecast.

## Dependencies

This script requires the following Python packages:

- requests
- json
- dotenv
- twilio

You can install these packages using pip:

```
pip install requests json dotenv twilio
```