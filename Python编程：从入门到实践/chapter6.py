# #6-1
# data={"first_name":"Bruce",
#       "last_name":"batman",
#       "age":"28",
#       "city":"Gotham"}
# print(data["first_name"])
# print(data["last_name"])
# print(data["age"])
# print(data["city"])
#
# #6-2
# number={"kobe":"24",
#         "curry":"30",
#         "James":"23",
#         "Jordan":"23",
#         "Young":"11"}
# print(number["kobe"])
# print(number["curry"])
# print(number["James"])
# print(number["Jordan"])
# print(number["Young"])
#
# #6-3
# glossary = {
#     'string': 'A series of characters.',
#     'comment': 'A note in a program that the Python interpreter ignores.',
#     'list': 'A collection of items in a particular order.',
#     'loop': 'Work through a collection of items, one at a time.',
#     'dictionary': "A collection of key-value pairs.",
#     }
# word = 'string'
# print("\n" + word.title() + ": " + glossary[word])
# word = 'comment'
# print("\n" + word.title() + ": " + glossary[word])
# word = 'list'
# print("\n" + word.title() + ": " + glossary[word])
# word = 'loop'
# print("\n" + word.title() + ": " + glossary[word])
# word = 'dictionary'
# print("\n" + word.title() + ": " + glossary[word])
#
# #6-4
# glossary = {
#     'string': 'A series of characters.',
#     'comment': 'A note in a program that the Python interpreter ignores.',
#     'list': 'A collection of items in a particular order.',
#     'loop': 'Work through a collection of items, one at a time.',
#     'dictionary': "A collection of key-value pairs.",
#     'key': 'The first item in a key-value pair in a dictionary.',
#     'value': 'An item associated with a key in a dictionary.',
#     'conditional test': 'A comparison between two values.',
#     'float': 'A numerical value with a decimal component.',
#     'boolean expression': 'An expression that evaluates to True or False.',
#     }
# for word, definition in glossary.items():
#     print("\n" + word.title() + ": " + definition)
#
# #6-5
# rives={"Yangtze_River":"china","Yellow_river":"china","nile":"egypt"}
# for river,country in rives.items():
#     print("\nThe "+river+" runs through "+country)
# for river in rives.keys():
#     print(river)
# for country in rives.values():
#     print(country)
#
# #6-6
# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
# names=['jen','sarah','edward','phil',"batman"]
# for name in names:
#     if name in favorite_languages.keys():
#         print("thank you for taking the poll,"+name)
#     else:
#         print("please take our poll,"+name)
#
# #6-7
# people = []
# person = {
#     'first_name': 'eric',
#     'last_name': 'matthes',
#     'age': 43,
#     'city': 'sitka',
# }
# people.append(person)
# person = {
#     'first_name': 'ever',
#     'last_name': 'matthes',
#     'age': 5,
#     'city': 'sitka',
# }
# people.append(person)
# person = {
#     'first_name': 'willie',
#     'last_name': 'matthes',
#     'age': 8,
#     'city': 'sitka',
# }
# people.append(person)
# for person in people:
#     name = person['first_name'].title() + " " + person['last_name'].title()
#     age = str(person['age'])
#     city = person['city'].title()
#     print(name + ", of " + city + ", is " + age + " years old.")
#
# #6-8
# pets = []
#
# pet = {
#     'type': 'fish',
#     'name': 'john',
#     'owner': 'guido',
#     }
# pets.append(pet)
#
# pet = {
#     'type': 'chicken',
#     'name': 'clarence',
#     'owner': 'tiffany',
#     }
# pets.append(pet)
#
# pet = {
#     'type': 'dog',
#     'name': 'peso',
#     'owner': 'eric',
#     }
# pets.append(pet)
#
# for pet in pets:
#     print("\nHere's what I know about " + pet['name'].title() + ":")
#     for key, value in pet.items():
#         print("\t" + key + ": " + value)
#
# #6-9
# favorite_places = {
#     'znn': ['chengdu', 'shanghai', 'hangzhou'],
#     'yl': ['chengdu', 'huang montains'],
#     'other': ['xian', 'xinjiang', 'nanji']
#     }
#
# for name, places in favorite_places.items():
#     print("\n" + name.title() + " likes the following places:")
#     for place in places:
#         print("- " + place.title())
#
# #6-10
# favorite_numbers = {
#     'mandy': [42, 17],
#     'micah': [42, 39, 56],
#     'gus': [7, 12],
#     }
# for name, numbers in favorite_numbers.items():
#     print("\n" + name.title() + " likes the following numbers:")
#     for number in numbers:
#         print("  " + str(number))
#
# #6-11
# cities = {
#     'santiago': {
#         'country': 'chile',
#         'population': 6158080,
#         'nearby mountains': 'andes',
#         },
#     'talkeetna': {
#         'country': 'alaska',
#         'population': 876,
#         'nearby mountains': 'alaska range',
#         },
#     'kathmandu': {
#         'country': 'nepal',
#         'population': 1003285,
#         'nearby mountains': 'himilaya',
#         }
#     }
# for city, city_info in cities.items():
#     country = city_info['country'].title()
#     population = city_info['population']
#     mountains = city_info['nearby mountains'].title()
#     print("\n" + city.title() + " is in " + country + ".")
#     print("  It has a population of about " + str(population) + ".")
#     print("  The " + mountains + " mountains are nearby.")
#
# #6-12
# aliens = []
# alien = {
#     'name': 'A',
#     'color': 'green',
#     'point': 5,
#     'speed': 'slow',
#     }
# aliens.append(alien)
# alien = {
#     'name': 'B',
#     'color': 'yellow',
#     'point': 10,
#     'speed': 'med',
#     }
# aliens.append(alien)
# alien = {
#     'name': 'C',
#     'color': 'red',
#     'point': 10,
#     'speed': 'fast',
#     }
# aliens.append(alien)
# print(aliens)
# for alien_info in aliens:
#     print("\nHere's what I know about " + alien_info['name'].title() + ":")
#     for key, value in alien_info.items():
#         print("\t" + key + ": " + str(value))