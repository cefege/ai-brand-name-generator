import csv # import module for saving csv files
import sng # import module startup-name-generator (sng) for use generator models
from pronounceable import Complexity # import class Complexity for word complexity calculations


# Function for generating brand names based on
# two startup-name-generator models (trained on latin and pokemon wordlists)
#
# - domains_number parameter must be a multiple of 2
# - function returns csv_data in list format with rows lists
#
def generate_brand_name(domains_number):
	latin_gen = sng.Generator.load('latin_model') # load latin model
	pokemon_gen = sng.Generator.load('pokemon_model') # load pokemon model
	complexity = Complexity() # create object of class Complexity to calculate words complexity

	# generate latin brands
	latin_brands = []
	for _ in range(int(domains_number/2)):
		brand = 'qxyz'
		while 'q' in brand or 'x' in brand or 'y' in brand or 'z' in brand: # exclude characters 'q', 'x', 'y' and 'z'
			brand = latin_gen.simulate(n=1, max_word_len=15)[0].lower()

		latin_brands.append(brand)

	# generate pokemon brands
	pokemon_brands = []
	for _ in range(int(domains_number/2)):
		brand = 'qxyz'
		while 'q' in brand or 'x' in brand or 'y' in brand or 'z' in brand: # exclude characters 'q', 'x', 'y' and 'z'
			brand = pokemon_gen.simulate(n=1, max_word_len=15)[0].lower()

		pokemon_brands.append(brand)

	csv_data = []

	# append latin brands to csv_data list
	for brand in latin_brands:
		csv_data.append([brand, 'latin', complexity.complexity(brand)])

	# append pokemon brands to csv_data list
	for brand in pokemon_brands:
		csv_data.append([brand, 'pokemon', complexity.complexity(brand)])

	csv_data.sort(key = lambda x: x[2]) # sort brands by complexity - from min to max
	csv_data.insert(0, ['Brand Name', 'Generation Source', 'Complexity Score']) # insert column names to csv_data

	return csv_data


# Function for saving csv file
def save_csv(csv_brands, file_path):
	with open(file_path, 'w') as file:
		csv_writer = csv.writer(file, delimiter=',') # create csv_writer object

		# writing csv file row by row
		for row in csv_brands:
			csv_writer.writerow(row)
			print(row)


# Code below will run if you execute this file
if __name__ == '__main__':
	csv_brands = generate_brand_name(50) # generating 50 brands in csv format
	save_csv(csv_brands, 'result.csv') # saving generated brands to csv file
