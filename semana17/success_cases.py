# Ejercicio 3: Suma de elementos de una lista
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Ejercicio 4: Invertir un string
def reverse_string(text):
    return text[::-1]

# Ejercicio 5: Contar mayúsculas y minúsculas
def count_case(text):
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    return f"There's {upper_count} upper cases and {lower_count} lower cases"

# Ejercicio 6: Ordenar palabras separadas por guion
def sort_hyphenated_words(text):
    words = text.split("-")
    words.sort()
    return "-".join(words)

# Ejercicio 7: Filtrar números primos de una lista
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def filter_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes


import unittest

class TestFunctionsExercises(unittest.TestCase):

    # --- Ejercicio 3: Suma de listas ---
    def test_sum_list_standard(self):
        self.assertEqual(sum_list([4, 6, 2, 29]), 41)

    def test_sum_list_with_negatives(self):
        self.assertEqual(sum_list([-10, 5, 15, -2]), 8)

    def test_sum_list_empty(self):
        self.assertEqual(sum_list([]), 0)

    # --- Ejercicio 4: Invertir string ---
    def test_reverse_string_standard(self):
        self.assertEqual(reverse_string("Hola mundo"), "odnum aloH")

    def test_reverse_string_single_word(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_reverse_string_palindrome(self):
        self.assertEqual(reverse_string("reconocer"), "reconocer")

    # --- Ejercicio 5: Contar mayúsculas y minúsculas ---
    def test_count_case_standard(self):
        self.assertEqual(
            count_case("I love Nación Sushi"), 
            "There's 3 upper cases and 13 lower cases"
        )

    def test_count_case_all_upper(self):
        self.assertEqual(
            count_case("PYTHON"), 
            "There's 6 upper cases and 0 lower cases"
        )

    def test_count_case_with_punctuation(self):
        self.assertEqual(
            count_case("Hello, World! 123"), 
            "There's 2 upper cases and 8 lower cases"
        )

    # --- Ejercicio 6: Ordenar palabras con guiones ---
    def test_sort_hyphenated_words_standard(self):
        input_text = "python-variable-funcion-computadora-monitor"
        expected = "computadora-funcion-monitor-python-variable"
        self.assertEqual(sort_hyphenated_words(input_text), expected)

    def test_sort_hyphenated_words_already_sorted(self):
        self.assertEqual(sort_hyphenated_words("apple-banana-cherry"), "apple-banana-cherry")

    def test_sort_hyphenated_words_mixed(self):
        self.assertEqual(sort_hyphenated_words("zorro-auto-casa"), "auto-casa-zorro")

    # --- Ejercicio 7: Filtrar números primos ---
    def test_filter_primes_standard(self):
        self.assertEqual(filter_primes([1, 4, 6, 7, 13, 9, 67]), [7, 13, 67])

    def test_filter_primes_no_primes(self):
        self.assertEqual(filter_primes([0, 1, 4, 6, 8, 9, 10]), [])

    def test_filter_primes_all_primes(self):
        self.assertEqual(filter_primes([2, 3, 5, 7, 11]), [2, 3, 5, 7, 11])


if __name__ == "__main__":
    unittest.main()