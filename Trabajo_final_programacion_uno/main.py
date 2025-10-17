import pandas as pd
import funciones

df = pd.read_csv("paises.csv")
bandera = True
while bandera == True:
    funciones.menu()
    opcion = input("Indique la opcion: ")
    funciones.opciones(opcion)
    salir = input("Si desea salir del programa indique X")
    if salir.lower() == "x":
        bandera = False