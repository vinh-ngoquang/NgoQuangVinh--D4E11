prices = {'banana': 4,
'apple': 2,
'orange': 1.5,
'pear': 3}

stock = {'banana': 6,
'apple': 0,
'orange': 32,
'pear': 15}

for key in stock:
    # for key1 in stock:
    print(key)
    print('price:', prices[key] )
    print('stock:', stock[key])