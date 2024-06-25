""" LEER Y ESCRIBIR ARCHIVO .TXT """

# with open('./clases/text.txt', 'r') as file:     #ACA LEEMOS EL ARCHIVO CON O SIN LA    'r'
#     for line in file:                       
#         print(line)  
     

""" tenemos permiso de escritura pero se borra todo lo demas y nos queda un archivo en blanco"""
# with open('./clases/text.txt', 'w') as file:     #aca se escribe en el archivo    'w' 
#     for line in file:                       
#         file.write('esta sera la nueva lina del texto')
        

with open('./clases/text.txt', 'w+') as file:     # TENEMOS PERMISOS DE LECTURA Y ESCRITURA 
    for line in file:                       
        print(line)
    file.write('esta sera la nueva lina del texto\n')
    file.write('otro linea\n')
    file.write('otra mas\n')