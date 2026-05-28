product_price = int(input("ingrese el precio del producto "))

if product_price >= 100:
    float_discount = 0.90
    final_price = product_price * float_discount
else:
    float_discount = 0.98
    final_price = product_price * float_discount

print(f"El precio final es de: {final_price}")

