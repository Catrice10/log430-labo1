"""
User controller
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from daos.product_dao_mongo import ProductDAOMango

class ProductController:
    def __init__(self):
        self.dao = ProductDAOMango()

    def list_products(self):
        """ List all users """
        return self.dao.select_all()
        
    def create_product(self, user):
        """ Create a new user based on user inputs """
        self.dao.insert(user)

    def update_product(self, user):
        """ Update existing user based on user inputs """
        self.dao.update(user)
    
    def delete_product(self, user_id):
        """ Create a new user based on user inputs """
        self.dao.delete(user_id)

    def shutdown(self):
        """ Close database connection """
        self.dao.close()
