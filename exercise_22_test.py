from exercise_22 import ProductsService

products = ProductsService.get_products()

for product in products: 
    print("ID: " + str(product.id))
    print("Description: " + product.description)
    print("Price: " + str(product.price))
    print()

id = int(input("Enter a product ID: "))
product = ProductsService.find(id)

if product != None:
    print("Description: " + product.description)
    print("Price: " + str(product.price))
else:
    print("That product doesn't exist.")
