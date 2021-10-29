from exercise_21 import Product

 # Create an instance
pro1 = Product(101, "Coke", 25.00)
pro2 = Product(208, "Lays Chips", 105.00)
pro3 = Product(560, "Mott's Apple Juice", 200.00)

products = [pro1, pro2, pro3]

for product in products: 
    print("ID: " + str(product.id))
    print("Description: " + product.description)
    print("Price: " + str(product.price))
    print()