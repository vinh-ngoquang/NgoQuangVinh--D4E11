person = ['Dat', 96, 'Viettel', 1, False, True]


#dictionary, object, map...

person = {                                             #in
    'name': 'Dat', 
    'yob': {
        'year': 1996,
        'month': 1,
        'day': 1
    }, 
    'company': ['Viettel', 'Vinaphone'],
    'key': None
    }
#{key: value, key: value, ...}
name = person['name']
# print(person['yob']['year'])
# print(person['company'])
person['relationship'] = True                           #create
person['yob']['month'] = 4                              #update
del person['key']                                       #delete
for key in person:
    print(key, person[key])                             #read