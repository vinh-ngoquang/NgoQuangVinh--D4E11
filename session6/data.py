from pymongo import MongoClient

client = MongoClient()

db = client.get_database('Movie')

collection = db.get_collection('films')


data = [
{
'title' : 'Fight Club',
'writer' : 'Chuck Palahniuk',
'year' : 1999,
'actors' : [
'Brad Pitt',
'Edward Norton',
]
},
{
'title' : 'Pulp Fiction',
'writer' : 'Quentin Tarantino',
'year' : 1994,
'actors' : [
'Brad Pitt',
'Edward Norton',
]
},
{
'title' : 'Inglorious Basterds',
'writer' : 'Chuck Palahniuk',
'year' : 1999,
'actors' : [
'Brad Pitt',
'Edward Norton',
]
},
{
'title' : 'The Hobbit: An Unexpected Journey',
'writer' : 'Chuck Palahniuk',
'year' : 1999,
'actors' : [
'Brad Pitt',
'Edward Norton',
],
'franchise' : 'The Hobbit'
},
{
'title' : 'The Hobbit: The Desolation of Smaug',
'writer' : 'Chuck Palahniuk',
'year' : 1999,
'actors' : [
'Brad Pitt',
'Edward Norton',
],
'franchise' : 'The Hobbit',
},
{
'title' : 'The Hobbit: The Battle of the Five Armies',
'writer' : 'Chuck Palahniuk',
'year' : 1999,
'actors' : [
'Brad Pitt',
'Edward Norton',
],
'franchise' : 'The Hobbit'
},
{
'title' : "Pee Wee Hermans Big Adventure",
},
{
'title' : 'Avatar',
},
]
collection.insert_many(data)

######

# writer = collection.find({'writer':'Quentin Tarantino'})
# for i in writer:
#     print(i)

# franchises = collection.find({'franchise': 'The Hobbit'})
# for franchise in franchises:
#     print(franchise)

# results = collection.find({'$or':[{'year':{'$gt':2000}},{'year':{'$lte':2010}}]})
# for result in results:
#     print(result)

# query = {'title':'The Hobbit: An Unexpected Journey'}
# update = {'$set':{'title':' reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug.'}}

# collection.update_one(query,update)

# query2 = {'title': 'The Hobbit: The Desolation of Smaug'}
# update2 = {'$set':{'title':'The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring.'}}

# collection.update_one(query2,update2)

# query3 = {'title':'Pulp Fiction'}
# push = {'$push':{'actors':'Samuel L. Jackson'}}
# collection.update_many(query3,push)

########

# user = [
# {
# 'username' : 'GoodGuyGreg',
# 'first_name' : 'Good Guy',
# 'last_name' : 'Greg'
# },
# {
# 'username' : 'ScumbagSteve',
# 'full_name' : {
# 'first' : 'Scumbag',
# 'last' : 'Steve'}
# }
# ]

# # collection.insert_many(user)

# post = [
# {
# 'username' : 'GoodGuyGreg',
# 'title' : 'Passes out at party',
# 'body' : 'Wakes up early and cleans house',
# },
# {
# 'username' : 'GoodGuyGreg',
# 'title' : 'Steals your identity',
# 'body' : 'Raises your credit score'
# },
# {
# 'username' : 'GoodGuyGreg',
# 'title' : 'Reports a bug in your code',
# 'body' : 'Sends you a Pull Request'
# },
# {
# 'username' : 'ScumbagSteve',
# 'title' : 'Borrows something',
# 'body' : 'Sells it'
# },
# {
# 'username' : 'ScumbagSteve',
# 'title' : 'Borrows everything',
# 'body' : 'The end'
# },
# {
# 'username' : 'ScumbagSteve',
# 'title' : 'Forks your repo on github',
# 'body' : 'Sets to private
# }]
# collection.insert_many(post)