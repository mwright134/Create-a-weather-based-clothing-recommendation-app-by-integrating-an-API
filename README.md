# Create-a-weather-based-clothing-recommendation-application-by-integrating-an-API

## Project Overview
 
Welcome to the README file for creating a weather-based clothing recommendation application by integrating an API! This project incorporates the Openweather API to run successfully.

## Functionality

  The program successfully fetches weather information from the OpenWeatherMap API based on the provided zip code.
  
  It accurately provides temperature, humidity, and clothing suggestions based on the temperature.
  
  It handles invalid zip codes or errors by displaying an appropriate error message.


## Python Script
This is the Python script for the Application:

```
### This program allows a user to see weather information based on zip code
### If a valid zip code is entered, it will return temperature, humidity and clothing suggestions based on the temperature
### If an invalid zip code is entered, it will return an error messsage stating, "Invalid zip code or unable to fetch weather information"

###  Imports the requests library
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

api_key = ""  # API Key for OpenWeatherMap


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
```

## How to run the program

To run this program, follow these steps:

1.) **Install Python**: Ensure that Python is installed on your system. You can download and install Python from the official website: python.org.

2.) **Install Requests Library**: This program relies on the requests library. If you haven't installed it yet, you can do so using pip, the Python package installer, by running the following command in your terminal or command prompt:

```
pip install requests
```

3.) **Get API Key**: You need to obtain an API key from OpenWeatherMap to access their weather API. You can sign up for a free account and generate an API key from the OpenWeatherMap website: openweathermap.org.

4.) **Copy the Code**: Copy the provided Python code into a text editor or an Integrated Development Environment (IDE) of your choice

5.) **Replace API Key**: Replace the placeholder api_key variable with your actual OpenWeatherMap API key.

6.) **Save the File**: Save the file with a .py extension. For example, weather.py.

7.) **Run the Program**: Open a terminal or command prompt, navigate to the directory where the Python file is saved, and run the program by typing:

```
python weather.py
```

Press Enter to execute the program.

8.) **Enter Zip Code**: Once the program is running, it will prompt you to enter a zip code. Input a valid zip code and press Enter.

9.) **View Weather Information**: If the zip code is valid and weather information is successfully retrieved, the program will display the temperature, humidity, and clothing suggestions based on the temperature. If the zip code is invalid or weather information cannot be fetched, an error message will be displayed.

10.) **Repeat**: You can run the program multiple times with different zip codes to check the weather information for different locations.



Note: Don't forget to include your own Openweathermap API Key when coming across the API Key placeholder.

## Contributions

If you have any recommendations or contributions please do not hesiate to fork the repository and submit a pull request with your improvements!

Happy Deploying! 🚀
