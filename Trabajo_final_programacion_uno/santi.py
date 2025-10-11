import requests
import streamlit as st

st.title("Búsqueda de Países 🚀")

pais = st.text_input("Ingresá el nombre de un país:")

if st.button("Buscar"):
    url = f"https://restcountries.com/v3.1/name/{pais}?fullText=true&lang=es"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]  # Tomamos el primer resultado
        nombre = data["name"]["common"]
        capital = data.get("capital", ["Sin capital"])[0]
        region = data.get("region", "Desconocida")
        poblacion = data.get("population", "No disponible")
        moneda = list(data["currencies"].keys())[0]
        bandera = data["flags"]["png"]

        st.write(f"📍 País: {nombre}")
        st.write(f"🏙️ Capital: {capital}")
        st.write(f"🌎 Región: {region}")
        st.write(f"👥 Población: {poblacion}")
        st.write(f"💰 Moneda: {moneda}")
        st.image(bandera, caption=f"Bandera de {nombre}", width=200)
    else:
        st.error("❌ No se encontró el país o hubo un error en la búsqueda.")
