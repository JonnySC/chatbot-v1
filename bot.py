import nltk
from nltk.chat.util import Chat, reflections

# Descargar recursos de NLTK (solo es necesario hacerlo una vez)
nltk.download('punkt')
nltk.download('wordnet')

pairs = [
    # Pares de patrones y respuestas
    [
        r"Hola bot",
        ["Hola, que puedo hacer por ti?"]
    ],
    [
        r"puedes decirme que es compuevolucion?",
        ["Compuevolucion (CE) es una empresa mexicana establecida desde 2010 que se especializa en soluciones de TI y servicios basados en cloud."]
    ],
    [
        r"como me puede ayudar?",
        ["Nuestro equipo te ayudara a contratar el servicio indicado para tu empresa. Nos esforzamos dia a dia para tener el mejor servicio al cliente y brindar la mejor experiencia a cada una de las empresas que confian en nosotros."]
    ],

    # Puedes agregar más pares de patrones y respuestas aquí
]

def get_response(user_input):
    chat = Chat(pairs, reflections)
    response = chat.respond(user_input)
    return response

"""def chat_bot():
    print("¡Hola! Soy un bot de chat. Escribe 'salir' para finalizar la conversación.")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'salir':
            print("Bot: ¡Hasta luego! Espero haberte sido de ayuda.")
            break
        response = chat.respond(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chat_bot()
"""