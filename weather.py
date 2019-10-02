import pyowm

owm = pyowm.OWM('2dbd4d8ae880ca5737375946c337f14d', language="uk")

place = input("Місто: ")

observation = owm.weather_at_place(place)
# observation = owm.weather_at_place('Kostopil,UA')
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print("В місті " + place + " зараз " + w.get_detailed_status())
print("Температура: " + str(temp))
