from pymongo import MongoClient

client = MongoClient()

db = client.get_database('d4e11')  #taodatabase

collection = db.get_collection('members')

# collection.insert_one({      #create
#     'name': 'Dat',
#     'age': 24,
#     'gender': True
# })

collection.insert_many([
    {      
    'name': 'Dat',
    'age': 24,
    'gender': True
    },{      
    'name': 'Dat2',
    'age': 24,
    'gender': True
    },{      
    'name': 'Dat3',
    'age': 24,
    'gender': True
    },{      
    'name': 'Dat4',
    'age': 24,
    'gender': True
    }
])

members = collection.find()
for members in members:
    print(members)