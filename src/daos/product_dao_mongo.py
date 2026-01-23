"""
Product DAO (Data Access Object) - MongoDB Version
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import os
from dotenv import load_dotenv
import pymongo
from bson import ObjectId
from models.product import Product

class ProductDAOMango:
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
            self.collection = self.db["products"]
        except FileNotFoundError:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur de connexion MongoDB : " + str(e))

    def select_all(self):
        """ Select all products from MongoDB """
        cursor = self.collection.find({})
        product_list = []
        for doc in cursor:
            product = Product(
                product_id=str(doc["_id"]), 
                name=doc.get("name"), 
                brand=doc.get("brand"),
                price=doc.get("price")
            )
            product_list.append(product)
        return product_list

    def insert(self, product):
        """ Insert given product into MongoDB """
        new_product = {
            "name": product.name, 
            "brand": product.brand, 
            "price": product.price
        }
        result = self.collection.insert_one(new_product)
        return str(result.inserted_id)

    def update(self, product):
        """ Update given product in MongoDB """
        updated_data = {
            "name": product.name, 
            "brand": product.brand, 
            "price": product.price
        }
        result = self.collection.update_one(
            {"_id": ObjectId(product.id)},
            {"$set": updated_data}
        )
        return result.modified_count

    def delete(self, product_id):
        """ Delete product from MongoDB with given product ID string """
        result = self.collection.delete_one({"_id": ObjectId(product_id)})
        return result.deleted_count

    def delete_all(self):
        """ Empty products collection in MongoDB """
        result = self.collection.delete_many({})
        return result.deleted_count
        
    def close(self):
        """ Properly close the MongoDB client """
        if hasattr(self, 'client'):
            self.client.close()