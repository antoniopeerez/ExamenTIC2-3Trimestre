import random
from tkinter import Menu


# ----  Ejercicios ---- 

#Ejercicio 1
#1. (1p) Crea una función que imprima por pantalla un menú con las opciones: 
# 1- Guardar asignatura 
#2- Borrar asignatura
# 3- Ver Nota media
#4- Ver todas las asignaturas
#  5- Salir

#Ejercicio 1

def muestraMenu():
    
    print("1 - Guardar asignatura")
    print("2 - Borrar asignatura")
    print("3 - Ver Nota media")
    print("4 - Ver todas las asignaturas")
    print("5 - Salir")

    bandera = False

    while bandera == False:
        try:
            opc = int(input("Introduce una opcion: "))
            print("")
            bandera = True
        except:
            print("NO sirve\n")
            bandera = False

    if opc == 5:
        print("Salir del programa...")
    return opc

#Fin ejercicio 1








# ---- Programa principal -----

#Ejercicio 2
def opcion1(asignaturas):
    auxbandera = False
    while auxbandera == False:
        try:
            numAsignaturas = int(input("¿Cuántas asignaturas quieres?: "))
            auxbandera = True
        except:
            print("Incorrecto")
    
    for i in range(0, numAsignaturas):
        materia = input("Añade las asignaturas que quieras: ")
        materia = materia.upper()
        asignaturas.append(materia)
    
    return asignaturas

#Ejercicio4

def opcion2(asignaturas):
    deleteasignatura = input("Introduce el nombre de la asignatura que vayas a eliminar: ")
    deleteasignatura = deleteasignatura.upper()

    try:
        asignaturas.remove(deleteasignatura)
        return True
    except:
        return False
    
#Fin ejercicio 4


























