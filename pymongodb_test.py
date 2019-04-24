import pymongo
import os
import sys
import pprint
import dns

def main():
    url = 'mongodb+srv://{}:{}@{}/{}'.format(
        os.environ["MONGO_USERNAME"],
        os.environ["MONGO_PASSWORD"],
        os.environ["MONGO_HOST"],
        os.environ["MONGO_DBNAME"]
    )
        #mongodb+srv://Objective:<password>@cluster0-emrl4.mongodb.net/test?retryWrites=true
    client = pymongo.MongoClient(url)
    db = client[os.environ["MONGO_DBNAME"]]
    collection = db['Finances'] #put the name of your collection in the quotes

    #1. print the number of documents in collection
    print(collection.count_documents({}))
    #2. print the first document in the collection
    print(collection.find_one({}))
    #3. print all documents in the collection
    for InfoWars in collection.find({}):
        print(InfoWars)
    #4. print all documents with a particular value for some attribute
    #ex. print all documents with the birth date 12/1/1990


if __name__=="__main__":
    main()
