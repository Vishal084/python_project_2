import requests

def get_weather(city_name, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        print(f"Current temperature in {city_name}: {temperature_celsius:.2f}°C")
    else:
        print("Error in fetching data or invalid city name.")

def main():
    api_key = "091b1d453bdc30bf15eb4fbff2bf9e05"
    
    # Take city name as input from the user
    city_name = input("Enter City Name: ")
    
    get_weather(city_name, api_key)

if __name__ == "__main__":
    main()

