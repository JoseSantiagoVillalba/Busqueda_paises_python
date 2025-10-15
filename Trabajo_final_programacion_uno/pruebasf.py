import requests
import csv
import os

ARCHIVO = "paises.csv"

def crear_csv():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["País", "Capital", "Población", "Área (km²)"])

def leer_csv():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)

def guardar_en_csv(pais, capital, poblacion, area):
    datos = leer_csv()
    
    for fila in datos:
        if fila["País"].lower() == pais.lower():
            print("⚠️ Ese país ya está guardado.")
            return

    if len(datos) >= 30:
        print(f"⚠️ Ya hay {len(datos)} países guardados.")
        continuar = input("¿Desea agregar igualmente este país? (s/n): ").lower()
        if continuar != "s":
            print("❌ No se agregó el país.")
            return

    with open(ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([pais, capital, poblacion, area])
    print(f"✅ {pais} guardado en el archivo.")

def eliminar_pais(nombre_pais):
    datos = leer_csv()
    nuevos = [fila for fila in datos if fila["País"].lower() != nombre_pais.lower()]

    if len(datos) == len(nuevos):
        print(f"❌ No se encontró {nombre_pais} en el archivo.")
        return

    with open(ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["País", "Capital", "Población", "Área (km²)"])
        escritor.writeheader()
        escritor.writerows(nuevos)
    print(f"🗑️ {nombre_pais} eliminado correctamente.")

def buscar_capital(pais):
    pais_info = datos[0]
    capital = pais_info.get("capital", ["No disponible"])[0]
    print(f"La capital de {pais} es: {capital}")
    return capital

def buscar_poblacion(pais):
    pais_info = datos[0]
    poblacion = pais_info.get("population", "No disponible")
    print(f"La población de {pais} es: {poblacion:,}")
    return poblacion

def territorio_pais(pais):
    pais_info = datos[0]
    area = pais_info.get("area", "No disponible")
    print(f"El territorio de {pais} es: {area} km²")
    return area

def opciones(pais):
    print(f'''\n¿Qué quiere hacer con {pais}?:
        1 - Mostrar capital
        2 - Mostrar población
        3 - Mostrar territorio
        4 - Guardar país
        5 - Eliminar país del CSV
    ''')
    op = input("Ingrese una opción: ")

    if isinstance(datos, list) and len(datos) > 0:
        pais_info = datos[0]
        capital = pais_info.get("capital", ["No disponible"])[0]
        poblacion = pais_info.get("population", "No disponible")
        area = pais_info.get("area", "No disponible")

        if op == "1":
            buscar_capital(pais)
        elif op == "2":
            buscar_poblacion(pais)
        elif op == "3":
            territorio_pais(pais)
        elif op == "4":
            guardar_en_csv(pais, capital, poblacion, area)
        elif op == "5":
            eliminar_pais(pais)
        else:
            print("Opción no válida.")
    else:
        print("❌ No se encontró el país en la API.")

crear_csv()

bandera = True

while bandera:
    pais = input("\nIngrese el nombre del país que desea buscar (o 'salir' para terminar): ")
    if pais.lower() == "salir":
        print("👋 Programa finalizado.")
        break
    url=f"https://restcountries.com/v3.1/name/{pais}/lang/spanish"
    respuesta = requests.get(url)

    if respuesta.status_code != 200:
        print("❌ No se encontró el país en la API.")
        continue

    datos = respuesta.json()

    # ✅ Traducción automática desde la API
    pais_traducido = datos[0]["translations"]["spa"]["common"]
    print(f"🔍 Mostrando información de: {pais_traducido}")

    opciones(pais_traducido)

    seguir = input("\n¿Desea buscar otro país? (si/no): ").lower()
    if seguir == "no":
        print("👋 Fin de la búsqueda. ¡Hasta luego!")
        break
