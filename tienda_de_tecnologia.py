"""tienda de tecnologia es un pequeño diccionario que devuelve un valor segun el articulo que deses """
# por terminar..

def message_creator(text):
   # Escribe tu solución 👇
   mensaje = {
      'computadora' : "Con mi computadora puedo programar usando Python",
      'celular' : "En mi celular puedo aprender usando la app de Platzi",
      'cable' : "¡Hay un cable en mi bota!",
      'invalido' : "Artículo no encontrado"
      }
   if text in mensaje.keys():
      return mensaje[text]
   else:
      return mensaje['invalido']

text = input('Que articulo deseas tenemos computadora, celular y cable: ')
response = message_creator(text)
print(response)