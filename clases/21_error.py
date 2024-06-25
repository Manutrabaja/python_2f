"""  LOS ERRORES SERAN COMENTADOS PARA QUE EL CODIGO PUEDA CORRER 
     ESO NO ES UNA BUENA PRACTICA, SOLO QUE ACA SE HACE POR SER EJEMPLOS""" 

# print(0/ 0) divicion entre cero -------- "ZeroDivisionError"

# print(result) result no esta defivinda ----- "NameError"

print('Hola')

suma = lambda x,y : x + y    # aca funcionaria bien y el codigo correra
assert suma(2,2) == 4

"""sum = lambda x,y : x + (y * 2)""" # esto podria ser un mini test de prueba, para que el resultado sea el esperado
"""assert suma(2,2) == 4"""          # ---"AssertionError"  el resultado no sera el correcto o el esperado

age = 10
if age < 18:
     raise Exception('No se permite menores de edad')
