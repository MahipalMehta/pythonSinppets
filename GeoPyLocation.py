from geopy.geocoders import Nominatim
geolocator=Nominatim(user_agent="specify")
location=geolocator.geocode("Gateway of India")
print(location.address)
print((location.latitude,location.longitude))
print(location.raw)