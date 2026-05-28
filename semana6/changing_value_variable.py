number = 5  

def change_number():
    global number  # Estuve investigando y al parecer, para poder cambiar el valor de "number", se necesita usar el "global", ya que con esto se le dice a Python que use la variable que existe fuera de la función, en lugar de crear una nueva dentro.
    number = 10
    print("Inside the function:", number)

change_number()

print("Outside the function:", number)

print ("- - -")

number_test = 5  

def change_number():
    number_test = 10  
    print("Inside the function:", number_test)

change_number()

print("Outside the function:", number_test)