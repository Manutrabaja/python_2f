price = 100                             #-------------- ALCANCE GLOBAL 

def increment():                        #-------------- ALCANCE LOCAL
    price = 200      
    price = price + 10    

    print(price)              # imprime 210
    return price

print(price)                  # imprime 100

price_2 = increment()                   #-------------- Asignandole un otro nombre a la variable local 
print(price_2)                          #-------------- imprimiendo la el resultado de la funcion increment (210)