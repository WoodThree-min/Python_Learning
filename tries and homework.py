#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 17:46:23 2020

@author: risugi
"""

#%% Chapter 2

my_name = "Shan LI"
print("Hello " + my_name + ", would you like to learn some Python today?")
print(my_name.title())
print(my_name.upper())
print(my_name.lower())

famous_person = 'Albert Einstein'
message = "A person who never made a mistake never tried anything new."
print(famous_person.title() + " once said," + '"' + message + '"')

test_name = " \t amy\n  "
print(test_name)
print(test_name.strip())
print(test_name.lstrip())
print(test_name.rstrip())

import this

#%% Chapter 3.1-3.7

names = ['zhao', 'zhou', 'wu', 'zheng', 'wang']
for name in names:
    message = 'Hello, ' + name.title() + '!' 
    message += '\tWould you like to have a dinner with me?'
    print(message)
    
guest_refused = 'wu'
print('\nSorry! ' + guest_refused.title() +' cannot come.\n')
new_invited = 'yang'
print('I would like to invite a new guest.\n')
index = 0
for name in names:
    if name.lower() == guest_refused.lower():
        names[index] = new_invited
      
    index += 1
        
    
for name in names:
    print('Hello, ' + name.title() + '! Would you like to have a dinner with me?')
    
print('\nI found a bigger table. So I would like to invite more people.\n')
names.insert(0,'qian')
names.insert(4,'sun')
names.append('li')
for name in names:
    print('Hello, ' + name.title() + '! Would you like to have a dinner with me?')
    
print('\nThe new table cannot delivered in time. I have to cut the list.\n')
while len(names) > 2:
    cut_guest = names.pop()
    print(cut_guest.title() + ', I am so sorry that you are not in the inviting list.')
    
for name in names:
    print(name.title() + ', I am glad to inform you that you are still in the inviting list.')
    
print(names)
del names[0]
print(names)
del names[0]
print(names)

#%% Chapter 3.8-

place_visit = ['Romania', 'London', 'Scottland', 'Iceland', 'Paris']
print(place_visit)
print(sorted(place_visit))
print(place_visit)
print(sorted(place_visit, reverse=True))
print(place_visit)

place_visit.reverse()
print(place_visit)
place_visit.reverse()
print(place_visit)
place_visit.sort()
print(place_visit)
place_visit.sort(reverse=True)
print(place_visit)


print('\nI want to go ' + str(len(place_visit)) + ' places.')

#%% Chapter 4.1-4.12

number_list = list(range(1,1000001))
number_1m_min = min(number_list)
number_1m_max = max(number_list)
number_1m_sum = sum(number_list)
print([number_1m_min, number_1m_max, number_1m_sum])

odd_number = list(range(1,21,2))
print(odd_number)

multi3 = []
for i in range(3,31):
    if i%3 == 0:
        multi3.append(i)

print(multi3)

cubes = [value**3 for value in range(1,11)]
print(cubes)

print('\nThe first three items in the list are: ')
print(cubes[:3])

print('\nThree items from the middle of the list are: ')
print(cubes[4:7])

print('\nThe last three items in the list are: ')
print(cubes[-3:])

#%% Chapter 4.13-

foods = ('burger', 'pizza', 'noodles', 'fish', 'cake')
for item in foods:
    print(item.title())
    
    
# foods[0] = 'chickens'
print('Original foods:')
print(foods)

print('Replace "fish" to "shushi", replace "noodles" to "rice"')
new_foods = ('burger', 'pizza' ,'rice', 'shushi', 'cake') 
# i = 0
# for food in foods:
#     if food == 'fish':
#         new_foods[i] = 'shushi'
#     elif food == 'noodles':
#         new_foods[i] = 'rice'
#     else:
#         new_foods[i] = food
#     i += 1
        
print('\nModified foods: ')
print(new_foods)
         
#%% Chapter 5

alien_color = 'blue'
score = 0
if alien_color == 'green':
    score += 5
    print('The player get ' + str(score) + ' scores.')
elif alien_color == 'yellow':
    score += 10
    print('The player get ' + str(score) + ' scores.')
elif alien_color == 'red':
    score += 15
    print('The player get ' + str(score) + ' scores.')
    
users = ['resugi', 'takki', 'mesa', 'admin', 'karl']
if len(users)==0:
    print('We need to find some users!')
else:
    for user in users:
        if user.lower() == 'admin':
            print('Hello ' + user.lower() + ', would you like to see a status report?')
        else:
            print('Hello ' + user.title() + ', thank you for logging in again.')
        
#%% Chapter 6.1-6.7

info_1 = {'first_name':'Jin',
        'last_name':'Tian',
        'age':'26',
        'city':'Shanghai'}
info_2 = {'first_name':'Zhang',
        'last_name':'Yao',
        'age':'24',
        'city':'Qingdao'}
info_3 = {'first_name':'Li',
        'last_name':'Shan',
        'age':'25',
        'city':'Lvliang'}
people =[info_1, info_2, info_3]
for key, value in info_1.items():
    print('\nKey: '+ key)
    print('Value: '+ value + '\n')
for info in people:
    for key, value in info.items():
        print('\nKey: ' + key)
        print('Value: ' + value)
    
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python'}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')
polls = ['jen','edward', 'resugi','invictus']
for poll in polls:
    if poll in favorite_languages.keys():
        print('\nThank you!' + poll.title() + '.')
    else:
        print('\n' + poll.title() + ', We are glad to invite you to take the survey.')

#%% Chapter 6.8-

einstein = {'type': 'dog','owner': 'Zhang'}
fisher = {'type': 'cat', 'owner': 'chen'}
roxy = {'type': 'cat', 'owner': 'Lan'}
pets = [einstein, fisher, roxy]
print('\nPets:')
for pet in pets:
    print(pet)

favorite_places = {
    'Zhang':['Qingdao', 'Taiwan'],
    'Li':['Taiyuan', 'iceland'],
    'ji':['Shanghai', 'Tokio', 'Osaka'],
    }
for name, places in favorite_places.items():
    print(name.title() + "'s favorite places are: ")
    for place in places:
        print('\t' + place.title())

#%% Chapter 7.1-7.3
    
Car_rent = input("What kind of car would you like to rent? ")
print('Let me see if I can find you a ' + Car_rent.title())

inquiry = input('How many people will have the dinner? ')
if int(inquiry) > 8:
    print('Sorry! The table is unavailable.')
else:
    print('Congrats! The table is available.')

number = input('Please input an int number: ')
if int(number)%10 == 0:
    print('The number can be divided by 10.')
else:
    print('The number can not be divided by 10.')
    
#%% Chapter 7.4

active =True
while active:
    age = input('Please tell me your age: ')
    if age == 'quit':
        break
    else:
        if int(age) < 4:
            print('You are free for this movie.')
        elif int(age) < 13:
            print('Your ticket is 10 dollar.')
        else:
            print('Your ticket is 15 dollar.')

#%% Chapter 8
            
def display_message():
    print('We are going to learn some functions.')

def favorite_book(title):
    print('One of my favorite book is ' + title.title() + ' .')    
favorite_book('alice in wonderland')

def make_shirt(size='L', stamp='I Love Python'):
    print('\nI want to make a shirt :')
    print('\tSize: ' + size)
    print('\tStamp: ' + stamp)
T_1 = make_shirt()
T_2 = make_shirt('S', 'GREAT!!!')    
T_3 = make_shirt('M')


































































































