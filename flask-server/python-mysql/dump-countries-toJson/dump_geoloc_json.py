import json

countries_data = open("../../data/Countries-State-Cities_CleanedUp/countries.json")
countries = json.load(countries_data)

STATES_CITIES_COUNTRIES = [];

for country in  countries:
	for state_dict in countries[country]:
		for state in state_dict:
			list_of_cities = state_dict[state]
			for city in list_of_cities:
				STATES_CITIES_COUNTRIES.append((country, state, city))
				

	
SCC = json.dumps(STATES_CITIES_COUNTRIES) 
print(SCC)
output = open("country-state-city.json", 'w')
output.write(SCC)
output.close()
