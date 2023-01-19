import requests

r = requests.get(
    'https://login.microsoftonline.com/05970be3-354a-4a2a-9956-5c6455ece5a8/oauth2/v2.0/token', 
    headers={'Content-Type': 'application/x-www-form-urlencoded'},
    data='client_id=d3de027b-72ae-4e86-90c4-1cfd13498e9e&scope=api%3A%2F%2F34110978-d6b8-461c-b6af-dea73303af69/.default&client_secret=tKK8Q~wmRuhelJN4P0KxaRoMG.xsSNYiLtALfdlU&grant_type=client_credentials')

data = r.json()

access_token = data['access_token']
#print(access_token)

w = requests.get(
    'http://localhost:5000/WeatherForecast',
    headers={'Authorization': f'Bearer {access_token}'})

weather = w.json()

print(weather)
