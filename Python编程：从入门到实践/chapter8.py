# #8-1
# def display_message():
#     print("function")
# display_message()
#
# #8-2
# def favorite_book(title):
#     print("One of my favorite books is "+title+".")
# favorite_book("playboy")

# #8-3
# def make_shirt(size,word):
#     print("The shirt size is "+size)
#     print("The shirt word is " + word)
# make_shirt("23","peace and love")
# make_shirt(size="23",word="peace and love")
#
# #8-4
# def make_shirt(size="23",word="I love Python"):
#     print("The shirt size is "+size)
#     print("The shirt word is "+word)
# make_shirt()
# make_shirt(size="15")
# make_shirt("15","love")
#
# #8-5
# def describe_city(city,country='china'):
#     print(city+' is in '+country)
# describe_city('shanghai')
# describe_city('nanjing')
# describe_city('tokyo','japan')

# #8-6
# def city_country(city,country):
#     re=city+','+country
#     return re
# a=city_country('Santiago','chile')
# print(a)
#
# #8-7
# def make_album(name,album,number=' '):
#     c={'n':name,'a':album,}
#     if number:
#         c['nu']=number
#     return c
# ma=make_album('a','b',number=10)
# print(ma)

# #8-8
# def make_album(artist, title, tracks=0):
#     """Build a dictionary containing information about an album."""
#     album_dict = {
#         'artist': artist.title(),
#         'title': title.title(),
#     }
#     if tracks:
#         album_dict['tracks'] = tracks
#     return album_dict
# title_prompt = "\nWhat album are you thinking of? "
# artist_prompt = "Who's the artist? "
# print("Enter 'quit' at any time to stop.")
# while True:
#     title = input(title_prompt)
#     if title == 'quit':
#         break
#     artist = input(artist_prompt)
#     if artist == 'quit':
#         break
#     album = make_album(artist, title)
#     print(album)
# print("\nThanks for responding!")

# # 8-9
# def show_magicians(names):
#     for name in names:
#         print(name.title())
# magicians = ['znn','david','amy']
# show_magicians(magicians)
#
# #8-10
# def show_magicians(names):
#     for name in names:
#         print(name)
# def make_great(names):
#     great_magicians = []
#     while names:
#         magician = names.pop()
#         great_magician = magician + ' the Great'
#         great_magicians.append(great_magician)
#     for great_magician in great_magicians:
#         names.append(great_magician)
# magicians = ['znn', 'david', 'amy']
# show_magicians(magicians)
# print("\n")
# make_great(magicians)
# show_magicians(magicians)

# # 8-11
# def show_magicians(names):
#     for name in names:
#         print(name)
# def make_great(names):
#     great_magicians = []
#     while names:
#         magician = names.pop()
#         great_magician = magician + ' the Great'
#         great_magicians.append(great_magician)
#     for great_magician in great_magicians:
#         names.append(great_magician)
#     return names
# magicians = ['znn', 'david', 'amy']
# show_magicians(magicians)
# print("\nGreat magicians:")
# great_magicians = make_great(magicians[:])
# show_magicians(great_magicians)
# print("\nOriginal magicians:")
# show_magicians(magicians)

# #8-11
# def make_sandwich(*items):
#     for item in items:
#         print("...adding " + item)
#
# make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
# make_sandwich('turkey', 'apple slices', 'honey mustard')
# make_sandwich('peanut butter', 'strawberry jam')
#
# #8-12
# def make_sandwich(*items):
#     for item in items:
#         print("...adding " + item)
#
# make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
# make_sandwich('turkey', 'apple slices', 'honey mustard')
# make_sandwich('peanut butter', 'strawberry jam')
#
# #8-13
# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)
#
# #8-14
# def make_car(manufacturer, model, **options):
#     car_dict = {
#         'manufacturer': manufacturer.title(),
#         'model': model.title(),
#         }
#     for option, value in options.items():
#         car_dict[option] = value
#
#     return car_dict
#
# my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(my_outback)
#
# my_accord = make_car('honda', 'accord', year=1991, color='white',
#         headlights='popup')
# print(my_accord)

