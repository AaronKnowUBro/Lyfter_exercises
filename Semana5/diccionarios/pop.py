list_of_keys = ['access_level', 'age']
employee = {'name': 'Aaron', 'email': 'aaron@aaron.com', 'access_level': 5, 'age': 25}

for key in list_of_keys:
    employee.pop(key, None)

print(employee)
