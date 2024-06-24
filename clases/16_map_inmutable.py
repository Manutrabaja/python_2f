items = [
    {   'product' : 'camisa',
        'price': 100    },

    {   'product' : 'pantalones',
        'price' : 300    },
    
    {   'product' : 'zapatos',
        'price' : 200
    }
]

# prices = list(map(lambda element: element['price'], items))
# print(prices)
 
def add_taxes(itrs):
    new_item = itrs.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_items = list(map(add_taxes, items))
print(F'nueva lista',new_items)
print(F'antigua lista',items)
