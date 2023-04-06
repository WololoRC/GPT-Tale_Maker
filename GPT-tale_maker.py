#!/usr/bin/python3
"""
Script muy rudimentario para jugar a una aventura basada en texto con chatGPT
"""
import openai

if __name__ == "__main__":
    openai.api_key = input("Introduce API key: ")
    print()

    # @'role': 'system' sirve para indicarle al modelo cual es el rol que debe tomar
    messages = [{"role": "system", "content": "Similar a un juego de Dungeons & Dragons, debes crear una historia donde el usuario debe elegir cual sera el siguiente paso en la trama. El modo en que haras esto es el siguiente: Inicia un hilo conductor hasta llegar a una situacion, en ese punto debes dar multiples opicones numeradas, el usuario debe elegir la opcion indicando el numero, realizada esta acción debes contunar la historia a partir de aquello que el usuaro decidio."}]

    print("Introducete como personaje.")
    print("...")
    print()

    while True:
        a_input = input(">>> ")

        # Lo que dice el usuario #
        messages.append({"role": "user", "content": a_input})

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                messages=messages)

        # Agrega las respuestas de GPT a la array de la conversacion, #
        # de este modo existe continuidad entre las respuestas #
        messages.append({"role": "assistant", "content": response.choices[0].message.content})

        print()
        print("---------------------------------")
        print()
        print(response.choices[0].message.content)
