class Person:
    def __init__(self, name):
        self.name = name

class Bus:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def board(self, person):
        if len(self.passengers) < self.capacity:
            self.passengers.append(person)
            print(f"{person.name} subió al bus.")
        else:
            print("El bus está lleno, no se pueden agregar más pasajeros.")

    def disembark(self, name):
        for p in self.passengers:
            if p.name == name:
                self.passengers.remove(p)
                print(f"{name} bajó del bus.")
                return
        print(f"{name} no está en el bus.")

bus = Bus(2)
person1 = Person("Aaron")
person2 = Person("Chris Tren")
person3 = Person("Mike Tren")

bus.board(person1)
bus.board(person2)
bus.board(person3)

bus.disembark("Chris Tren")
bus.disembark("Paco")