# `[ comprehensions ]`
from collections import namedtuple
from pprint import pprint as print

Person = namedtuple('Person', ['name', 'city'])

juan = Person(name='Juan', city='Santiago')
pedro = Person(name='Pedro', city='San Juan')
marcos = Person(name='Marcos', city='SANTIAGO')
nabucodonosor = Person(name='Nabucodonosor', city='santiago')

users = [juan     , pedro   , marcos   , nabucodonosor ]

cities = []
for user in users:
    cities.append(user.city)
print(cities)

cities = [user.city for user in users]
print(cities)

cities = {user.city.lower() for user in users}
print(cities)

cities = {user.name: user.city for user in users}
print(cities)

