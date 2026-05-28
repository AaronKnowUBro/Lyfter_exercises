file = open(r"C:\Users\acald\canciones_test\canciones.txt", "r")
songs = file.readlines()
file.close()

print("=== Canciones originales ===")
for s in songs:
    print(s, end="")

ordered = sorted(songs)

print("\n=== Canciones ordenadas ===")
for s in ordered:
    print(s, end="")

out = open(r"C:\Users\acald\canciones_test\canciones_ordenadas.txt", "w")
for s in ordered:
    out.write(s)
out.close()

print("\nLas canciones ordenadas fueron guardadas en el archivo.")
