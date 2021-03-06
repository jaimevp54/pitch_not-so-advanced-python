#HSLIDE
## Not so advanced python
## <span style="font-size:0.6em; color:gray">(for real)</span> 

#HSLIDE
### `>>> help()`

#HSLIDE
### `[ comprehensions ]`
#VSLIDE
##### Ex 1:
```python
juan = Person(name='Juan', city='Santiago')
pedro = Person(name='Pedro', city='San Juan')
marcos = Person(name='Marcos', city='SANTIAGO')
nabucodonosor = Person(name='Nabucodonosor', city='santiago')

users = [juan     , pedro   , marcos   , nabucodonosor ]
```
#VSLIDE
```python
cities = []
for user in users:
    cities.append(user.city)
# cities -> ['Santiago', 'San Juan', 'SANTIAGO', 'santiago']
```
#VSLIDE
#### Lists
```python
cities = [user.city for user in users]
# cities -> ['Santiago', 'San Juan', 'SANTIAGO', 'santiago']
```
#VSLIDE
#### Sets
```python
cities = {user.city.lower() for user in users}
# cities -> {'santiago', 'san juan'}
```
#VSLIDE
#### Dictionaries
```python
cities = {user.name: user.city for user in users}
# cities -> {
#    'Nabucodonosor': 'santiago',
#    'Pedro': 'San Juan',
#    'Marcos': 'SANTIAGO',
#    'Juan': 'Santiago'
#    }
```
#VSLIDE
##### Ex 2:
```python
from random import randrange

random_list = []
for i in range(10):
    random_list.append(randrange(100))

divided_by_3 = []
for number in random_list:
    if number%3==0:
        divided_by_3.append(number)

less_than_15 = []
for number in random_list:
    if number<15:
        less_than_15.append(number)
        
how_many_odds = 0 
for number in random_list:
    if number%2 != 0:
        how_many_odds += 1
```
#VSLIDE
```python
from random import randrange

random_list = [randrange(100) for i in range(10)]

divided_by_3 = [number for number in random_list if number%3==0]
less_than_15 = [number for number in random_list if number<15]
how_many_odds = len([number for number in random_list if number%2 != 0])
```

#HSLIDE
### $$\lambda ambda  functions:$$
#VSLIDE
`lambda argument: manipulate(argument)`
#VSLIDE
```
def mul_by_two(x):
    return x*2
```
```python
mul_by_two = lambda x : x*2
``` 
<!-- .element: class="fragment" -->
#VSLIDE
##### Ex 1: 
```python
list_of['int'](3)
# [34, 23, 15]
list_of['float'](3)
# [34.5345, 4.1239, 88.6531]
```
#VSLIDE
##### Ex 1:
```python
from random import randrange, random

def list_of_integers(length): 
    result = []
    for _ in range(length):
        result.append(randrange(100))
    return result

def list_of_floats(length): 
    result = []
    for _ in range(length):
        result.append(random()*100)
    return result

list_of = {
    'int': list_of_integers,
    'float': list_of_floats,
}
```
#VSLIDE
##### Ex 1:
```python
list_of = {
    'int': lambda length: [randrange(100) for _ in range(length)],
    'float': lambda length: [random()*100 for _ in range(length)],
}
```
#VSLIDE
##### Ex 2:
```python
def find(item_list, condition):
    for item in item_list: 
        try:
            if condition(item):
                return item
        except Exception as e:
            pass
            # print("Error: "+str(item)+" -> "+str(e.__class__))
```
#VSLIDE
```python
my_list = [12.34, 'Carlos', 34, {'color':'verde'}]
```
```python
def my_func(arg):
    return len(arg)>5

my_str = find(my_list, condition=my_func)
# my_str -> 'Carlos'
```
<!-- .element: class="fragment" -->
```python
my_str = find(my_list, condition=lambda x: len(x)>5)
# my_str -> 'Carlos'
```
<!-- .element: class="fragment" -->

#VSLIDE
```python
my_list = [12.34, 'Carlos', 34, {'color':'verde'}]
```
```python
find(my_list, lambda x: type(x) is int)
#34 

find(my_list, lambda x: x['color'])
# {'color': 'verde'}

find(my_list, lambda x: x.nombre)
# None
```

#HSLIDE
### \_\_magic\_methods\_\_()
#VSLIDE
- \_\_add\_\_()
    - <span style="font-size:0.6em; color:gray">a+b</span>
- \_\_mul\_\_()
    - <span style="font-size:0.6em; color:gray">a\*b</span>
- \_\_doc\_\_
    - <span style="font-size:0.6em; color:gray">help()</span>
- \_\_init\_\_()
    - <span style="font-size:0.6em; color:gray">Dog(name='Rufus')</span>
- \_\_str\_\_()
    - <span style="font-size:0.6em; color:gray">str()</span>
