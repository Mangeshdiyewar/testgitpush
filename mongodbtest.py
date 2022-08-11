import pymongo



client = pymongo.MongoClient("mongodb+srv://agerabeast:Mangesh1@mangesh.tycxduh.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {   'name':'mangesh',
     'email' : 'mangeshmjd@gmail.com',
      'surname': 'diyewar'
}

db1 = client['mongodbtest']
coll = db1['test']
coll.insert_one(d)

