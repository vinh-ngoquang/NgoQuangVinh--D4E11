from pymongo import MongoClient

client = MongoClient()

db = client.get_database('Movie')

collection = db.get_collection('Films')

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

# collection.insert_many(data)

# movies = collection.find()
# for movie in movies:            #1.1
#     print(movie)


# writers = collection.find({'writer':'Chuck Palahniuk'})
# for writer in writers:                     #1.2
#     print(writer)


# actors = collection.find({'actors':'Brad Pitt'})
# for actor in actors:                          #1.3
#     print(actor)


# franchises = collection.find({'franchise':'The Hobbit'})
# for franchise in franchises:                    #1.4
#     print(franchise)


# years = collection.find({'$and':[{'year':{'$gte': 1990}}, {'year':{'$lte':1999}}]})
# for year in years:                            #1.5
#     print(year)


# years = collection.find({'$or':[{'year':{'$gt': 2000}}, {'year':{'$lt':2010}}]})
# for year in years:                            #1.6
#     print(year)


# query = {'title':'The Hobbit: An Unexpected Journey'}
# update = {'$set':{'synopsis':"A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug."}}
# collection.update_many(query,update)                 #2.1


# query = {'title':'The Hobbit: The Desolation of Smaug'}
# update = {'$set':{'synopsis': "The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring."}}
# collection.update_many(query,update)             #2.2

# query = {'title' : 'Pulp Fiction'}
# update = {'$push':{'actors':'Samuel L. Jackson'}}      #2.3
# collection.update_one(query,update)


# query = {'title':'Pee Wee Hermans Big Adventure'}
# collection.delete_one(query)                #3.1


# query = {'title':'Avatar'}
# collection.delete_one(query)

movie_found = collection.find({
    'synopsis':{'$regex': '.*Bilbo.*'}
    })
for movie in movie_found:
    print(movie)