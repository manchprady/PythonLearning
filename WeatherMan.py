import json
from tempfile import tempdir
import requests
from urllib import request, response
BASE_URL ="https://api.openweathermap.org/data/2.5/weather?"

API_KEY = "OurKey"
#print welcome message
print("Welcome to WeatherMan's world")
CITY = input("Enter city name: ")
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

response = requests.get(URL)

if response.status_code == 200:
    print("Success")    
    data = response.json() 

    #print the city name
    print ("Please find the weather details of " + data['name'])

    #print the country name
    print("Country Name: " + data['sys']['country'])

    #print the latitude and longitude
    print("Latitude: " + str(data['coord']['lat']))

    #print the tempature
    print("Temperature: " + str(data['main']['temp']))

    #print feels like
    print("Feels Like: " + str(data['main']['feels_like']))

    #print min tempature
    print("Min Tempature: " + str(data['main']['temp_min']))

    #print max tempature
    print("Max Tempature: " + str(data['main']['temp_max']))

    #print pressure
    print("Pressure: " + str(data['main']['pressure']))

    #print humidity
    print("Humidity: " + str(data['main']['humidity']))

    #print wind speed
    print("Wind Speed: " + str(data['wind']['speed']))

    #print weather description
    print("Weather Description: " + str(data['weather'][0]['description']))

    #print visibility
    print("Visibility: " + str(data['visibility']))   
 

else :
    print("Error in the HTTP request")
    print(response.status_code)
    print(response.text)
      

