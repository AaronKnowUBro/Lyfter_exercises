class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        self.balance = initial_balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Ingreso exitoso: +${amount:.2f}. Saldo actual: ${self.balance:.2f}")
        else:
            print("El monto a ingresar debe ser mayor que cero.")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("El monto a retirar debe ser mayor que cero.")
            return

        if amount <= self.balance:
            self.balance -= amount
            print(f"Retiro exitoso: -${amount:.2f}. Saldo actual: ${self.balance:.2f}")
        else:
            print("Fondos insuficientes para realizar el retiro.")


class SavingsAccount(BankAccount):
    def __init__(self, initial_balance: float = 0.0, min_balance: float = 0.0):
        super().__init__(initial_balance)
        self.min_balance = min_balance

    def withdraw(self, amount: float):
        if amount <= 0:
            print("El monto a retirar debe ser mayor que cero.")
            return

        if self.balance - amount < self.min_balance:
            raise ValueError(
                f"Error: El retiro de ${amount:.2f} dejaría el saldo (${self.balance - amount:.2f}) "
                f"por debajo del mínimo permitido (${self.min_balance:.2f})."
            )
        
        super().withdraw(amount)


if __name__ == "__main__":
    print("--- Configuración Inicial de la Cuenta de Ahorros ---")
    saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
    saldo_minimo = float(input("Ingrese el saldo mínimo permitido: "))

    cuenta = SavingsAccount(initial_balance=saldo_inicial, min_balance=saldo_minimo)

    while True:
        print(f"\n--- Menú de Opciones (Saldo Actual: ${cuenta.balance:.2f}) ---")
        print("1. Ingresar dinero")
        print("2. Retirar dinero")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            monto = float(input("Ingrese el monto a depositar: "))
            cuenta.deposit(monto)
        elif opcion == "2":
            monto = float(input("Ingrese el monto a retirar: "))
            try:
                cuenta.withdraw(monto)
            except ValueError as e:
                print(e)
        elif opcion == "3":
            print("Gracias por utilizar el sistema bancario. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")