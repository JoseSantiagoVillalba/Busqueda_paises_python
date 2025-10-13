import requests

def buscar_capital(pais):
    if isinstance(datos, list) and len(datos) > 0:
        pais_info = datos[0]
        capital = pais_info.get("capital", ["No disponible"])[0]
        print(f"La capital de {pais} es: {capital}")
    else:
        print("No se pudo obtener información del país.")

def buscar_poblacion(pais):
    if isinstance(datos, list) and len(datos) > 0:
        pais_info = datos[0]
        poblacion = pais_info.get("population", "No disponible")
        if isinstance(poblacion, int):
            print(f"La población de {pais} es: {poblacion:,}")
        else:
            print(f"La población de {pais} es: {poblacion}")
    else:
        print("No se pudo obtener información del país.")

def territorio_pais(pais):
    if isinstance(datos, list) and len(datos) > 0:
        pais_info = datos[0]
        area = pais_info.get("area", "No disponible")
        print(f"El territorio de {pais} es: {area} km²")
    else:
        print("No se pudo obtener información del país.")

def opciones(pais):
    print(f'''¿Qué quiere saber de {pais}?:
        1 - Capital
        2 - Población
        3 - Territorio
    ''')
    op = input("Ingrese una opción: ")

    if isinstance(datos, list) and len(datos) > 0:
        if op == "1":    
            buscar_capital(pais)
        elif op == "2":
            buscar_poblacion(pais)
        elif op == "3":
            territorio_pais(pais)
        else:
            print("Opción no válida.")
    else:
        print("❌ No se encontró el país en la API.")

pais = input("Ingrese el nombre del país: ")

url = f"https://restcountries.com/v3.1/name/{pais}?fullText=true&lang=es"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    datos = respuesta.json()
else:
    print("Error al conectar con la API.")
    datos = []

opciones(pais)


