## Con map transformamos todos los elementos de cualquier grupo y creamos uno nuevo

""" forma de transformar una lista de manera convencional"""

numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i * 2)

print(numbers)
print(numbers_v2)

""" implementando * map() * y el uso de funciones lambda """
        
#          MAP( FUNC  , ITER )
#  """ FUNC :  es una funcion """     
#  """ ITER :  es un iterable """     

numbers_v3 = map(lambda i : i * 2 , numbers)          # esto regresa un map osea un iterable..

numbers_v3 = list(map(lambda i : i * 2 , numbers))    # convertimos en lista
print(numbers_v3)


""" utilizamos map() para interactuar con 2 listas"""

numbers_2 = [5, 6, 7]

result = list(map(lambda x, y : x + y, numbers, numbers_2)) 
print(result)
 
# """ suma cada uno de los elementos de cada lista y los convierte en una nueva lista """
# """ esta nueva lista tomara la cantida menor de elemento """

# imprime = [6, 8, 10]