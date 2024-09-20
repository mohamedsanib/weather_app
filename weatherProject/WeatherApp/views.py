from django.shortcuts import render
import requests
import datetime
def App(request):
    if 'city' in request.POST:
        CITY = request.POST['city']
    else:
        CITY = 'punjab'
    
    API_KEY = '439268e4643a9e5b9d984cc070a706f1'
    URL = 'http://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q' : CITY, 'appid' : API_KEY, 'units':'metric'} 
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    desc = res['weather'][0]['description']
    img = res['weather'][0]['icon']
    tem = res['main']['temp']
    hum = res['main']['humidity']
    wind = res['wind']['speed']
    day = datetime.date.today()
    return render(request, 'weather/index.html', {'desc' : desc, 'img' : img,
    'tem' : tem, 'hum':hum, 'wind':wind, 'CITY':CITY, 'date':day})

