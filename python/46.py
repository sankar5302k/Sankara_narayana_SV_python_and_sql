import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true"
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    current = data.get("current_weather", {})
    temp = current.get("temperature")
    print(f"Current Temperature in Berlin: {temp} C")
except requests.exceptions.RequestException as e:
    print(f"Network or API error: {e}")
