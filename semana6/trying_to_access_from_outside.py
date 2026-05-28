# Experimente con el concepto de scope:
#    1. Intente accesar a una variable definida dentro de una función desde afuera.
#    2.  Intente accesar a una variable global desde una función y cambiar su valor.


def inside_function():
    message = "Michael Jackson"
    print (message)

inside_function()

print (message)