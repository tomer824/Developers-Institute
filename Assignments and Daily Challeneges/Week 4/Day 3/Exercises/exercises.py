# countries = [
# {
#     "Country" : "United States", 
#     "Capital" : "Washington D.C.", 
#     "Continent" : "North America"
# },
# {
#     "Country" : "Israel", 
#     "Capital" : "Jerusalem", 
#     "Continent" : "Asia"
# },
# {
#     "Country" : "United Kingdom", 
#     "Capital" : "London", 
#     "Continent" : "Europe"
# },
# {
#     "Country" : "France", 
#     "Capital" : "Paris", 
#     "Continent" : "Europe"
# },
# {
#     "Country" : "China", 
#     "Capital" : "Beijing", 
#     "Continent" : "Asia"
# }
# ]

# continents = set

# for country in countries:
#      continents.add(country["Continent"])


# print(continents)



# sampleDict = {
#     "name" : "Kelly",
#     "age" : 25,
#     "salary" : 8000,
#     "city" : "New York"
# }

# print(sampleDict)

# keysToRemove = ["name", "salary"]
# for key in keysToRemove:
#     del sampleDict[key]

# print(sampleDict)

names = ["jon", "tom", "omri", "tzivia", "chaim", "alon"]
output = {}

# output = {name[0].upper() : name for name in names}

for name in names:
    key = name[0].upper()
    if key not in output:
        output[key] = [name]
    else:
        output[key].append(name)
        

print(output)