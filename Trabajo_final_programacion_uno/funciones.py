import streamlit as st
import pandas as pd
import requests
import os

# --- FUNCIONES ---
def obtener_paises_api():
    """Obtiene todos los países de la API RestCountries."""
    url = "https://restcountries.com/v3.1/all"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        paises = []
        for p in data:
            nombre = p.get("name", {}).get("common", "Desconocido")
            capital = p.get("capital", ["Desconocida"])[0]
            region = p.get("region", "Desconocida")
            subregion = p.get("subregion", "Desconocida")
            poblacion = p.get("population", 0)
            paises.append({
                "nombre": nombre,
                "capital": capital,
                "región": region,
                "subregión": subregion,
                "población": poblacion
            })

        # Ordenar alfabéticamente y guardar solo los primeros 50
        paises = sorted(paises, key=lambda x: x["nombre"])[:50]
        pd.DataFrame(paises).to_csv("paises.csv", index=False)
        return paises

    except Exception as e:
        st.warning(f"No se pudo acceder a la API ({e}). Cargando datos locales...")
        return None


def cargar_paises_local():
    """Carga países desde el archivo CSV local."""
    if os.path.exists("paises.csv"):
        return pd.read_csv("paises.csv").to_dict(orient="records")
    else:
        return []


def buscar_paises(paises, termino):
    """Filtra los países por coincidencia parcial en el nombre."""
    termino = termino.lower()
    return [p for p in paises if termino in p["nombre"].lower()]



#import requests

#print("------------------------")
#print("Aca empezamos a escribir el codigo")
#print("------------------------")

#pais = input("Ingresá el nombre de un país: ")

# Llamada a la API
#url = f"https://restcountries.com/v3.1/name/{pais}?fullText=true&lang=es"
#response = requests.get(url)

#if response.status_code == 200:
#    data = response.json()[0]  # Tomamos el primer resultado
#    nombre = data["name"]["common"]
#    capital = data.get("capital", ["Sin capital"])[0]
#    region = data.get("region", "Desconocida")
#    poblacion = data.get("population", "No disponible")
#    moneda = list(data["currencies"].keys())[0]
#    bandera = data["flags"]["png"]

#    print(f"\n📍 País: {nombre}")
#    print(f"🏙️ Capital: {capital}")
#    print(f"🌎 Región: {region}")
#    print(f"👥 Población: {poblacion}")
#    print(f"💰 Moneda: {moneda}")
#    print(f"🏁 Bandera: {bandera}")

#else:
#    print("❌ No se encontró el país o hubo un error en la búsqueda.")