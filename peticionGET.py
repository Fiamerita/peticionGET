import requests

def comprobar_estado():
    try:
        # Realizar la petición GET a la API
        respuesta = requests.get('https://api.ejemplo.com/estado')

        # Verificar si la petición fue exitosa
        respuesta.raise_for_status()
        print(respuesta.text)

    except requests.exceptions.ConnectionError:
        print("Bienvenido")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición: {e}")

def interactuar_con_api():
    while True:
        mensaje = str(input("Escriba código: "))

        if mensaje == '200':
            print("OK")
        else:
            print("ERROR")
            break

        try:
            respuesta = requests.post(
                'https://api.ejemplo.com/estado',
                json={'mensaje': mensaje}
            )
            respuesta.raise_for_status()
            datos = respuesta.json()
            print(f"Respuesta del servidor: {datos}")
        except requests.exceptions.ConnectionError:
            print("Error: FALLO DE CONEXIÓN.")
        except requests.exceptions.RequestException as e:
            print(f"Error al enviar la solicitud: {e}")
        except ValueError:
            print("La respuesta no está en formato JSON.")

if __name__ == '__main__':
    comprobar_estado()
    interactuar_con_api()
