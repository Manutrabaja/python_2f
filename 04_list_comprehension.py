    # esta es la forma que se haria normalmente

numbres = []
for element in range(1,11):
    numbres.append(element)
print(numbres)

    # esta es aplicando el concepto de list comprehension

numeros = [elements for elements in range(1,11)]
print(numeros)

#------------------------------------ si queremos que el (element * 2)

    # esta es la forma coridiana
numbres = []
for element in range(1,11):
    numbres.append(element * 2)

print(numbres)

    # plicando list comprehension 

numeros = [elements * 2 for elements in range(1,11)]
print(numeros)

#---------------------------------------- agregamos condicion

list_numbers = []
for i in range(1,11):
    if i % 2 == 0:
        list_numbers.append(i * 2)
print(list_numbers)

# con list comprehension

lista_numeros = [i * 2 for i in range(1,11) if i % 2 == 0]
print(lista_numeros)


