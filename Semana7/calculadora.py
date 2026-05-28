def show_menu(current_number):
    print("\n--- Calculator ---")
    print(f"Número actual: {current_number}")
    print("Seleccione una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Borrar resultado")
    print("6. Salir")


def option_input():
    option = input("Ingrese su opción: ")
    return option


def number_input():
    number = input("Ingrese un número: ")
    try:
        return float(number)
    except ValueError:
        print("Número inválido, por favor intente de nuevo.")
        return None


def operation(option, actual, new):
    if option == "1":
        return actual + new
    elif option == "2":
        return actual - new
    elif option == "3":
        return actual * new
    elif option == "4":
        if new == 0:
            print("No se puede dividir entre cero.")
            return None
        return actual / new


def main():
    current_number = 0.0

    while True:
        show_menu(current_number)
        option = option_input()   # <-- AQUÍ sí llamamos a la función

        if option not in ["1", "2", "3", "4", "5", "6"]:
            print("Opción inválida.")
            continue

        if option == "6":
            print("Cerrando la calculadora...")
            break

        if option == "5":
            current_number = 0.0
            print("El resultado ha sido reiniciado.")
            continue

        # Pedimos el número nuevo
        new_number = number_input()   # <-- AQUÍ sí se llama la función
        if new_number is None:
            continue

        # Ejecutamos la operación
        result = operation(option, current_number, new_number)
        if result is not None:
            current_number = result
            print(f"Resultado actualizado: {current_number}")


if __name__ == "__main__":
    main()