""" funcio basica """

def increment(x):           # funcion basica definada
    return x + 1

result = increment(10)
print(result)               # imprime 11


""" implementando el uso de funciones lambda"""

incremento = lambda x : x + 1

resultado = incremento(20)
print(resultado)

"""Segundo ejemplo de lambda"""

"""En este segundo caso podriamos agregar un 
input asi hacerlo con los datos introduciodos""" # !__ NOTA __!    

full_name = lambda name, last_name : f'full name is {name.title()} {last_name.title()}'

text = full_name('hannah carolina', 'espina concho')
print(text)

# esto imprimiria el nombre completo con las primeras letras en mayuscula
