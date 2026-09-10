from datetime import datetime
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        args_fmt = ", ".join(map(str, args))
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print(f"func:{func.__name__} - args: {args_fmt} - [{fecha_actual}] - Resultado: {resultado}")
        return resultado
    return wrapper

def validate_numbers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        todos_los_valores = list(args) + list(kwargs.values())
        for valor in todos_los_valores:
            if not isinstance(valor, (int, float)) or isinstance(valor, bool):
                raise TypeError(f"El argumento {valor} no es un número válido.")
        return func(*args, **kwargs)
    return wrapper

@log_call
@validate_numbers
def multiply(first_number, second_number):
    return first_number * second_number

raw_first = input("Por favor ingresa el primer número a multiplicar: ")
raw_second = input("Por favor ingresa el segundo número a multiplicar: ")

try:
    first_number = float(raw_first) if "." in raw_first else int(raw_first)
    second_number = float(raw_second) if "." in raw_second else int(raw_second)
except ValueError:
    first_number = raw_first
    second_number = raw_second

try:
    result = multiply(first_number, second_number)
    print(f"Resultado {result}")
except TypeError as error:
    print(f"Error: {error}")