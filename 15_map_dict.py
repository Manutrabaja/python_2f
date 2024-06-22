items = [
    {   'product' : 'camisa',
        'price': 100    },

    {   'product' : 'pantalones',
        'price' : 300    },
    
    {   'product' : 'zapatos',
        'price' : 200
    }
]

prices = list(map(lambda element: element['price'], items))
print(prices)
 
def add_taxes(itrs):
    itrs['taxes'] = itrs['price'] * .19
    return itrs

#  otra forma de hacerlo
# new_items = list(map( lambda x: x|{'tax': x['price']*0.19} ,items))

new_items = list(map(add_taxes, items))
print(new_items)