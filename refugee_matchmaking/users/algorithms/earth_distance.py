import json
#from urllib.request import urlopen
from math import radians, cos, sin, asin, sqrt
from .lat_long import lat_long


def get_earth_distance(loc1, loc2):
	'''Function that returns the haversine distance between two locations'''
	
	#url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(loc1),str(loc2))
	
	#result= simplejson.load(urlopen(url))
	
	#print(result)
	#driving_distance = result['rows'][0]['elements'][0]['distance']['value']/1000 # [km]
	
	lat1, lon1 = lat_long(loc1)
	lat2, lon2 = lat_long(loc2)

	return haversine(lon1, lat1, lon2, lat2)


def haversine(lon1, lat1, lon2, lat2):

	lon1, lat1, lon2, lat3 = map(radians,[lon1, lat1, lon2, lat2])

	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
	c = 2*asin(sqrt(a))
	r = 6371
	ans=c*r

	return ans #[m]

#What is this for? _Asked_By_PJ
# if __name__ == "__main__":
# 	earth_distance = get_earth_distance("koeln","bonn")
# 	print(earth_distance)
	