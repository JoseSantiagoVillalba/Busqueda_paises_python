import pandas as pd
import streamlit as st
import os
import requests

# ------------------------------
# Busqueda del archivo y creacion.
# ------------------------------
# Estas Funciones sirven para buscar si existe el archivo paises.csv y si no se llama a la api
# para crear uno: 
# 
# Primero se verifica si el archivo "paises.csv" existe en la carpeta:
# Si ya existe, devuelve True.
# Si no existe, llama a crear_csv_paises() para generarlo y
# se revisa de nuevo si el archivo fue creado correctamente.
# 
# 
# Si el archivo no existe:
# Llama a la API de restcountries para obtener los datos de todos los países.
# Recorremos el json y extraemos los name, population, continents y area
# A la poblacion la convertimos en millones con 2 decimales para usarla mejor.
# 
# Luego creamos un diccionario con los titulos que usamos en las funciones ´
# para que puedan acceder correctamente y los metemos con el .append()
# Tomamos paises y lo convertimos a un dataframe
# Luego guardamos el dataframe en un archivo csv con el nombre paises.csv solo con los 
# datos que pedimos.
# Mandamos el mensaje de que todo salio bienn. 
#
# Si algo sale mal, no tenemos internet o algo asi se muestran los mensajes de error. 
# ------------------------------

def existe_archivo_paises():
    nombre_archivo = "paises.csv"
    if os.path.exists(nombre_archivo):
        return True
    else:
        crear_csv_paises()
        return os.path.exists(nombre_archivo)

def crear_csv_paises():
    try:
        url = "https://restcountries.com/v3.1/independent?status=true"
        response = requests.get(url)
        response.raise_for_status()

        datos = response.json()
        paises = []
        for pais in datos:
            nombre = pais.get("name", {}).get("common", "Desconocido")
            poblacion = round(pais.get("population", 0) / 1_000_000, 2)
            continente = pais.get("continents", ["Desconocido"])[0]
            superficie = pais.get("area", 0)

            paises.append({
                "Nombre": nombre,
                "Población (millones)": poblacion,
                "Continente": continente,
                "Superficie (km²)": superficie
            })

        data_frame_del_cvs = pd.DataFrame(paises)
        data_frame_del_cvs.to_csv("paises.csv", index=False)
        st.success("Archivo 'paises.csv' creado de manera exitosa.")
        return data_frame_del_cvs

    except requests.RequestException as e:
        st.error(f"Se porduce un error de coneccion con la API: {e}")
        return None
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# ------------------------------
# Busqueda.
# ------------------------------
# Estas Funciones sirven para buscar dentro del cvs por el nombre de la columna: 
# Nombre, Continente, Población (millones) y Superficie (km²)
# se toma el titulo y lo pasamos a lower (por ejemplo con nombre.lower()).
# La variable "coincidencias" se iguala al dataframe del cvs y dentro se busca la columna con el 
# titulo en lower y se retorna la coincidencia.
# Si la coincidencia esta vacia, se retorna un mensaje de error

#Con las busquedas de poblacion y superficie, se agregan parametros de maximo y minimo 
# y se comparan para encontrar los elementos correspondientes. 
# ------------------------------

def busqueda_paises(nombre,data_frame_del_cvs):
    coincidencias = data_frame_del_cvs[data_frame_del_cvs["Nombre"].str.lower().str.contains(nombre.lower())]
    if coincidencias.empty:
        return "No se encontraron países que coincidan."
    else:
        return coincidencias

def busqueda_poblacion(min_p, max_p,data_frame_del_cvs):
    coincidencias = data_frame_del_cvs[(data_frame_del_cvs["Población (millones)"] >= min_p) & (data_frame_del_cvs["Población (millones)"] <= max_p)]
    if coincidencias.empty:
        return "No se encontraron países que coincidan con ese rango de población."
    else:
        return coincidencias

def busqueda_continente(continente,data_frame_del_cvs):
    coincidencias = data_frame_del_cvs[data_frame_del_cvs["Continente"].str.lower().str.contains(continente.lower())]
    if coincidencias.empty:
        return "No se encontraron Continentes que coincidan."
    else:
        return coincidencias

def busqueda_superficie(min_s, max_s,data_frame_del_cvs):
    coincidencias = data_frame_del_cvs[(data_frame_del_cvs["Superficie (km²)"] >= min_s) & (data_frame_del_cvs["Superficie (km²)"] <= max_s)]
    if coincidencias.empty:
        return "No se encontraron países que coincidan con ese rango de superficie."
    else:
        return coincidencias

# ------------------------------
# Estadísticas
# ------------------------------
# Estas funciones muestran la estadistica.
# Se pasan los parámetros del dataframe del cvs completo e igualamos el parametro datos a None.
# Esto es por si no se ha filtrado nada, poder hacerlo con todos los datos del cvs.
# Si los datos estan filtrados (datos != None) se pasa el data_frame_del_cvs filtrado.
# Si los datos estan vacíos tira un error.
# 
# Luego se revisa, en el caso de continente, los ítems con el conteo = datos["Continente"].value_counts()
# y hacemos un for para que pasen la cantidad de países en el conteo
# y se impriman en la variable resultado.
#
# En el caso de poblacion y superficie buscamos la superficie mayor y menor con 
# datos.loc[datos["superficie/poblacion")"].idxmin() o idxmax()] y las metemos en una variable. 
# Y con mean() calculamos la media de la columna y lo ponemos en promedio.
# Por último se imprime todo.
# ------------------------------

def cantidad_paises_por_continente(data_frame_del_cvs,datos=None):
    if datos is None:
        datos = data_frame_del_cvs
    if datos.empty:
        return "No hay datos cargados."
    
    conteo = datos["Continente"].value_counts()
    resultado = "Cantidad de países por continente:\n"

    for continente, cantidad in conteo.items():
        resultado += f"{continente}: {cantidad}\n"
    return resultado

def estadisticas_superficie(data_frame_del_cvs,datos=None):
    if datos is None:
        datos = data_frame_del_cvs
    if datos.empty:
        return "No hay datos disponibles."

    pais_menor = datos.loc[datos["Superficie (km²)"].idxmin()]
    pais_mayor = datos.loc[datos["Superficie (km²)"].idxmax()]
    promedio = datos["Superficie (km²)"].mean()

    return f"""
País con menor Superficie: {pais_menor['Nombre']} ({pais_menor['Superficie (km²)']} km²)
País con mayor Superficie: {pais_mayor['Nombre']} ({pais_mayor['Superficie (km²)']} km²)
Promedio de Superficie: {round(promedio, 2)} km² \n \n
"""

def estadisticas_poblacion(data_frame_del_cvs,datos=None):
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
Promedio de población: {round(promedio, 2)} millones \n \n
"""
