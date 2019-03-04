import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students
'''
插入数据
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}
result = collection.insert_many([student1, student2])
查询
result = collection.find_one({'name': 'Mike'})

result = collection.fine_one({'_id': ObjectId('5c4dd2ec00eee94a5cfab709')})

results = collection.find({'age': {'$gt': 20}}) # 大于20(比较符号)

results = collection.find({'name': {'$regex': '^M.*'}}) # 以M开头（正则表达式）
计数
count = collection.find({'age': 20}).count()
排序
results = collection.find().sort('name', pymongo.ASCENDING)
偏移
results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
更新
condition = {'name': 'Jordan'}
student = collection.fine_one(condition)
student['age'] = 25
result = collection.update_one(condition, {'$set': student})

condition = {'age': {'$gt': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
删除
result = collection.remove({'name': 'Jordan'})

result = collection.delete_one({'name': 'Jordan'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age': {'$lt': 25}})
'''
print(result.deleted_count)
