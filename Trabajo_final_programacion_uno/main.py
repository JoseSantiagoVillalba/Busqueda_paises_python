import streamlit as st
import pandas as pd
import requests
import os

def obtener_paises_api():
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

        paises = sorted(paises, key=lambda x: x["nombre"])[:50]
        pd.DataFrame(paises).to_csv("paises.csv", index=False)
        return paises

    except Exception as e:
        st.warning(f"No se pudo acceder a la API ({e}). Cargando datos locales...")
        return None


def cargar_paises_local():
    if os.path.exists("paises.csv"):
        return pd.read_csv("paises.csv").to_dict(orient="records")
    else:
        return []


def buscar_paises(paises, termino):
    termino = termino.lower()
    return [p for p in paises if termino in p["nombre"].lower()]


st.title("🌍 Búsqueda de Países")

paises = obtener_paises_api()
if not paises:
    paises = cargar_paises_local()

if not paises:
    st.error("No se pudieron cargar los datos de países.")
else:
    termino = st.text_input("🔍 Ingresá el nombre o parte del nombre de un país:")

    if termino:
        resultados = buscar_paises(paises, termino)
        if resultados:
            st.success(f"Se encontraron {len(resultados)} país(es):")
            st.dataframe(pd.DataFrame(resultados))
        else:
            st.warning("No se encontraron coincidencias.")
    else:
        st.info("Escribí el nombre de un país para comenzar la búsqueda.")
