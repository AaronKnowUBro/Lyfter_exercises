from functools import wraps

def log_parametros_y_retorno(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Parámetros posicionales (*args): {args}")
        print(f"Parámetros nombrados (**kwargs): {kwargs}")
        
        resultado = func(*args, **kwargs)
        
        print(f"Retorno de la función: {resultado}")
        return resultado
    return wrapper

@log_parametros_y_retorno
def sumar(a, b, multiplicador=1):
    return (a + b) * multiplicador

sumar(5, 3, multiplicador=2)