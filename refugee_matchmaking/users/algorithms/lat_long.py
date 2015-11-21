import requests
#Note that requests needs to be installed 'pip install requests'

def lat_long(city):
	''' function to return latitude and longitude information based on city name '''
	print('running slow lat long function')
	try:
		response = requests.get('http://maps.googleapis.com/maps/api/geocode/json?address='+str(city))
		resp_json_payload = response.json()

		latlong = resp_json_payload['results'][0]['geometry']['location']
		
		lat = latlong['lat']
		lng = latlong['lng']
		output=(lat,lng)

	except:
		lat=1.1
		lng=1.1

		output=(lat,lng)

	#lat = 

	return output


if __name__ == '__main__':
	lat,lng = lat_long('bonn')

	print('lat %.5f' %lat)
	print('lng %.5f' %lng)
