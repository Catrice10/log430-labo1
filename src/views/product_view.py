"""
Product view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from models.product import Product
from controllers.product_controller import ProductController

class ProductView:
    @staticmethod
    def show_options():
        """ Show menu for product operations """
        controller = ProductController()
        while True:
            print("\n1. Montrer la liste des produits\n2. Ajouter un produit\n3. Mettre à jour un produit\n4. Supprimer un produit\n5. Retourner au menu\n")
            choice = input("Choisissez une option: ")

            if choice == '1':
                products = controller.list_products()
                ProductView.show_products(products)
            elif choice == '2':
                name, brand, price = ProductView.get_inputs()
                product = Product(None, name, brand, price)
                controller.create_product(product)
            elif choice == '3':
                products = controller.list_products()
                ProductView.show_products(products)
                product_id = input("ID complet du produit à modifier : ")
                name, brand, price = ProductView.get_inputs()
                product = Product(product_id, name, brand, price)
                controller.update_product(product)
            elif choice == '4':
                product_id = input("ID complet du produit à supprimer : ")
                controller.delete_product(product_id)
            elif choice == '5':
                controller.shutdown()
                break
            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_products(products):
        """ List products """
        print("\n--- Liste des produits ---")
        if not products:
            print("Aucun produit trouvé.")
        else:
            print("\n".join(f"{p.id}: {p.name} - {p.brand} ({p.price}$)" for p in products))

    @staticmethod
    def get_inputs():
        """ Prompt for product inputs """
        name = input("Nom du produit : ").strip()
        brand = input("Marque du produit : ").strip()
        price = input("Prix du produit : ").strip()
        return name, brand, price