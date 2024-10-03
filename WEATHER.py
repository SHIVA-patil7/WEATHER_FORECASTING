import requests

# Function to get weather data
def get_weather(city):
    api_key = "3805ba5f07f241eb81538438c61fafe8"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Create complete URL
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"

    # Make the HTTP request to the weather API
    response = requests.get(complete_url)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON data returned by the API
        data = response.json()

        # Extract the required weather information
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        weather_desc = data['weather'][0]['description']

        # Display the weather details
        print(f"Temperature: {temperature}°C")
        print(f"Weather Description: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")

    else:
        # If the city is not found, display an error message
        print(f"City {city} not found! Please check the spelling or try another city.")

# Main program to ask for city input
if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
