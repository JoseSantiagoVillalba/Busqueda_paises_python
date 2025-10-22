import pandas as pd
data_frame_del_cvs = pd.read_csv("paises.csv")


pd.set_option('display.max_rows', None)

pd.set_option('display.max_columns', None)

#Funcion de menu.

def menu():
    print("""     Busqueda Paises     
        Marque la opcion 1 para buscar un pais por nombre: 
        Marque la opcion 2 para buscar un pais por rango de poblacion: 
        Marque la opcion 3 para buscar un pais por continente: 
        Marque la opcion 4 para buscar un pais por rango de superficie: 
        Si desea Salir marque X: 
        """)


#Estas funciones son las que buscan por nombre, continente, rango de poblacion y rango de superficie.

def busqueda_paises(nombre):
    coincidencias = data_frame_del_cvs[data_frame_del_cvs["Nombre"].str.lower().str.contains(nombre.lower())]
    if coincidencias.empty:
        return "No se encontraron países que coincidan."
    else:
        return coincidencias
    
def busqueda_poblacion(min_p, max_p):
    coincidencias = data_frame_del_cvs[(data_frame_del_cvs["Población (millones)"] >= min_p) & (data_frame_del_cvs["Población (millones)"] <= max_p)]
    
    if coincidencias.empty:
        return "No se encontraron países que coincidan con ese rango de población."
    else:
        return coincidencias


def busqueda_continente(continente):
    coincidencias = data_frame_del_cvs[data_frame_del_cvs["Continente"].str.lower().str.contains(continente.lower())]
    if coincidencias.empty:
        return "No se encontraron Continentes que coincidan."
    else:
        return coincidencias


def busqueda_superficie(min_s, max_s):
    coincidencias = data_frame_del_cvs[(data_frame_del_cvs["Superficie (km²)"] >= min_s) & (data_frame_del_cvs["Superficie (km²)"] <= max_s)]
    
    if coincidencias.empty:
        return "No se encontraron países que coincidan con ese rango de superficie."
    else:
        return coincidencias






#Aca cantidad de paises por continente
def cantidad_paises_por_continente(datos=None):
    if datos is None:
        datos = data_frame_del_cvs
    if datos.empty:
        return "No hay datos cargados."
    
    conteo = datos["Continente"].value_counts()
    resultado = "Cantidad de países por continente:\n"
    for cont, cant in conteo.items():
        resultado += f"{cont}: {cant} -- "
    return resultado








def estadisticas_superficie(datos=None):
    if datos is None:
        datos = data_frame_del_cvs
    if datos.empty:
        return "No hay datos disponibles."

    pais_menor = datos.loc[datos["Superficie (km²)"].idxmin()]
    pais_mayor = datos.loc[datos["Superficie (km²)"].idxmax()]
    promedio = datos["Superficie (km²)"].mean()

    return f"""
        País con menor Superficie: {pais_menor['Nombre']} ({pais_menor['Superficie (km²)']} millones)
        País con mayor Superficie: {pais_mayor['Nombre']} ({pais_mayor['Superficie (km²)']} millones)
        Promedio de Superficie: {round(promedio, 2)} millones
        """


def estadisticas_poblacion(datos=None):
    if datos is None:
        datos = data_frame_del_cvs
    if datos.empty:
        return "No hay datos disponibles."

    pais_menor = datos.loc[datos["Población (millones)"].idxmin()]
    pais_mayor = datos.loc[datos["Población (millones)"].idxmax()]
    promedio = datos["Población (millones)"].mean()

    return f"""
        País con menor población: {pais_menor['Nombre']} ({pais_menor['Población (millones)']} millones)
        País con mayor población: {pais_mayor['Nombre']} ({pais_mayor['Población (millones)']} millones)
        Promedio de población: {round(promedio, 2)} millones
        """












#Estas funciones sirven para ordenar segun nombre, poblacion y superficie. 

def ordenar_por_nombre_ascendente(nombre_filtrado, ascendente=True):
    return nombre_filtrado.sort_values(by="Nombre", ascending=ascendente)


def ordenar_por_poblacion_ascendente(pop_filtrado, ascendente=True):
    return pop_filtrado.sort_values(by="Población (millones)", ascending=ascendente)


def ordenar_por_superficie_ascendente(sup_filtrado, ascendente=True):
    return sup_filtrado.sort_values(by="Superficie (km²)", ascending=ascendente)







# Esta funcion esta buscando que tipo de opcion hay. Y si coincide con la 1, 2, 3 o 4
# llama a las funciones.

def opciones(opcion):
    bandera = True
    while bandera:
        try:
            if opcion == "1":
                pais = input("Ingrese un nombre o letras a buscar: ")
                resultado = busqueda_paises(pais)

            elif opcion == "2":
                try:
                    min_p = float(input("Ingrese población mínima (millones): "))
                    max_p = float(input("Ingrese población máxima (millones): "))
                    resultado = busqueda_poblacion(min_p, max_p)
                except ValueError:
                    print("Error: Por favor, ingrese solo numeros para continuar")
                    continue  # vuelve al inicio del bucle sin romper el programa

            elif opcion == "3":
                continente = input("Ingrese un continente a buscar: ")
                resultado = busqueda_continente(continente)

            elif opcion == "4":
                try:
                    min_s = float(input("Ingrese superficie mínima (km²): "))
                    max_s = float(input("Ingrese superficie máxima (km²): "))
                    resultado = busqueda_superficie(min_s, max_s)
                except ValueError:
                    print("Error: Por favor, ingrese solo numeros para continuar")
                    continue
            else:
                print("Opción inválida.")
                break

            print("Resultados encontrados:")
            print(resultado)


            if isinstance(resultado, pd.DataFrame):
                ordenar = input("""
Si desea ordenar por nombre (N), 
por población (P), 
por superficie (S), 
o volver al menú (X): """)

                if ordenar.lower() == "n":
                    print(ordenar_por_nombre_ascendente(resultado))
                elif ordenar.lower() == "p":
                    print(ordenar_por_poblacion_ascendente(resultado))
                elif ordenar.lower() == "s":
                    print(ordenar_por_superficie_ascendente(resultado))
                elif ordenar.lower() == "x":
                    bandera = False
                else:
                    print("Ingrese una de las opciones dadas.")

                # --- Estadísticas filtradas ---
                ver_estadisticas = input("¿Desea ver estadísticas de este conjunto de países? (S/N): ")
                if ver_estadisticas.lower() == "s":
                    print(estadisticas_poblacion(resultado))
                    print(estadisticas_superficie(resultado))
                    print(cantidad_paises_por_continente(resultado))


        except KeyError as e:
            print(f"Error: La columna {e} no existe en los datos. Revisa los encabezados del CSV.")
        except TypeError as e:
            print(f"Error de tipo: {e}. Es posible que el CSV tenga datos faltantes o mal formateados.")
        except KeyboardInterrupt:
            print("Interrupción por parte del usuario. Saliendo del programa...")
            bandera = False
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
