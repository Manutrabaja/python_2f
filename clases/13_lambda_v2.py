def incremet(x):
    return x + 1

def high_ord_func(x, func):
    return x + func(x)

result = high_ord_func(2, incremet)
print(result)                                       # aca se ejecuta  2 + (2 + 1) = 5

""" implementando el uso de funciones lambda"""

incremet_2 = lambda x : x + 1

high_ord_func_2 = lambda x , func2 : x + func2(x)

result_2 = high_ord_func_2(2, incremet_2)
print(result_2)                                    # 5    


""" utilizando lambda de forma dinamica"""

result_3 = high_ord_func_2(2, lambda x : x + 2)         # aplicamos la lambda directamente en los argumentos
print(result_3)

result_4 = high_ord_func_2(2, lambda x : x * 5)
print(result_4)