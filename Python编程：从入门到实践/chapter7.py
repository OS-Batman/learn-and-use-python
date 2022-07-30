#7-1
# car=input("waht kind of car would you like to rent?")
# print("Let me see if I can find you a "+car)

#7-2
# people=input("How many people are coming to dinner?")
# people=int(people)
# if people>=9:
#     print("we don't have room")
# elif people<9:
#     print("we have the room")

#7-3
# number=input("please print a number")
# number=int(number)
# if number%10==0:
#     print(str(number)+" is an integer multiple of 10")
# else:
#     print(str(number) + " is not an integer multiple of 10")

#7-4
# prompt ="You need to add some toppings to the pizza"
# prompt+="\n(Enter 'quit' when you are finished.)"
# active=True
# while active:
#     topping = input(prompt)
#     if topping=="quit":
#         active=False
#     else:
#         print("we have add this topping")

#7-5
# prompt="please tell me you age"
# prompt+="\n(Enter 'quit' when you are finished.)\n"
# active=True
# while active:
#     age=input(prompt)
#     if age == "quit":
#         break
#     age=int(age)
#     if age<3:
#         print("You can get in for free")
#     elif age>=3 and age<=12:
#         print("Your ticket is $10")
#     elif age>12:
#         print("Your ticket is $15")

#7-7
#a=1
# while True:
#   a=a+1
#   print(a)

#7-8
# sandwich_orders=["Cheese sandwich","ham sandwich","vegetable sandwich"]
# finished_sandwiches=[]
# while sandwich_orders:
#     sandwich=sandwich_orders.pop()
#     print("I made your "+sandwich)
#     finished_sandwiches.append(sandwich)
# print("\nThe sandwiches have been finished !")
# for finish in finished_sandwiches:
#     print(finish)

#7-9
# sandwich_orders=["Cheese sandwich","ham sandwich","vegetable sandwich","pastrami","pastrami","pastrami"]
# print("The deli is out of pastrami")
# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")
# print(sandwich_orders)

#7-10
# name_prompt = "\nWhat's your name? "
# place_prompt = "If you could visit one place in the world, where would it be? "
# continue_prompt = "\nWould you like to let someone else respond? (yes/no) "
# responses = {}
# while True:
#     name = input(name_prompt)
#     place = input(place_prompt)
#     responses[name] = place
#     repeat = input(continue_prompt)
#     if repeat != 'yes':
#         break
# print("\n--- Results ---")
# for name, place in responses.items():
#     print(name.title() + " would like to visit " + place.title() + ".")
