import json
import requests

print('Wprowadź miasto(np. Gdańsk) oraz państwo(np. PL) w postaci(Gdańsk, PL):')
s_city = input()
print()
city_id = 0
appid = "4adae648a189eda18d27baab09a7814c"
try:
    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id =', city_id)
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'id': city_id, 'units': 'metric', 'lang': 'eng', 'APPID': appid})
        data = res.json()
        temp_indeks = 0
        for i in data['list']:
            print(i['dt_txt'], int(i['main']['temp_max']),'/', int(i['main']['temp_min']), u"\u2103",i['weather'][0]['description'])
            temp_indeks+=1
            if temp_indeks == 8:
                print()
                temp_indeks = 0
    except Exception as e:
        print("Exception (forecast):", e)
        pass

    except Exception as e:
        print("Exception (weather):", e)
        pass
except Exception as e:
    print("Exception (find):", e)
    pass

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)