- \_\_len\_\_()
    - <span style="font-size:0.6em; color:gray">len()</span>

#VSLIDE
```python
class SuperString(str):
    """ Class for the strings who want something more from life. """

    __doc__ = "Awesome " +__doc__

    def __neg__(self):
        return self.__class__(''.join(list(reversed(self))))

    def __sub__(self, other):
        if type(other)==str:
            return self.__class__(''.join([c for c in self if c not in other]))
```
#VSLIDE
- help('SPECIALMETHODS')
- [Python Docs](https://docs.python.org/2/reference/datamodel.html)

#HSLIDE
### with... as... :

#VSLIDE
```python
f = open('file.txt')
try: 
    f.do_something()
finally:
    f.close()
```
```python
with open('file.txt') as f:
    f.do_something()
```
<!-- .element: class="fragment" -->

#VSLIDE
```python
class Pizza():
    def __init__(self, ingredient):
        self.ingredient = ingredient 

    def __enter__(self):
        print('Buying a {} pizza'.format(self.ingredient))
        return 'A {} pizza'.format(self.ingredient)

    def __exit__(self, _type, value, traceback):
        print('Cleaning after my mess of {}!'.format(self.ingredient))
```
```python
with Pizza('lobster') as pizza: 
    print("I'm eating {}.".format(pizza))
# Buying a lobster pizza
# A lobster pizza
# Cleaning after my mess of lobster!
```
<!-- .element: class="fragment" -->
```python
with Pizza('lobster') as pizza1, Pizza('peperoni') as pizza2: 
    print("I'm eating {} and {}.".format(pizza1, pizza2)) 
# Buying a lobster pizza
# Buying a peperoni pizza
# I'm eating A lobster pizza. and A peperoni pizza..
# Cleaning after my mess of peperoni!
# Cleaning after my mess of lobster!
```
<!-- .element: class="fragment" -->

#HSLIDE
### func(\*args, \*\*kwargs):
#VSLIDE
```python
def func(arg):
    print(arg)

func("My Str")
    # My Str
func(arg="My Str")
    # My Str
```
```python
def func(arg="Default str"):
    print(arg)

func()
    # Default str
func(arg="Custom str")
    # Custom str
```
<!-- .element: class="fragment" -->
#VSLIDE
```python
def func(arg1, arg2="Default str"):
    print("arg1 -> "+arg1)
    print("arg2 -> "+arg2)

func("My str")
# arg1 -> My str
# arg2 -> Default str

func("My str",arg2="My other str")
# arg1 -> My str
# arg2 -> My other str
```
#VSLIDE
```python
def func(*args, **kwargs):
    print("args -> "+str(args))
    print("kwargs -> "+str(kwargs))

func(1, "Hola",color="azul", cant=28)
# args -> (1, 'Hola')
# kwargs -> {'color': 'azul', 'cant': 28}
```
```python
def my_pet(*nicknames, **attributes):
    print("My pet's nicknames")
    for name in nicknames:
        print(" - " + name) 

    print("\nMy pet's attributes")
    for attr in attributes:
        print(" - "+attr+": "+ str(attributes[attr])) 

my_pet('Firulais', 'Ruffus', age=3, loving=True) 
# My pet's nicknames
#  - Firulais
#  - Ruffus
#
# My pet's attributes
#  - age: 3
#  - loving: True
```
<!-- .element: class="fragment" -->
#HSLIDE
### (named\_tuple,)
#VSLIDE
```python
import csv

with open('my_file.csv') as csvfile:
    rows = csv.reader(csvfile)
    
    for row in rows:
        print(row[1],row[-3])
```

```python
from collections import namedtuple

with open('my_file.csv') as csvfile:
    rows = csv.reader(csvfile)

    House = namedtuple('House', rows[0])
    for row in rows:
        house = House._make(row) 
        print(house.city, house.price)
```
<!-- .element: class="fragment" -->
#VSLIDE
```python
rows = (
    ('Jose', 2, False),
    ('Pedro', 10, True),
    ('Marcos', 1, False),
    ('Nabucodonosor', 23, True),
    ('Ivan', 0, False),
)
```
```python
for person in rows:
    if person[1]>5 and person[2]==False:
        print('We got one!!!')
        break
else:
    print('No Luck :(')
```
<!-- .element: class="fragment" -->
#VSLIDE
```python
from collections import namedtuple

Person = namedtuple('Person', ['name', 'cats_amount', 'single'])
people = [Person._make(row) for row in rows] 

for person in people:
    if person.cats_amount >5 and person.single==False:
        print('We got one!!!')
        break
else:
    print('No Luck :(')
```

#HSLIDE
 - `>>> help()`
 - `[ comprehensions ]`
 - $$\lambda ambda  functions:$$
 - \_\_magic\_methods\_\_()
 - with... as... :
 - func(\*args, \*\*kargs):
 - (named\_tuple,)
