# Cree una función que le de la vuelta a un string y lo retorne.

def my_string():
    text = 'Pizza con piña'
    reversed_text = ''

    for counter in range(len(text) - 1, -1, -1):
        reversed_text += text[counter]

    return reversed_text

print(my_string())
