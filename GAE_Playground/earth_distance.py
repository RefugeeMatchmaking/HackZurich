import simplejson
from urllib.request import urlopen


def get_earth_distance(loc1, loc2):
	'''Function that returns the driving distance between two locations'''
	
	#url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(loc1),str(loc2))
	
	#result= simplejson.load(urlopen(url))
	
	#print(result)
	#driving_distance = result['rows'][0]['elements'][0]['distance']['value']/1000 # [km]
	
	lat1, lng1 = lat_long(loc1)
	lat2, lng2 = lat_long(loc2)

	


	return earth_distance



if __name__ == "__main__":
	earth_distance = get_earth_distance("koeln","bonn")
	print(earth_distance)
	