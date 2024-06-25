# """diferentes forma de importar"""

"""completao simple"""  

# esta esta comentada ya que es el mismo archivo y generaria error

# import my_functions

# def get_total(orders):

#   totales = my_functions.get_totals(orders)
#   sumatoria = my_functions.calc_total(totales)
#   return sumatoria

"""especifica o parcial"""

from my_functions import get_totals, calc_total

def get_total(orders):

  totales = get_totals(orders)
  sumatoria = calc_total(totales)
  return sumatoria

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)