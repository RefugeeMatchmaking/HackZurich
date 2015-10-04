import requests

def lat_long(city):
	''' function to return latitude and longitude information based on city name '''
	try:
		response = requests.get('http://maps.googleapis.com/maps/api/geocode/json?address='+str(city))
		resp_json_payload = response.json()

		latlong = resp_json_payload['results'][0]['geometry']['location']
		
		lat = latlong['lat']
		lng = latlong['lng']

	except:
		lat=4.5
		lng=2.5


	#lat = 

	return lat, lng


if __name__ == '__main__':
	lat,lng = lat_long('bonn')

	print('lat %.5f' %lat)
	print('lng %.5f' %lng)
