animal = {
    1 : {
        'name' : 'dog', 
        'id' : 1,
        'legs' : 4,
        'weight' : 100,
        'height' : 3,
        'speed' : 10,
        'family' : 1
    },
    2 : {
        'name' : 'lizard',
        'id' :2,
        'legs' : 4,
        'weight' : 0.5,
        'height' : 0.5,
        'speed' : 2,
        'family' : 2
    },
    3 : {
        'name' : 'tarantula', 
        'id' : 3,
        'legs' : 8,
        'weight' : 1,
        'height' : 0.5,
        'speed' : 2,
        'family' : 4
    }
}

family = {
    1 : {
        'name' : 'mamal'
    },
    2 : {
        'name' : 'reptile'
    },
    3 : {
        'name' : 'insect'
    },
    4 : {
        'name' : 'arachnid'
    },
    5 : {
        'name' : 'amphibian'
    }
}

import json

with open('animals_json.json', 'w') as f:
    json.dump(animal, f) 

with open('family_json.json', 'w') as f:
    json.dump(family, f) 