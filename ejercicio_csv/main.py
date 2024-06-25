import csv

def read_csv(path):
   # Tu código aquí 👇
   with open(path,'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      element = list()
      for linea in reader:
         element.append(int(linea[1]))
      print(element)
      total= (sum(element))
      
   return total

response = read_csv('./data.csv')
print(response)