
edad=input("cuantos años tienes")
while not edad.isdigit():
    edad=input("digita un numero")
edad= int(edad)
if edad <=25:
     print("Estudiante")
elif edad > 25 :
        print("Profesor")
elif edad>= 65:
            print("Master")