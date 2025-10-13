import requests

def opciones(pais):
    print(f'''¿Qué quiere saber de {pais}?:
        1 - Capital
        2 - Población
        3 - Territorio
    ''')
    op = input("Ingrese una opción: ")

    url = f"https://restcountries.com/v3.1/name/{pais}?fullText=true&lang=es"
    respuesta = requests.get(url)
    datos = respuesta.json() 

    if isinstance(datos, list) and len(datos) > 0:
        pais_info = datos[0]

        if op == "1":
            capital = pais_info.get("capital", ["No disponible"])[0]
            print(f"La capital de {pais} es: {capital}")

        elif op == "2":
            poblacion = pais_info.get("population", "No disponible")
            print(f"La población de {pais} es: {poblacion:,}")

        elif op == "3":
            area = pais_info.get("area", "No disponible")
            print(f"El territorio de {pais} es: {area} km²")

        else:
            print("Opción no válida.")
    else:
        print("❌ No se encontró el país en la API.")


def letra_pais(pais):
    url = f"https://restcountries.com/v3.1/name/{pais}?lang=es"
    respuesta = requests.get(url)
    datos = respuesta.json()

    if isinstance(datos, list) and len(datos) > 0:
        print("🔎 Coincidencias encontradas:")
        for i in datos:
            print(f" - {i['name']['common']}")
    else:
        print(f"❌ No se encontraron países que contengan '{pais}'.")


pais = input("Ingrese el nombre del país: ")

opciones(pais)

