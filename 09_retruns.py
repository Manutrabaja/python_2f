def find_volume(length = 1, width = 1, depth = 1):
    return length * width * depth , width , 'Esto es todo'

result = find_volume(10, 20, 3) #------------------------------ devuelve la tupla 
print(result)    # (600, 20, 'Esto es todo')

resulta = list(find_volume(10, 20, 3)) #------------ ---------- devuelve una lista en vez de una tupla!!
print(resulta)   # [600, 20, 'Esto es todo']

resultado, width, text = find_volume(3 , width = 4) 
print(resultado)         # 12
print(width)             # 4
print(text)              # Esto es todo 