"""agregando condicionales"""
import random
countries = ['col', 'mex', 'bol', 'pe']

poblacion = {ciudad: random.randint(1, 100) for ciudad in countries}
print(poblacion)

ressult = {country: population for (country,population) in poblacion.items() if population > 40}
print(ressult)

""" Ejemplo 2 """

text = 'hola , soy Manuel' 
unique = { c:c.upper() for c in text if c in 'aeiou' }
print(unique)