def list_of_songs():
    with open(r"C:\Users\acald\canciones_test\canciones.txt") as file:
        for lines in file.readlines():
	        print(f'Linea: {lines}')


print("\n--- Leyendo archivo ---")
list_of_songs()