GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
import time
import random

iniciar_trivia = True
intentos = 0

while iniciar_trivia == True:
    intentos += 1
    puntaje = random.randint(0, 10)
    nombre = input(GREEN + "Ingresa tu nombre " + RESET)

    print(GREEN + "\nHola", nombre,
          " Bienvenido a mi trivia sobre Nutricion Deportiva" + RESET)
    print(GREEN + "\nVeamos cuanto sabes sobre los macro-nutrienes" + RESET)
    print(GREEN + "\nInicialmente tienes", puntaje,
          "puntos, veamos cuantos logras alcanzar" + RESET)

    print(
        "\nResponde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta:\n"
    )

    print("\nIntento número:", intentos)
    input("Presiona Enter para continuar")

    print("Empezamos en 5 segundos\n")
    time.sleep(5)

    print("1) ¿Que alimento es proteina?")
    print("a. pollo")
    print("b. arroz")
    print("c. tamal")
    print("d. huevo, carne")

    respuesta_1 = input(CYAN + "\nTu respuesta: " + RESET)

    while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = input(
            "\nDebes responder una alternativa        valida, Ingresa nuevamente tu respuesta "
        )

        if respuesta_1 == "a":
            puntaje += 5
            print("\nRespuesta correcta, Muy bien", nombre, "!!")
        elif respuesta_1 == "b":
            puntaje -= 5
            print("\nIncorrecto, arroz es carbohidrato")
        elif respuesta_1 == "c":
            puntaje = puntaje / 2
            print("\nTotalmente incorrecto", nombre,
                  "tamal no es          proteina")
        elif respuesta_1 == "d":
            puntaje = puntaje * 2
            print("\nExcelente", nombre,
                  "ambos alimentos son              proteina")

    print("\nTu puntaje actual es", puntaje, ".")

    print("\n2) ¿Que alimento es carbohidrato?\n")
    print("a. pollo")
    print("b. arroz, papa")
    print("c. caramelo")
    print("d. galleta")

    respuesta_2 = input(CYAN + "\nTu respuesta: " + RESET)

    while respuesta_2 not in ("a", "b", "c", "d"):
        respuesta_2 = input(
            "Debes responder una alternativa valida, Ingresa nuevamente tu respuesta "
        )

        if respuesta_2 == "b":
            puntaje = puntaje * 2
            print("\nExcelente, ambos son carbohidraos , Muy            bien",
                  nombre, "!")
        elif respuesta_2 == "a":
            puntaje -= 5
            print("\nIncorrecto, pollo es proteina")
        elif respuesta_2 == "c":
            puntaje -= 5
            print("\nTotalmente incorrecto", nombre, "no es     carbohidrato")
        elif respuesta_2 == "d":
            puntaje = puntaje / 2
            print("\nCorrecto", nombre, "es carbohidrato")

    print("\nTu puntaje actual es", puntaje, ".")

    print("\n3) ¿Que alimento es grasa natural?")
    print("a. mantequilla")
    print("b. arroz")
    print("c. chicle")
    print("d. palta")

    respuesta_3 = input(CYAN + "\nTu respuesta: " + RESET)

    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input(
            "Debes responder una alternativa valida, Ingresa nuevamente tu respuesta "
        )

    if respuesta_3 == "d":
        puntaje = puntaje * 2
        print("\nExcelente, Muy bien", nombre, "!")
    elif respuesta_3 == "a":
        puntaje += 5
        print("\nCorrecto", nombre, "mantequilla es una fuente de grasa")
    elif respuesta_3 == "b":
        puntaje = puntaje / 2
        print("\nTotalmente incorrecto", nombre, "pescado es proteina")
    elif respuesta_3 == "c":
        puntaje -= 5
    print("\nIncorrecto", nombre, "atun es proteina")

    print(CYAN + "\nTu puntaje actual es", puntaje, "." + RESET)

    print(GREEN + "\nGracias", nombre,
          " por jugar a la trivia,       alcanzaste", puntaje,
          "puntos" + RESET)

    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir,o cualquier tecla para finalizar: ").lower(
        )

if repetir_trivia != "si":
    print("\nEspero que lo hayas pasado bien, hasta pronto!")
    iniciar_trivia = False
