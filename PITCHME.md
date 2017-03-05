#HSLIDE
## Not so advanced python
### (for real)

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
```
cities = []
for user in users:
    cities.append(user.city)
```
```python
# cities -> ['Santiago', 'San Juan', 'SANTIAGO', 'santiago']
```
#VSLIDE
#### Lists Comprehensions
```python
cities = [user.city for user in users]
```
```python
# cities -> ['Santiago', 'San Juan', 'SANTIAGO', 'santiago']
```
#VSLIDE
#### Sets
```python
cities = {user.city.lower() for user in users}
```
```python
# cities -> {'santiago', 'san juan'}
```
#VSLIDE
#### Dictionaries
```python
cities = {user.name: user.city for user in users}
```
```python
# cities -> {
#    'Nabucodonosor': 'santiago',
#    'Pedro': 'San Juan',
#    'Marcos': 'SANTIAGO',
#    'Juan': 'Santiago'
#    }
```
#HSLIDE
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

