import pymysql
# from pymongo import MongoClient

# mongo_client = MongoClient()
# mongo_db = mongo_client.get_database('mysql_ex')
# call_collection = mongo_db.get_collection('restaurants')


mysql_client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'matbonchuc',
    cursorclass = pymysql.cursors.DictCursor      
)

cursor = mysql_client.cursor()
cursor.execute('''
create table if not exists mysql_ex.restaurant(
id varchar(255) primary key,
building varchar(255),
zipcode varchar(255),
borough varchar(255),
cuisine varchar(255)
)
''')