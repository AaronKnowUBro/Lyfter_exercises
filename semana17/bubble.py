import unittest
import random

def bubble_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("El parámetro debe ser una lista.")
    
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


class TestBubbleSort(unittest.TestCase):

    def test_lista_pequena(self):
        lista = [5, 2, 8, 1, 3]
        resultado = bubble_sort(lista)
        self.assertEqual(resultado, [1, 2, 3, 5, 8])

    def test_lista_grande(self):
        lista = random.sample(range(1, 1000), 150)
        lista_esperada = sorted(lista)
        resultado = bubble_sort(lista)
        self.assertEqual(resultado, lista_esperada)

    def test_lista_vacia(self):
        lista = []
        resultado = bubble_sort(lista)
        self.assertEqual(resultado, [])

    def test_parametro_no_es_lista(self):
        parametros_invalidos = ["texto", 123, (1, 2, 3), {"a": 1}, True]
        for param in parametros_invalidos:
            with self.subTest(param=param):
                with self.assertRaises(TypeError):
                    bubble_sort(param)


if __name__ == "__main__":
    unittest.main()