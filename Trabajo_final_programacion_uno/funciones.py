

import pandas as pd
df = pd.read_csv("paises.csv")


#Funcion de menu.

def menu():
    print("""     Busqueda Paises     
        Marque la opcion 1 para buscar un pais por nombre: 
        Marque la opcion 2 para buscar un pais por continente: 
        Marque la opcion 3 para buscar un pais por rango de poblacion: 
        Marque la opcion 4 para buscar un pais por rango de superficie: 
        """)


#Estas funciones son las que buscan por nombre, continente, rango de poblacion y rango de superficie.

def busqueda_paises(nombre):
    coincidencias = df[df["Nombre"].str.lower().str.contains(nombre.lower())]
    if coincidencias.empty:
        return "No se encontraron países que coincidan."
    else:
        return coincidencias
    
def busqueda_poblacion(min_p, max_p):
    coincidencias = df[(df["Población (millones)"] >= min_p) & (df["Población (millones)"] <= max_p)]
    
    if coincidencias.empty:
        return "No se encontraron países que coincidan con ese rango de población."
    else:
        return coincidencias


def busqueda_continente(continente):
    coincidencias = df[df["Continente"].str.lower().str.contains(continente.lower())]
    if coincidencias.empty:
        return "No se encontraron Continentes que coincidan."
    else:
        return coincidencias


def busqueda_superficie(min_s, max_s):
    coincidencias = df[(df["Superficie (km²)"] >= min_s) & (df["Superficie (km²)"] <= max_s)]
    
    if coincidencias.empty:
        return "No se encontraron países que coincidan con ese rango de superficie."
    else:
        return coincidencias


#Estas funciones sirven para ordenar segun nombre, poblacion y superficie. 


def ordenar_por_nombre_ascendente(df_filtrado, ascendente=True):
    return df_filtrado.sort_values(by="Nombre", ascending=ascendente)





# Esta funcion esta buscando que tipo de opcion hay. Y si coincide con la 1, 2, 3 o 4
# llama a las funciones pertinentes. 
def opciones(opcion):
    try:
            if opcion == "1":
                bandera = True
                while bandera == True:
                    pais = input("Ingrese un nombre o letras a buscar: ")
                    resultado = busqueda_paises(pais)
                    print(resultado)
                    ordenar = input("Si desea ordenar de manera ascendente indique Y: ")
                    # aca me estoy fijando si se pone y y si esto es un dataframe ya que si no 
                    # va a aparecer como que se quiere ordenar el mensaje de error y eso genera
                    # lios
                    if ordenar.lower() == "y" and isinstance(resultado, pd.DataFrame):
                        resultado_ordenado = ordenar_por_nombre_ascendente(resultado)
                        print("\nResultados ordenados:")
                        print(resultado_ordenado)
                    salir = input("Si desea volver al menu indique X")
                    if salir.lower() == "x":
                        bandera = False
                    
            if opcion == "2":
                bandera = True
                while bandera == True:
                    min_p = float(input("Ingrese población mínima (millones): "))
                    max_p = float(input("Ingrese población máxima (millones): "))
                    resultado = busqueda_poblacion(min_p, max_p)
                    print(resultado)
                    salir = input("Si desea volver al menu indique X")
                    if salir.lower() == "x":
                        bandera = False
            if opcion == "3":
                bandera = True
                while bandera == True:
                    continente = input("Ingrese un continente a buscar: ")
                    resultado = busqueda_continente(continente)
                    print(resultado)
                    salir = input("Si desea volver al menu indique X")
                    if salir.lower() == "x":
                        bandera = False
            if opcion == "4":
                bandera = True
                while bandera == True:
                    min_s = float(input("Ingrese superficie mínima (km²): "))
                    max_s = float(input("Ingrese superficie máxima (km²): "))
                    resultado = busqueda_superficie(min_s, max_s)
                    print(resultado)
                    salir = input("Si desea volver al menu indique X")
                    if salir.lower() == "x":
                        bandera = False
    except:
        pass
    finally:
        pass




