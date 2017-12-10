import pyowm
from twilio.rest import Client
from credentials import *

def pullWeather():
    owm = pyowm.OWM(openWeatherMap)

    observation = owm.weather_at_place(location)
    weather = observation.get_weather()
    return weather


def printWeather(weather):
    wind = weather.get_wind()
    temperature = weather.get_temperature('fahrenheit')

    temp = str(temperature['temp'])
    tempMin = str(temperature['temp_min'])
    tempMax = str(temperature['temp_max'])
    status = weather.get_status().lower()
    windSpeed = str(wind['speed'])

    returnStr = "The temperature in " + location + " is around " + temp +  \
    " with a variation from " + tempMin + " to " + tempMax + ". \n" +  \
    "The status is currently " + status + " and the wind speed is " + windSpeed\
    + " miles per hour."


    return returnStr

weather = pullWeather()
toTwilio = printWeather(weather)


# must verify each number you text with a trial account 
client = Client(accountSID, authToken)
for number in cellPhone:
    client.messages.create(body=toTwilio, from_ = twilioNumber, to = number)