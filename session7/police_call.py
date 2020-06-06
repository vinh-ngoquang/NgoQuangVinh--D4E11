import pymysql
from pymongo import MongoClient

mongo_client = MongoClient()
mongo_db = mongo_client.get_database('mysql_ex')
call_collection = mongo_db.get_collection('pollice_call')


mysql_client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'matbonchuc',
    cursorclass = pymysql.cursors.DictCursor      
)

cursor = mysql_client.cursor()

cursor.execute('''
create table if not exists mysql_ex.police_call(
id varchar(255) primary key,
recordid varchar(255),
calldatetime varchar(255),
callnumber varchar(255),
priority varchar(255),
district varchar(255),
description varchar(255),
incidentlocation varchar(255),
zipcode varchar(255),
neighborhood varchar(255),
policedistrict varchar(255),
policepost varchar(255),
councildistrict varchar(255),
sheriffdistricts varchar(255),
community_statistical_areas varchar(255),
census_tracts varchar(255)
)
''')

for call in call_collection.find():
    cursor.execute(f'''
    insert into mysql_ex.police_call(id,recordid,calldatetime,callnumber,priority,district,description,incidentlocation,zipcode,neighborhood,policedistrict,policepost,councildistrict,sheriffdistricts,community_statistical_areas,census_tracts)
    values("{call["_id"]}","{call["recordid"]}", "{call["calldatetime"]}","{call["callnumber"]}", "{call["priority"]}","{call["district"]}","{call["description"]}",
    "{call["incidentlocation"]}","{call["zipcode"]}","{call["neighborhood"]}","{call["policedistrict"]}","{call["policepost"]}","{call["councildistrict"]}","{call["sheriffdistricts"]}","{call["community_statistical_areas"]}","{call["census_tracts"]}")
    ''')
    







mysql_client.commit()