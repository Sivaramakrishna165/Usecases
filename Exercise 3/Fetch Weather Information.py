# This function fetches weather information for a given city using the OpenWeatherMap API.

import json
import requests

def lambda_handler(event, context):
    # Extract city from the event
    city = event.get('city', 'New York')
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        weather_data = response.json()

        if response.status_code == 200:
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'city': city,
                    'temperature': weather_data['main']['temp'],
                    'description': weather_data['weather'][0]['description']
                })
            }
        else:
            return {
                'statusCode': response.status_code,
                'body': json.dumps(weather_data)
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
