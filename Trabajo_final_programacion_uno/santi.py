import requests
import streamlit as st

# 🎨 Configuración general de la página
st.set_page_config(
    page_title="Buscador de Países 🌍",
    page_icon="🌎",
    layout="centered",
)

# 🏷️ Título principal
st.title("🌍 Buscador de Países")
st.markdown("### Escribí el nombre de un país.")

# ✏️ Campo de entrada
pais = st.text_input("🔎 Ingresá el nombre de un país:")

# 🚀 Acción al presionar el botón
if st.button("Buscar"):
    if pais.strip() == "":
        st.warning("⚠️ Por favor, escribí un nombre antes de buscar.")
    else:
        url = f"https://restcountries.com/v3.1/name/{pais}?fullText=true&lang=es"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()[0]

            nombre = data["name"]["common"]
            capital = data.get("capital", ["Sin capital"])[0]
            region = data.get("region", "Desconocida")
            poblacion = data.get("population", "No disponible")
            moneda = list(data["currencies"].keys())[0]
            bandera = data["flags"]["png"]

            # 📦 Diseño con columnas
            col1, col2 = st.columns([2, 1])

            with col1:
                st.markdown(f"## 📍 {nombre}")
                st.markdown(f"**🏙️ Capital:** {capital}")
                st.markdown(f"**🌎 Región:** {region}")
                st.markdown(f"**👥 Población:** {poblacion:,}".replace(",", "."))
                st.markdown(f"**💰 Moneda:** {moneda}")

            with col2:
                st.image(bandera, caption=f"Bandera de {nombre}", use_container_width=True)

            st.success("✅ Datos obtenidos correctamente.")
        else:
            st.error("❌ No se encontró el país o hubo un error en la búsqueda.")

# ✨ Pie de página
st.markdown("---")
st.markdown(
    "<small>Desarrollado en Python con ❤️ y Streamlit — Ejemplo educativo</small>",
    unsafe_allow_html=True,
)
