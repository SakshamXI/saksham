import requests
def weather (c):
    user_input = c
    weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID=30d4741c779ba94c470ca1f63045390a")
    if weather_data.json()['cod'] == '404':
        d = "No City Found"
    else:
        while True:
            try:
                a = weather_data.json()['weather'][0]['main']
                b = round(weather_data.json()['main']['temp'])
            except:
                d = "not possible"
                break
                
            else:
                d = f"The Weather in {c} is {a} and temperature is {b} degree fahrenhite"

                break
    return d

