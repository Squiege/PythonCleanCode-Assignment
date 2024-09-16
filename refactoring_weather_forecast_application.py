# Weather Forecast Application Script

class GetWeatherData:
    def fetch_weather_data(city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        # Simulated data based on city
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        return weather_data.get(city, {})

class WeatherParser:
    def parse_weather_data(data):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class GetDetailedForecast:
    def get_detailed_forecast(city):
        # Function to provide a detailed weather forecast for a city
        data = GetWeatherData.fetch_weather_data(city)
        return WeatherParser.parse_weather_data(data)

class DisplayWeather:
    def display_weather(city):
        # Function to display the basic weather forecast for a city
        data = GetWeatherData.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = WeatherParser.parse_weather_data(data)
            print(weather_report)

class UserInterface:
    def main():
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = GetDetailedForecast.get_detailed_forecast(city)
            else:
                forecast = DisplayWeather.display_weather(city)
            print(forecast)

if __name__ == "__main__":
    UserInterface.main()