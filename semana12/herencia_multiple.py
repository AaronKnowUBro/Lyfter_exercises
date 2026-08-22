class Phone:
    def __init__(self, number: str):
        self.number = number

    def make_call(self, target_number: str):
        print(f"Llamando a {target_number} desde {self.number}...")


class CameraMixin:
    def take_photo(self):
        print("¡Foto capturada y guardada en la galería!")


# Herencia Múltiple: hereda de Phone Y de CameraMixin
class SmartPhone(Phone, CameraMixin):
    def __init__(self, number: str, model: str):
        super().__init__(number)
        self.model = model


# Prueba del código
if __name__ == "__main__":
    mi_telefono = SmartPhone(number="8888-8888", model="Galaxy S24")

    # Métodos heredados de clases distintas
    mi_telefono.make_call("7777-7777")  # De la clase Phone
    mi_telefono.take_photo()            # Del mixin CameraMixin