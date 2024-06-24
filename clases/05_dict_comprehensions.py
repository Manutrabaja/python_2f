""" crenado un dicionario donde i es la llave y (i*2) es el valor """
dict  = {}
for i in range(1, 5):
    dict[i] = i * 2

print(dict)
#----------------------------------------- dict comprehensions

dict_v2 = {i : i * 2 for i in range(1, 5)}
print(dict_v2)


""" diccionario de ciudades y su poblacion (el valor de la poblacion es random) """

import random
countries = ['col', 'mex', 'bol', 'pe']
populatoin = {}
for country in countries:
    populatoin[country] = random.randint(1, 100)

print(populatoin)

#-------------------------------------------------- dict comprehensions

poblacion = {ciudad: random.randint(50, 100) for ciudad in countries}
print(poblacion)


""" crenado un diccionario apartir de 2 listas"""

names = ['nico', 'suke', 'santi']
ages = [12, 36 , 60]

print(list(zip(names, ages)))

#-------------------------------------------------- dict comprehensions

new_dict = {name: age for (name, age) in zip(names,ages)}
print(new_dict)

