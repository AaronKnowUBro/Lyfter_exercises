# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
# 1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”


def count_words(text):
    upper_count = 0
    lower_count = 0

    for letter in text:
        if 'A' <= letter <= 'Z':   
            upper_count += 1
        elif 'a' <= letter <= 'z': 
            lower_count += 1

    print(f"There are {upper_count} upper cases and {lower_count} lower cases")

count_words("I Love Hamburgers")
