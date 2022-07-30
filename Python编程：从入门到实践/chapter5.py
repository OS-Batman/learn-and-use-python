# #5-1
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
#
# #5-2
# m1 = "Zoctopus"
# m2 = "nian"
# m3 = "Zoctopus"
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# # 检查两个字符串相等和不等
# if m1 == m3:
#     print("m1 equal m3")
# if m1 != m2:
#     print("m1 not equal m2")
#
# # 使用函数lower()的测试
# name = 'ADS'
# if name.lower() == 'ads':
#     print("true")
#
# # 检查两个数字相等、不等、大于、小于、大于等于和小于等于
# age = 23
# age_1 = 18
# if age == 23:
#     print("true")
# if age > 18:
#     print("true")
#
# # 使用关键字and和or的测试
# if age > 10 and age_1 < 22:
#     print("true")
# if age > 25 or age_1 < 25:
#     print("true")
#
# # 测试特定的值是否包含在列表中
# if 'audi' in cars:
#     print("in true")
#
# # 测试特定的值是否未包含在列表中
# if 'aaaai' not in cars:
#     print("not in true")
#
# #5-3
# alien_color="green"
# if alien_color=="green":
#     print("you have got 5 points")
# alien_color="yellow"
# if alien_color=="green":
#     print("you have got 5 points")
#
# #5-4
# alien_color="green"
# if alien_color=="green":
#     print("you have got 5 points")
# else:
#     print("you have got 10 points")
# alien_color="yellow"
# if alien_color=="green":
#     print("you have got 5 points")
# else:
#     print("you have got 10 points")
#
# #5-5
# alien_color="green"
# if alien_color=="green":
#     print("you have got 5 points")
# elif alien_color=="yellow":
#     print("you have got 10 points")
# else:
#     print("you have got 15 points")
# alien_color="yellow"
# if alien_color=="green":
#     print("you have got 5 points")
# elif alien_color=="yellow":
#     print("you have got 10 points")
# else:
#     print("you have got 15 points")
# alien_color="red"
# if alien_color=="green":
#     print("you have got 5 points")
# elif alien_color=="yellow":
#     print("you have got 10 points")
# else:
#     print("you have got 15 points")
#
# #5-6
# age=23
# if age<2:
#     print("you are a future star")
# elif age>=2 and age<4 :
#     print("it is the time to learn quantum physics")
# elif age>=4 and age<13 :
#     print("you are boy")
# elif age>=13 and age<20 :
#     print("you are superman")
# elif age>=20 and age<65 :
#     print("you are batman")
# else:
#     print("you out of the time")
#
# #5-7
# favorite_fruits=["apple","watermelon","banana"]
# if "banana" in favorite_fruits:
#     print("you are really like banana")
# if "watermelon" in favorite_fruits:
#     print("you are really like watermelon")
# if "apple" in favorite_fruits:
#     print("you are really like apple")
# if "pear" in favorite_fruits:
#      print("you are really like pear")
#
# #5-8
# lists=["a","b","c","d","admin"]
# for list in lists:
#     if list=="admin":
#         print("Hello admin, would you like to see a status report?")
#     else:
#         print("Hello "+list+", thank you for logging in again")
#
# #5-9
# lists=[]
# if lists:
#     for list in lists:
#         if list=="admin":
#             print("Hello admin, would you like to see a status report?")
#         else:
#             print("Hello "+list+", thank you for logging in again")
# else:
#     print("We need to find some users!")
#
# #5-10
# current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
# new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']
# current_users_lower = [user.lower() for user in current_users]
# for new_user in new_users:
#     if new_user.lower() in current_users_lower:
#         print("Sorry " + new_user + ", that name is taken.")
#     else:
#         print("Great, " + new_user + " is still available.")
#
# #5-11
# numbers = [1,2,3,4,5,6,7,8,9]
# for num in numbers:
#     if num == 1:
#         print("1st")
#     elif num == 2:
#         print("2nd")
#     elif num == 3:
#         print("3rd")
#     else:
#         print(str(num) + "th")