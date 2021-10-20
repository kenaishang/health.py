pet1 = {
    'color': 'white',
    'hair': 'long',
    'character': ['cute', 'warm', 'beauty']
    }
pet2 = {
    'color': 'white',
    'hair': 'medium',
    'character': ['beautiful', 'angry', 'warm']
    }
pet3 = {
    'color': 'red',
    'hair': 'short',
    'character': ['beau', 'warm', 'wild']
    }
pets = [pet1, pet2, pet3]
for pet in pets:
    print(pet)

favotite_places = {
    'ming': ['beijing'],
    'hong': ['beijing', 'xian'],
    'gang': ['beijing', 'xian', 'tianjin'],
}
for key, values in favotite_places.items():
    if len(values) == 1:
      print(key.title()+" favorite place is")
      for value in values:
         print("\t"+value.title())
    else:
        print(key.title()+" favorite place are ")
        for value in values:
            print("\t" + value.title())
cities = {
    'beijing': {
        'country': 'chaina',
        'population': 100,
        'fact': 'richest',
        },
    'totato': {
        'country': 'jepernese',
        'population': 10,
        'fact': 'richer',
        },
    'new_york': {
        'country': 'america',
        'population': 1,
        'fact': 'rich',
    },
}
for key, values in cities.items():
    print(key.title()+" in "+values['country'].title())
    print("\t"+str(values['population']))
    print("\t"+values['fact'].title())

for key in cities.keys():
    print(key.title())
del cities['beijing']
del cities['new_york']
for key, values in cities.items():
    print(key.title()+" in "+values['country'].title())
    print("\t"+str(values['population']))
    print("\t"+values['fact'].title())
