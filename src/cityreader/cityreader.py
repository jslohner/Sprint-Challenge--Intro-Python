# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

import csv
import decimal

class City:
	def __init__(self, name, lat, lon):
		self.name = name
		self.lat = lat
		self.lon =lon

	def __repr__(self):
		return f'Name - [{self.name}] || Latitude - [{self.lat}] || Longitude - [{self.lon}]\n'

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

def cityreader(cities=[]):
	# open csv file and read it
	with open('./cities.csv', 'r') as file:
		# use csv.reader to get each row as a list
		csvRead = csv.reader(file)
		# create attributes out of the corresponding csv row
		attributes = next(csvRead)
		# initialize attribute indices corresponding attributes in row lists
		attrIndices = {'city': 0, 'lat': 0, 'lng': 0}
		# loop through attributes for each csv row
		for i in range(0, len(attributes)):
			# if current attribute when looping is needed, assign the correct index to attrIndices
			if (attributes[i] == 'city') or (attributes[i] == 'lat') or (attributes[i] == 'lng'):
				attrIndices[attributes[i]] = i
		# create a city for each row
		for row in csvRead:
			cities.append(City(row[attrIndices['city']], float(row[attrIndices['lat']]), float(row[attrIndices['lng']])))

	return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
# for c in cities:
# 	print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
	# within will hold the cities that fall within the specified region
	within = []

	if int(lat1) > int(lat2):
		temp = lat1
		lat1 = lat2
		lat2 = temp

	if int(lon1) > int(lon2):
		temp = lon1
		lon1 = lon2
		lon2 = temp

	for c in cities:
		if (int(c.lat) in range(int(lat1), int(lat2))) and (int(c.lon) in range(int(lon1), int(lon2))):
			within.append(c)

	return within

lat1, lon1 = input('enter first latitude and longitude pair (separated by a comma) - ').split(',')
lat2, lon2 = input('enter second latitude and longitude pair (separated by a comma) - ').split(',')

print(cityreader_stretch(lat1, lon1, lat2, lon2, cities))
