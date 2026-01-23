import os
from dotenv import load_dotenv
import pymongo
from bson import ObjectId
from models.user import User

class UserDAOMongo:
    def __init__(self):
        try:
            env_path = ".env"
            load_dotenv(dotenv_path=env_path)
            db_host = os.getenv("MONGODB_HOST")
            db_name = os.getenv("MONGODB_NAME")
            db_user = os.getenv("DB_USERNAME")
            db_pass = os.getenv("DB_PASSWORD")    
            self.client = pymongo.MongoClient(f"mongodb://{db_user}:{db_pass}@{db_host}/")   
            self.db = self.client[db_name]
            self.collection = self.db["users"]
        except FileNotFoundError as e:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur : " + str(e))
    
    def select_all(self):
        """ Select all users from MySQL """
        cursor = self.collection.find({})
        user_list = []
        for x in cursor:
            user = User(user_id=str(x["_id"]), name=(x["name"]), email=(x["email"]))
            user_list.append(user)
        return user_list

    def insert(self, user):
        """ Insert given user into MySQL """
        new_user = {"name" : user.name, "email" : user.email}
        result = self.collection.insert_one(new_user)
        return str(result.inserted_id)

    def update(self, user):
        """ Update given user in MySQL """
        updated_user = {"name" : user.name, "email" : user.email}
        result = self.collection.update_one({"_id" : ObjectId(user.id)}, {"$set": updated_user})
        return (result.modified_count)

    def delete(self, user_id):
        """ Delete user from MySQL with given user ID """
        result = self.collection.delete_one({"_id" : ObjectId(user_id)})
        return (result.deleted_count)

    def delete_all(self): #optional
        """ Empty users table in MySQL """

        pass
        
    def close(self):
            """ Properly close the MongoDB client """
            if hasattr(self, 'client'):
                self.client.close()