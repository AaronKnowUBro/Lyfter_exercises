class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for p in self.products:
            print(f"{p.name} - Precio: {p.price}, Cantidad: {p.quantity}, Valor total: {p.total_value()}")

    def calculate_total_value_of_inventory(self):
        return sum(p.total_value() for p in self.products)


inventory = Inventory()

while True:
    name = input("Ingrese el nombre del producto: ")
    price = float(input("Ingrese el precio del producto: "))
    quantity = int(input("Ingrese la cantidad del producto: "))

    product = Product(name, price, quantity)
    inventory.add_product(product)

    continuar = input("¿Desea agregar otro producto? (s/n): ").lower()
    if continuar != "s":
        break

print("\n--- Productos en inventario ---")
inventory.show_products()
print("Valor total del inventario:", inventory.calculate_total_value_of_inventory())