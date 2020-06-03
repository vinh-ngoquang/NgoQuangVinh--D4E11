import pymysql
import pymongo

mongo_client = pymongo.MongoClient()

db = mongo_client.get_database('Restaurant')

collection = db.get_collection('film')




client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'matbonchuc',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = client.cursor()
# cursor.execute('create database film')

# cursor.execute('''
# create table film.movies(
#     id int(11) auto_increment primary key,
#     title varchar(255),
#     writer varchar(255),
#     year int(11)
# )
# ''')

# cursor.execute('''
# create table film.actors(
#     name varchar(255)
# )
# ''')

# cursor.execute('''
# create table film.movie_actors(
# id int(11),
# name varchar(255),
# PRIMARY KEY (id,name)
# )
# ''')

movies =  collection.find()
for movie in movies:
    # cursor.execute(f'''
    # insert into film.movies
    # (title, writer, year)
    # VALUES (, 'dasfs', '1998')
    # ''')
    print(movie['title'])