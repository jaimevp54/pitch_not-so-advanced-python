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
# cities => ['Santiago', 'San Juan', 'SANTIAGO', 'santiago']
```
#VSLIDE
<span class="fragment"> 
```python
cities = [user.city for user in users]
# cities => ['Santiago', 'San Juan', 'SANTIAGO', 'santiago']
```
<span/>

<span class="fragment"> 
```python
cities = {user.city.lower() for user in users}
# cities = {'santiago', 'san juan'}
``` 
<span/>

<span class="fragment"> 
cities = {user.name: user.city for user in users}
# cities = {'Nabucodonosor': 'santiago', 'Pedro': 'San Juan', 'Marcos': 'SANTIAGO', 'Juan': 'Santiago'}
<span/> 

#HSLIDE
## lambda

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

