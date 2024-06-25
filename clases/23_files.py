file = open('./clases/text.txt')
""" TODO ARCHIVO DEBE CERRARSE DEPUES DE ABRIRLO YA QUE OCUPARIA MUCHO ESPACIO EN MEMORIA"""
#print(file.read())                 -------- LEER TODO EL ARCHIO, 

# print(file.readline())
# print(file.readline())
# print(file.readline())            -------- ACA LEEMOS EL ARCHIVO LINEA POR LINEA
# print(file.readline())

# for line in file:                 -------- LEE EL ARCHIVO LINEA A LINE 
#     print(line)

# file.close()                      # -------- CIERRRA EL ARCHIVO

with open('./clases/text.txt') as file:     #   LEEMEOS EL ARCHIVO LIENA A LINEA  
    for line in file:                       #   Y A LO QUE ESTE TERMINE SE CERRAR
        print(line)                         #   SOLO AUTOMATICAMENTE