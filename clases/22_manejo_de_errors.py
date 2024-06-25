""" Capturando Errors del sistema"""
try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

try:
    assert 1 != 1, 'Uno no es igual que uno' # assert porse un sistema de eviar avisos
except AssertionError as error:
    print(error)

""" Capturando Excepciones propias"""
try:
    age = 10
    if age < 18:
        raise Exception('No se permite menores de edad')
except Exception as error:
    print(error)

print('hola') # metodo de pruba para verificar hasta donde corre el codigo