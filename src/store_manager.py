"""
Store manager application
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from views.user_view import UserView
from views.product_view import ProductView

def main():
    while True:
        print("1. Accéder à la gestion des produits")
        print("2. Accéder à la gestion des utilisateurs")

        choice = input("\nQue souhaitez-vous faire ? ")

        if choice == '1':
            ProductView.show_options()
        elif choice == '2':
            UserView.show_options()
        else:
            print("Option invalide. Veuillez choisir 1, 2 ou 3.")

if __name__ == '__main__':
    main()