import pymysql


client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'matbonchuc',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = client.cursor()
# cursor.execute('CREATE DATABASE D4E11 ')

# cursor.execute('''
# CREATE TABLE D4E11.USER(
# id INT(11) AUTO_INCREMENT PRIMARY KEY, 
# username VARCHAR(255),
# age INT(11)
#  )''')

# cursor.execute('''
# INSERT INTO D4E11.USER
# (username,age)
# VALUES ('dat','96'),('tada','98')
# ''')


# cursor.execute(''' select * from D4E11.USER ''')
# data = cursor.fetchone()
# print(data)

# cursor.execute('''
# # UPDATE  D4E11.USER SET age = 1 WHERE age = 98
# ''')

# cursor.execute('''
# DELETE FROM D4E11.USER WHERE age = 1
# ''')
# client.commit()

# cursor.execute('''
# CREATE TABLE D4E11.centre(
#     id varchar(255) UNIQUE PRIMARY KEY,
#     name VARCHAR(255) UNIQUE
# )
# ''')

# cursor.execute('''
# CREATE TABLE D4E11.saleman(
#     username varchar(255) PRIMARY KEY,
#     center_id varchar(255) references D4E11.centre(id),
#     email varchar(255),
#     name varchar(255)
# )
# ''')

# cursor.execute('''
# INSERT INTO D4E11.centre(id, name)
# VALUES ('MINDX 1' , 'mindx thanh cong'),('MINDX2', 'mindx nct')
# ''')

centre_name = 'mindx thanh cong'
cursor.execute(f''' select id from D4E11.centre where name = '{centre_name}' ''')

centre_found = cursor.fetchone()
print(centre_found)

cursor.execute(f'''
insert into D4E11.saleman(username, center_id, email, name)
VALUES ('best saleman','{centre_found['id']}', 'email.com', 'nguoi ban hang' )
''')


client.commit()
