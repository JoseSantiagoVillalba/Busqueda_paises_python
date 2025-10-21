import pandas as pd
df = pd.read_csv("paises.csv")


#Funcion de menu.

def menu():
    print("""     Busqueda Paises     
        Marque la opcion 1 para buscar un pais por nombre: 
        Marque la opcion 2 para buscar un pais por rango de poblacion: 
        Marque la opcion 3 para buscar un pais por continente: 
        Marque la opcion 4 para buscar un pais por rango de superficie: 
        Marque la opcion 5 para buscar menor/mayor del archivo y el promedio:
        Marque la opcion 6 para saber cuantos paises hay por continente:
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

#Santi aca cantidad de paises por continente
def cantidad_paises_por_continente():
    if df.empty:
        return "No hay datos cargados."
    
    conteo = df["Continente"].value_counts()
    return conteo
    print(cantidad_paises_por_continente())


# función: mayor, menor y promedio de población
def estadisticas_poblacion():
    if df.empty:
        return "No hay datos disponibles."

    pais_menor = df.loc[df["Población (millones)"].idxmin()]
    pais_mayor = df.loc[df["Población (millones)"].idxmax()]
    promedio = df["Población (millones)"].mean()

    return f"""
        País con menor población: {pais_menor['Nombre']} ({pais_menor['Población (millones)']} millones)
        País con mayor población: {pais_mayor['Nombre']} ({pais_mayor['Población (millones)']} millones)
        Promedio de población: {round(promedio, 2)} millones
        """


#Estas funciones sirven para ordenar segun nombre, poblacion y superficie. 

def ordenar_por_nombre_ascendente(df_filtrado, ascendente=True):
    return df_filtrado.sort_values(by="Nombre", ascending=ascendente)


def ordenar_por_poblacion_ascendente(df_filtrado, ascendente=True):
    return df_filtrado.sort_values(by="Población (millones)", ascending=ascendente)


def ordenar_por_superficie_ascendente(df_filtrado, ascendente=True):
    return df_filtrado.sort_values(by="Superficie (km²)", ascending=ascendente)


# Esta funcion esta buscando que tipo de opcion hay. Y si coincide con la 1, 2, 3 o 4
# llama a las funciones pertinentes.

def opciones(opcion):
    try:
        bandera = True
        while bandera:
            if opcion == "1":
                pais = input("Ingrese un nombre o letras a buscar: ")
                resultado = busqueda_paises(pais)

            elif opcion == "2":
                min_p:float = float(input("Ingrese población mínima (millones): "))
                max_p:float = float(input("Ingrese población máxima (millones): "))
                resultado = busqueda_poblacion(min_p, max_p)

                # Muestra estadísticas de población general
                print(estadisticas_poblacion())

            elif opcion == "3":
                continente = input("Ingrese un continente a buscar: ")
                resultado = busqueda_continente(continente)

            elif opcion == "4":
                min_s:float = float(input("Ingrese superficie mínima (km²): "))
                max_s:float = float(input("Ingrese superficie máxima (km²): "))
                resultado = busqueda_superficie(min_s, max_s)

            elif opcion == "5":
                resultado=estadisticas_poblacion()

            elif opcion == "6":
                resultado=cantidad_paises_por_continente()
            else:
                print("Opción inválida")
                break

            print("\nResultados encontrados:")
            print(resultado)

            ordenar = input("""
                Si desea ordenar por nombre (N), 
                por población (P), 
                por superficie (S), 
                o volver al menú (X): """)

            if ordenar.lower() == "n" and isinstance(resultado, pd.DataFrame):
                print(ordenar_por_nombre_ascendente(resultado))
            elif ordenar.lower() == "p" and isinstance(resultado, pd.DataFrame):
                print(ordenar_por_poblacion_ascendente(resultado))
            elif ordenar.lower() == "s" and isinstance(resultado, pd.DataFrame):
                print(ordenar_por_superficie_ascendente(resultado))
            elif ordenar.lower() == "x":
                bandera = False

    except ValueError:
        print("Error: ingresaste un valor numérico inválido. Por favor intenta de nuevo.")
    except KeyError as e:
        print(f"Error: la columna {e} no existe en los datos.")
    except TypeError as e:
        print(f"Error de tipo: {e}. Asegurate de que los datos sean correctos.")
    except KeyboardInterrupt:
        print("\nInterrupción por parte del usuario. Saliendo...")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
