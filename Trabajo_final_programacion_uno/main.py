import pandas as pd
import funciones


df = pd.read_csv("paises.csv")
bandera = True
while bandera == True:
    funciones.menu()
    opcion = input("Indique la opcion: ")
    if opcion.lower() == "x":
        bandera = False
    else:
        funciones.opciones(opcion)

