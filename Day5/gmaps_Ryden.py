# pip install googlemaps
#https://console.developers.google.com/apis/credentials?project=_
#need maps and distance APIs enabled
import googlemaps
api_key = 'your api key from developers.google.com'
gmaps = googlemaps.Client(api_key)
dir(gmaps)
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
location=gmaps.geocode(whitehouse)
print location
print location[0]
print location[0]['geometry']['location']
latlng=location[0]['geometry']['location']
lat, lng=latlng.values()

destination = gmaps.reverse_geocode(latlng)
print destination 

duke = gmaps.geocode('326 Perkins Library, Durham, NC 27708')
duke=duke[0]['geometry']['location']
distance = gmaps.distance_matrix(duke, latlng)
distance['rows'][0]['elements'][0]['distance']['text']
distance['rows'][0]['elements'][0]['distance']['value']


embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]



# TODO: write code to answer the following questions: 
# which embassy is closest to the White House in meters? how far? 


def nearest(place, others):
	lengths = dists(place, others)
	smallest = min(lengths)
	match = lengths.index(smallest)
	return match


def dists(origin, place_list):
	distances = []
	if type(origin) != str:
		origin = gmaps.reverse_geocode(origin)[0]['geometry']['location']
	for place in place_list:
		latlng = gmaps.reverse_geocode(place)[0]['geometry']['location']
		dist = gmaps.distance_matrix(origin, latlng)
		distances.append(dist['rows'][0]['elements'][0]['distance']['value'])
	return distances

# what is its address? You will get errors - debug
def find_place(place_list):
	places = []
	for place in place_list:
		places.append(gmaps.reverse_geocode(place)[0]['formatted_address'])
	return places
# if I wanted to hold a morning meeting there, which cafe would you suggest?
def nearest_venue(original_location, other_locations, venue_type):
	nearby = nearest(original_location, other_locations)
	embassy = other_locations[nearby]
	search = gmaps.places(query = venue_type, location = embassy)['results']
	venues = []
	for i in search:
		loc = i['geometry']['location']
		coords = [loc['lat'], loc['lng']]
		venues.append(coords)
	near_venue = nearest(embassy, venues)
	return str(search[near_venue]['name'])

nearest_venue(whitehouse, embassies, 'cafe')

# if I wanted to hold an evening meeting there, which bar would you suggest? 

nearest_venue(whitehouse, embassies, 'bar')

