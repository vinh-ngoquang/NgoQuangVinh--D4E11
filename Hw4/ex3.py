inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger','bedroll','bread loaf']
} 

inventory['pocket'] = ['seashell', 'strange berry', 'lint']           #1 + 2

pack = inventory['backpack']

# pack.remove('dagger')
# print(inventory)                     #3


inventory.pop('gold')
inventory['gold'] = 500, 50            #4


print(inventory)
