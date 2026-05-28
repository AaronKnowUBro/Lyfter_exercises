def main():
    current_number = 0.0

    while True:
        print("\n--- Calculadora ---")
        print(f"Número actual: {current_number}")
        print("Seleccione una opción:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Borrar resultado")
        print("6. Salir")

        option = input("Ingrese su opción: ")

        if option not in ["1", "2", "3", "4", "5", "6"]:
            print("Opción inválida, intente de nuevo.")
            continue

        if option == "6":
            print("Cerrando la calculadora...")
            break

        if option == "5":
            current_number = 0.0
            print("🔄 El resultado se ha reiniciado a 0.")
            continue

        new_number_input = input("Ingrese un número: ")

        try:
            new_number = float(new_number_input)
        except ValueError:
            print("❌ Número inválido, intente de nuevo.")
            continue

        if option == "1":
            current_number += new_number
        elif option == "2":
            current_number -= new_number
        elif option == "3":
            current_number *= new_number
        elif option == "4":
            if new_number == 0:
                print("❌ No se puede dividir entre cero.")
                continue
            current_number /= new_number

        print(f"✅ Resultado actualizado: {current_number}")


if __name__ == "__main__":
    main()
