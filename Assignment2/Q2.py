dict = {}

while True:
    product = input("Enter the product (Enter 'done' if finished): ").strip()
    if product.lower() == 'done':
        break
    else:
        price = int(input("Enter the price of the product: "))
        dict[product] = price

print("\n")

while True:
    name = input("Enter a product name (Enter 'done' if finished): ").strip()
    if name.lower() == 'done':
        break
    if name in dict:
        print(f"The price of {name} is {dict[name]}")
    else:
        print("Invalid product")
