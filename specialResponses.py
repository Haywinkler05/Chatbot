import requests


def GetTime():
    import datetime
    currentTime = datetime.datetime.now().strftime("%I:%M %p")
    return currentTime 

def getWeather(latitude, longitude):
    pointUrl = f"https://api.weather.gov/points/{latitude},{longitude}"
    pointResponse = requests.get(pointUrl)
    if pointResponse.status_code == 200:
        pointData = pointResponse.json()
        forcastUrl = pointData["properties"]["forecast"]
        forcastResponse = requests.get(forcastUrl)
        if forcastResponse.status_code == 200:
            forcastData = forcastResponse.json()
            currentConditions = forcastData["properties"]["periods"][0]
            temperature = currentConditions["temperature"]
            temperatureUnit = currentConditions["temperatureUnit"]
            weather = currentConditions["detailedForecast"]
            return f"According to the National Weather service: The current temperature is {temperature}{temperatureUnit}. Weather: {weather}"
        else:
            return "Unable to fetch forecast data."
    else:
        return "Unable to fetch point data."

 

def get_location():
    response = requests.get("https://ipinfo.io")
    data = response.json()
    loc = data["loc"].split(",")
    latitude = float(loc[0])
    longitude = float(loc[1])
    return latitude, longitude