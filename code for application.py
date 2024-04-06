### This program allows a user to see weather information based on zip code
### If a valid zip code is entered, it will return temperature, humidity and clothing suggestions based on the temperature
### If an invalid zip code is entered, it will return an error messsage stating, "Invalid zip code or unable to fetch weather information"

### Imports the requests library
import requests

### Retrieves weather data from the OpenWeatherMap API based on the provided zip code.
def get_weather(zip_code, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

### Provides clothing suggestions based on the temperature.
def suggest_clothing(temp):
    if temp < 0:
        return "It's very cold. Wear a heavy coat, hat, and warm boots."
    elif temp < 15:
        return "It's cold. Wear a jacket, pants, and closed-toe shoes."
    elif temp < 25:
        return "It's moderate. Wear a light jacket, pants and comfortable shoes."
    else:
        return "It's hot. Wear short sleeves, shorts, sandals and sunscreen."

### Asks the user to enter a zip code
zip_code = input("Enter a zip code: ")

api_key = "1a41f3f626b949ac6955ea272d5f3a35"  # API Key for OpenWeatherMap


### Calls the get_weather function to retrieve weather data
weather_data = get_weather(zip_code, api_key)

### Checks if the API request was successful
if weather_data.get("cod") == 200:
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]

  
### Prints the temperature, humidity and suggested clothing based on temperature.
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(suggest_clothing(temperature))
else:
    print("Invalid zip code or unable to fetch weather information.") ### Print statement for invalid zip code
