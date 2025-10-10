import requests

print("------------------------")
print("Aca empezamos a escribir el codigo")
print("------------------------")

pais = input("Ingresá el nombre de un país: ")

# Llamada a la API
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

    print(f"\n📍 País: {nombre}")
    print(f"🏙️ Capital: {capital}")
    print(f"🌎 Región: {region}")
    print(f"👥 Población: {poblacion}")
    print(f"💰 Moneda: {moneda}")
    print(f"🏁 Bandera: {bandera}")

else:
    print("❌ No se encontró el país o hubo un error en la búsqueda.")
