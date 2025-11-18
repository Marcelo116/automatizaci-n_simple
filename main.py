# __init__.py

from funciones_agentes.obtener_clima import obtener_clima
from funciones_agentes.obtener_precio_accion import obtener_precio_accion

from utils.sanitizar import sanitizar

def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return obtener_precio_accion

    return None

if __name__ == "__main__":
    print("""
*** Chatbot v1.0.0 ***
Hola, soy el Chatbot v1.0.0. Puedo ayudarte a obtener precios de acciones o decirte
la temperatura actual en cualquier ciudad del mundo.
Puedes hacerme preguntas como por ejemplo:
- ¿Cuál es el precio de una acción de Microsoft?
- ¿Cuál es la temperatura actual en la Ciudad de México?
""")
    while True:
        user_input = sanitizar(input("---> "))

        funcion_agente = procesar_input(user_input)

        if funcion_agente is None:
            print("No entendí tu solicitud. Intenta nuevamente.")
            continue

        respuesta = funcion_agente(user_input)
        print(f">>> {respuesta}")
