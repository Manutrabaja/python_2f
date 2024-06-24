numbers = [1, 2, 3, 4, 5]
new_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print(f'lista de numeros pares',new_numbers)
print(f'lista original',numbers)