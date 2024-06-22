import functools

numbers = [4, 5, 6, 7]

result = functools.reduce(lambda counter , item : counter + item, numbers)
print(result)

""" Veremos el paso a paso de esta func"""

def acumm(contador , sumador):
    print(f'contador es => ',contador)
    print(f'sumador es => ', sumador)
    return contador + sumador

resultado = functools.reduce(acumm, numbers)
print(resultado)