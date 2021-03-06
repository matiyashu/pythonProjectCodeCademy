# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def hurricanes_damages_update (record_list):
	new_list = []
	for element in record_list:
		if element[-1] == "M":
			new_list.append(float(element[:-1]) * 1000000)
		elif element[-1] == "B":
			new_list.append(float(element[:-1]) * 1000000000)
		elif element == "Damages not recorded":
			new_list.append(element)
	return new_list

updated_damages = hurricanes_damages_update(damages)

print(updated_damages)

# write your construct hurricane dictionary function here:

# 2 solution
"""
# using index() method to returns the position at the first occurrence 
of the specified value inside the list.

def create_hurricane_dictionary():
    hurricanes_dictionary = {}
    for name in names:
        index = names.index(name)
        hurricane_dict = {
            "Name": name, "Month": months[index], "Year": years[index],
            "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index],
            "Damage": updated_damages[index], "Death": deaths[index]
        }
        hurricanes_dictionary[name] = hurricane_dict
    return hurricanes_dictionary

hurricanes = create_hurricane_dictionary()

print(f"\n{hurricanes}")

"""

def h_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):

  hurricanes_dict = {}
  num_of_hurricanes = len(names)

  for element in range(num_of_hurricanes):
    hurricanes_dict[names[element]] = {
    "Name": names[element], 
    "Month": months[element], 
    "Year": years[element], 
    "Max Sustained Wind": max_sustained_winds[element], 
    "Areas Affected": areas_affected[element], 
    "Damage": updated_damages[element], 
    "Deaths": deaths[element]}
  return hurricanes_dict

h_dictionary = h_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(f"\n{h_dictionary}")




# write your construct hurricane by year dictionary function here:

def hurricane_by_year (h_dictionary):
  h_by_year = {}
  for element in years:
    hurricanes_year = []
    for h_element in h_dictionary.values():
      if h_element["Year"] == element:
        hurricanes_year.append(h_element)
      h_by_year[element] = hurricanes_year
  return h_by_year

year_of_h = hurricane_by_year(h_dictionary)
print(f"\n{year_of_h}")
# write your count affected areas function here:

def area_affected(areas):
	affected_area_count = {}
	for element in areas:
		for location in element:
			if affected_area_count.get(location) is None:
				affected_area_count[location] = 1
			else:
				affected_area_count[location] += 1
	return affected_area_count

hurricane_affected_area = area_affected(areas_affected)

print(f"\n{hurricane_affected_area}")




# write your find most affected area function here:
def most_affected_area (areas):
  place = ""
  max_hits = 0
  for area,hits in areas.items():
    if hits > max_hits:
      place = area
      max_hits = hits
  return place, max_hits

affected_area_hur = most_affected_area(hurricane_affected_area)


print(f"\n{affected_area_hur}")


# write your greatest number of deaths function here:

def greatest_mortality(h_dictionary):

    deadliest_hurricane = ''
    deaths = 0

    for element in h_dictionary:
        if h_dictionary[element]["Deaths"] > deaths:
            deadliest_hurricane = element
            deaths = h_dictionary[element]["Deaths"]
    return deadliest_hurricane, deaths

deadliest_hurricane, deaths = greatest_mortality(h_dictionary)
print(f"\nmax_mortality_cane = {deadliest_hurricane}\nmax_mortality = {deaths}")
# write your catgeorize by mortality function here:

def hurricane_mortality_category (h_dictionary):
	mortality_category = {	0 : [], 
							1 : [], 
							2 : [], 
							3 : [], 
							4 : [] }
							
	for  element in h_dictionary:
		category = 0
		deceased_victim = h_dictionary[element]["Deaths"]

		if deceased_victim < 100:
			category = 0
		elif deceased_victim >= 100 and deceased_victim < 500:
			category = 1
		elif deceased_victim >= 500 and deceased_victim < 1000:
			category = 2
		elif deceased_victim >= 1000 and deceased_victim < 10000:
			category = 3
		else:
			category = 4

		if category not in mortality_category:
			mortality_category[category] = h_dictionary[element]
		else:
			mortality_category[category].append(h_dictionary[element])
	return mortality_category


cane_mortality_category = hurricane_mortality_category(h_dictionary)

print(f"\n{cane_mortality_category}")





# write your greatest damage function here:

def greatest_damage_func(h_dictionary):
    dmg_list = []
    for name in h_dictionary:
        if h_dictionary[name]['Damage'] != 'Damages not recorded':
            dmg_list.append(h_dictionary[name]['Damage'])

    greatest_damage = max(dmg_list)

    for name in h_dictionary:
        if h_dictionary[name]['Damage'] == greatest_damage:
            return name, greatest_damage


print(f"\nThis is the most destructive hurricane_mortality_category : {greatest_damage_func(h_dictionary)}")




# write your catgeorize by damage function here:

def damage_scaled(hurricanes):

    scale_dict = {0: [], 1: [], 2: [], 3: [], 4: []}

    for element in hurricanes:

        power_rate = 0
        damage = hurricanes[element]["Damage"]

        if damage == "Damages not recorded":
            continue
        elif damage < 100000000:
            power_rate = 0
        elif damage >= 100000000 and damage < 1000000000:
            power_rate = 1
        elif damage >= 1000000000 and damage < 10000000000:
            power_rate = 2
        elif damage >= 10000000000 and damage < 50000000000:
            power_rate = 3
        else:
            power_rate = 4

        if power_rate not in scale_dict:
            scale_dict[power_rate] = hurricanes[element]
        else:
            scale_dict[power_rate].append(hurricanes[element])

    return scale_dict

damage_scale = damage_scaled(h_dictionary)

print(f"\nThis is the damage scale: \n{damage_scale}")


