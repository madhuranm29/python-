#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv
from collections import defaultdict

def load_products():
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        products = list(reader)
    return products

def save_products(products):
    with open('products.csv', 'w', newline='') as file:
        fieldnames = products[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

def display_categories(products):
    categories = set(product['Category'] for product in products)
    print("\nAvailable Categories:")
    for category in categories:
        print(category)

def display_products(products, category=None):
    print("\nAvailable Products:")
    for product in products:
        if category is None or product['Category'] == category:
            print(f"{product['ID']}. {product['Name']} - ${product['Price']} - Quantity: {product['Quantity']}")

def add_product_to_cart(products, cart, product_id, quantity):
    for product in products:
        if product['ID'] == product_id:
            if int(product['Quantity']) < quantity:
                print("Insufficient quantity available. Try a lower quantity.")
                return
            product_in_cart = dict(product)
            product_in_cart['Quantity'] = quantity
            cart.append(product_in_cart)
            product['Quantity'] = int(product['Quantity']) - quantity
            print(f"{quantity} {product['Name']} added to the cart.")
            return
    print("Invalid product ID. Try again.")

def add_product(products, name, price, category, quantity):
    product_id = str(len(products) + 1)
    new_product = {'ID': product_id, 'Name': name, 'Price': price, 'Category': category, 'Quantity': quantity}
    products.append(new_product)
    print(f"{name} added successfully.")

def remove_product(products, product_id):
    for product in products:
        if product['ID'] == product_id:
            products.remove(product)
            print(f"Product with ID {product_id} removed successfully.")
            return
    print("Invalid product ID. Try again.")

def customer_mode(products):
    cart = []
    categories = set(product['Category'] for product in products)

    while True:
        display_categories(products)
        category = input("Enter the category to view products (0 to checkout): ")
        if category == '0':
            break
        if category not in categories:
            print("Invalid category. Try again.")
            continue
        display_products(products, category)
        choice = input("Enter the product ID to add to cart (0 to change category): ")
        if choice == '0':
            continue
        quantity = int(input("Enter the quantity: "))
        add_product_to_cart(products, cart, choice, quantity)

    print("\nItems in Cart:")
    display_products(cart)
    total = sum(float(item['Price']) * item['Quantity'] for item in cart)
    print(f"\nTotal: ${total}")

    print("\nRemaining Products:")
    display_products(products)

def owner_mode(products):
    while True:
        print("\nOwner Mode:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Display Products")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter product name: ")
            price = input("Enter product price: ")
            category = input("Enter product category: ")
            quantity = int(input("Enter product quantity: "))
            add_product(products, name, price, category, quantity)
        elif choice == '2':
            display_products(products)
            product_id = input("Enter the product ID to remove: ")
            remove_product(products, product_id)
        elif choice == '3':
            display_products(products)
        elif choice == '4':
            save_products(products)
            break
        else:
            print("Invalid choice. Try again.")

def main():
    products = load_products()

    while True:
        print("\nSupermarket System:")
        print("1. Customer Mode")
        print("2. Owner Mode")
        print("3. Exit")
        mode_choice = input("Enter your mode choice: ")

        if mode_choice == '1':
            customer_mode(products)
        elif mode_choice == '2':
            owner_mode(products)
        elif mode_choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

