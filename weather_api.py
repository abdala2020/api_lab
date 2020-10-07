import os
import requests
import logging
from datetime import datetime
import pprint

key = os.getenv("WEATHER_API_KEY") # read the api key from the system env
url = 'http://api.openweathermap.org/data/2.5/forecast'
def main():
    location = get_location()
    weather_data, error = get_current_weather(location, key)
    
     
    if error:
        print("sorry, could not get weather info ")
    else:
        current_temp = get_temp(weather_data)
        print(f"the current temperature: {current_temp}")
        wind_speed = get_wind_speed(weather_data)
        print(f"the current temperature: {wind_speed}")
        weather_description = get_weather_description(weather_data)
        print(f"the current temperature {weather_description}")
    


def get_location():
    city, country_code = ", "
    while len(city) == 0 or not city.isalpha():
        city = input("Please enter a valid city name? ")
    while len(country_code) != 2 :
        country_code = input("Please 2 letters for the country code ")
    location = f'{city},{country_code}'  
    return location      
    

def get_current_weather(location, key):
    try:
        query = {'q': location,'units': 'imperial', 'appid': key }
        response = requests.get(url, params=query)
        logging.info(response.raise_for_status())
        data = response.json()
        return data, None
    except Exception as err:
        print(err)
        return None, err

def get_temp(weather_data):
    try:
        forcast_list = weather_data['list']
        for data in forcast_list:
            temp = data['main']['temp']
        return temp
    except KeyError:
        print("this data is not in the format expected")
        
def get_wind_speed(weather_data):
    try:
        forcast_list = weather_data['list']
        for data in forcast_list:
            wind_speed = data['wind']['speed']
        return wind_speed
    except KeyError:
        print("this data is not in the format expected")
        return "unknown"

def get_weather_description(weather_data):
    try:
        forcast_list = weather_data['list']
        for data in forcast_list:
            weather_description = data['weather'][0]['description']
        return weather_description
    except KeyError:
        print("this data is not in the format expected")
        return "unknown"

main()