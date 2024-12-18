import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'weather': data['weather'][0]['description']
        }
    else:
        return None

def display_weather(weather_data):
    if weather_data:
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Weather: {weather_data['weather']}")
    else:
        print("Failed to retrieve weather data")

if __name__ == "__main__":
    api_key = "d2178a271b0d31d5249f22d8ee62b76d"
    city = input("Enter the city name: ")
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)