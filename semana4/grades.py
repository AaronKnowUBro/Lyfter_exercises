grades_counter = 0
failed_grades = 0
average_failed = 0
aproved_grades = 0
average_aproved = 0
total_sum = 0

total_grades = int(input("Por favor ingrese la cantidad de notas que tienes: "))

while grades_counter < total_grades:
    current_grade = int(input("Por favor ingrese la nota: "))
    total_sum += current_grade

    if current_grade < 70:
        failed_grades = failed_grades + 1
        average_failed = average_failed + current_grade
    else:
        aproved_grades = aproved_grades + 1
        average_aproved = average_aproved + current_grade

    grades_counter += 1


average_failed = average_failed / failed_grades if failed_grades > 0 else 0
average_aproved = average_aproved / aproved_grades if aproved_grades > 0 else 0
overall = total_sum / total_grades if total_grades > 0 else 0



print(f"El estudiante tiene esta cantidad de notas aprovadas: {aproved_grades}")
print(f"El promedio de notas aprovadas es de: {average_aproved}")
print(f"El estudiante tiene esta cantidad de notas desaprobadas: {failed_grades}")
print(f"El promedio de notas desaprobadas es de:  {average_failed}")
print(f"El promedio total de notas es: {overall}")
