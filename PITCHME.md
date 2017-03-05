#HSLIDE
## Not so advanced python
## <span style="font-size:0.6em; color:gray">(for real)</span> 

#HSLIDE
`>>> help()`

#HSLIDE
`[ comprehensions ]`
#VSLIDE
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
$$\lambda ambda functions:$$
#VSLIDE

#HSLIDE
#VSLIDE


#HSLIDE
#VSLIDE

#HSLIDE
#VSLIDE

#HSLIDE
#VSLIDE

#HSLIDE

