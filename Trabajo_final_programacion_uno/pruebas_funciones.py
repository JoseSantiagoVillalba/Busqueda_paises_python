def obtener_paises_de_api():
    url_api = "https://restcountries.com/v3.1/independent?status=true"
    paises_formateados = []

    print("Obteniendo datos de la API de restcountries.com...")
    try:
        respuesta = requests.get(url_api)
        respuesta.raise_for_status()
        datos_api = respuesta.json()

        # selecciona 10 países al azar
        paises_seleccionados = random.sample(datos_api, 10)

        for pais_data in paises_seleccionados:
            nombre = pais_data.get('name', {}).get('common', 'N/A')
            poblacion = pais_data.get('population', 0)
            superficie = pais_data.get('area', 0)

            continentes = pais_data.get('continents', ['N/A'])
            continente = continentes[0] if continentes else 'N/A'

            paises_formateados.append({
                'nombre': nombre,
                'poblacion': int(poblacion),
                'superficie': int(superficie),
                'continente': continente
            })

        print(f"✅ ¡Éxito! Se obtuvieron {len(paises_formateados)} países de la API.")
        return paises_formateados

    except requests.exceptions.RequestException as error:
        print(f"❌ Error al conectar con la API: {error}")
        return []

if __name__ == "__main__":
    paises = obtener_paises_de_api()
    if paises:
        with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            writer = csv.DictWriter(archivo, fieldnames=campos)
            writer.writeheader()
            writer.writerows(paises)
        print("📁 Archivo 'paises.csv' creado con éxito.")


def obtener_paises_de_api():
    url_api = "https://restcountries.com/v3.1/independent?status=true"
    paises_formateados = []

    print("Obteniendo datos de la API de restcountries.com...")
    try:
        respuesta = requests.get(url_api)
        respuesta.raise_for_status()
        datos_api = respuesta.json()

        paises_seleccionados = random.sample(datos_api, 10)

        for pais_data in paises_seleccionados:
            nombre = pais_data.get('name', {}).get('common', 'N/A')
            poblacion = pais_data.get('population', 0)
            superficie = pais_data.get('area', 0)
            continentes = pais_data.get('continents', ['N/A'])
            continente = continentes[0] if continentes else 'N/A'

            paises_formateados.append({
                'nombre': nombre,
                'poblacion': int(poblacion),
                'superficie': int(superficie),
                'continente': continente
            })

        print(f"✅ ¡Éxito! Se obtuvieron {len(paises_formateados)} países de la API.")
        return paises_formateados

    except requests.exceptions.RequestException as error:
        print(f"❌ Error al conectar con la API: {error}")
        return []


def guardar_paises_en_csv(lista_paises, ruta_archivo):
    if not lista_paises:
        print("⚠️ No hay datos de países para guardar en el CSV.")
        return False

    encabezados = ['nombre', 'poblacion', 'superficie', 'continente']

    try:
        with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezados)
            escritor_csv.writeheader()
            escritor_csv.writerows(lista_paises)

        print(f"📁 Datos guardados exitosamente en '{ruta_archivo}'.")
        return True

    except IOError as e:
        print(f"❌ Error al escribir en el archivo CSV: {e}")
        return False


def cargar_paises_desde_csv(ruta_archivo):
    lista_paises = []

    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            for fila in lector_csv:
                try:
                    lista_paises.append({
                        'nombre': fila['nombre'],
                        'poblacion': int(fila['poblacion']),
                        'superficie': int(fila['superficie']),
                        'continente': fila['continente']
                    })
                except (ValueError, KeyError):
                    print(f"⚠️ Advertencia: Se omitió una fila con datos inválidos en el CSV: {fila}")

    except FileNotFoundError:
        print(f"❌ Error: El archivo CSV '{ruta_archivo}' no fue encontrado.")
    
    return lista_paises


if __name__ == "__main__":
    ruta_csv = "paises.csv"
    paises = obtener_paises_de_api()

    if paises:
        guardar_paises_en_csv(paises, ruta_csv)

    paises_cargados = cargar_paises_desde_csv(ruta_csv)
    print(f"\n📋 Se cargaron {len(paises_cargados)} países desde el archivo CSV.")