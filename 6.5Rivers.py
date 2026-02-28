#My home in CO was on the banks of the Dolores River
#The Dolores feeds into the Greater Colorado River near Utah

rivers = {
    'amazon': 'peru',
    'dolores': 'united states',
    'ganges': 'india'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers included in the dictionary:")
for river in rivers.keys():
    print(river.title())

print("\nCountries included in the dictionary:")
for country in rivers.values():
    print(country.title())