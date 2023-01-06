# author:qiao_px
# @Time 2022/10/28  11:38
# @File ceshiMongo.py
import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.users
data = {
    "name":"qiaolijie",
    "age":"12"
}
collection.insert_one(data)
rusult = collection.find()
print(rusult)