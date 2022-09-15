#damos la bienvenida
import time 
import random
iniciar_trivia = True
intentos = 0
print("\n\033[33mBienvenidos a mi trivia de deportes \033[39m")
nombre = input("\n\033[36m¿Cómo te llamas?:\033[39m ")
time.sleep(1)
print(f"\nHola {nombre}. Pondremos a prueba tus conocimientos")
#escribio la guia y pistas del juego
print("\n\033[32mResponda las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar su respuesta:\033[39m ")
print(f'''\n\033[33mPara hacerlo más interesante, hay una alternativa misteriosa que elevará tu puntaje hasta las nubes.
La pista secreta es el número '6'. Te deseo mucha suerte {nombre}.\033[39m''')
time.sleep(3)
while iniciar_trivia == True:
    intentos += 1
    #creo mi lista de puntaje que recopilará los puntos a favor o en contra de cada pregunta
    puntaje = []
    #una puntaje aleatorio inicial se sumará a mi lista
    puntaje.append(random.randint(0,12))
    print(f"\033[31m\nIntento número:\033[39m {intentos}")
    print(f"Has empezado con {puntaje[0]} puntos.")
    input("Presiona Enter para continuar") 
#aquí van mi pregunta 1
    print("\n\033[35m1) ¿Cómo se llama el jugador de futbol galardonado con más balores de oro?\033[39m\n")
# mi objetivo es hacer un listado de alternativas por cada pregunta.  
    a = " a) Cristiano Ronaldo"
    b = " b) Lionel Meesi"
    c = " c) Kylian Mbappé"
    d = " d) Ronaldinho Gaúcho"
    e = " e) Pelé"
    f = " sorpresa"
    pregunta1_alternativas = [a, b, c, d, e, f]
    #una vez recopilado, creo un bucle en un rango de 5 y lo imprimo despues de 1s
    for alternativa in range(0, 5):
        print(pregunta1_alternativas[alternativa])
        time.sleep(1)
    respuesta_1 = input("Respuesta: ")
    #este bucle es para conseguir una alternativa válida
    while respuesta_1 not in ("a", "b", "c", "d", "e", "f"):
        respuesta_1 = input('''\033[31mIngrese una respuesta válida porfavor, se reitera usar las letras en minúscula.\033[39m
    Coloque su nueva respuesta: ''')
    # con append busco llenar de valores mi lista de puntaje.   
    if respuesta_1 == "b":
        puntaje.append(20)
        print("\033[32mCORRECTO!\033[39m")
    # esta alternativa misteriosa suma considerablemente los resultados
    elif respuesta_1 == "f":
        puntaje.append(10000)
        print("\033[35mDesbloqueaste la alternativa misteriosa, y serás recompensado por ello!\033[39m")
    else:
        puntaje.append(-10)
        print("\033[31mINCORRECTO!\033[39m")
    # con esto busco sumar los elementos de mi lista puntaje.
    # así sabre cuanto de puntaje tengo al culminar cada pregunta.
    suma_puntajes = 0
    for punto in puntaje:
        suma_puntajes += punto
    print(f"\033[36mTienes {suma_puntajes} puntos hasta el momento, tú puedes {nombre}.\033[39m")
    time.sleep(2)
# aquí empieza mi pregunta 2 y se repite el proceso de la pregunta 1
    print("\n\033[35m2) ¿Qué selección se hizo campeón en la ultima edición del Mundial Rusia 2018?\033[39m\n")
    
    a = " a) Brasil"
    b = " b) Alemania"
    c = " c) España"
    d = " d) Francia"
    e = " e) Inglaterra"
    f = " sorpresa"
    pregunta2_alternativas = [a, b, c, d, e, f]
    for alternativa in range(0, 5):
        print(pregunta2_alternativas[alternativa])
        time.sleep(1)
    respuesta_2 = input("Respuesta: ")
    while respuesta_2 not in ("a", "b", "c", "d", "e", "f"):
        respuesta_2 = input('''\033[31mIngrese una respuesta válida porfavor, se reitera usar las letras en minúscula.\033[39m
    Coloque su nueva respuesta: ''')
#esta pregunta se diferencia de la anterior porque colocaré respuestas alternativas.      
    if respuesta_2 == "a":
        puntaje.append(-15)
        print(f"\033[31mINCORRECTO!\033[39m.Pero dejame decirte {nombre}. Brasil fue campeón por última vez el año 2002.")
    elif respuesta_2 == "b":
        puntaje.append(-5)
        print(f"\033[31mINCORRECTO!\033[39m.Pero dejame decirte {nombre}. Alemania fue campeón por última vez el año 2014.")
    elif respuesta_2 == "c":
        puntaje.append(-10)
        print(f"\033[31mINCORRECTO!\033[39m.Pero dejame decirte {nombre}. España fue campeón por última vez el año 2010.")
    elif respuesta_2 == "e":
        puntaje.append(-20)
        print(f"\033[31mINCORRECTO!\033[39m.Pero dejame decirte {nombre}. Inglaterra fue campeón por última vez el año 1966.")
    elif respuesta_2 == "f":
        puntaje.append(10000)
        print("\033[35mDesbloqueaste la alternativa misteriosa, y serás recompensado por ello!\033[39m")
    else:
        puntaje.append(30)
        print("\033[32mCORRECTO!\033[39m")
    suma_puntajes = 0  #con esto sabre cuanto de puntaje tengo hasta la pregunta 2
    for punto in puntaje:
        suma_puntajes += punto
    print(f"\033[36mTienes {suma_puntajes} puntos hasta el momento, tú puedes {nombre}.\033[39m")
    time.sleep(2)
#aqui empieza mi pregunta 3
    print("\n\033[35m3) ¿Qué selección sudamericana tiene más trofeos de campeonato mundial en la historia del futbol?\033[39m\n")
    
    a = " a) Argentina"
    b = " b) Uruguay"
    c = " c) Brasil"
    d = " d) Chile"
    e = " e) Colombia"
    pregunta3_alternativas = [a, b, c, d, e, f]
    for alternativa in range(0, 5):
        print(pregunta3_alternativas[alternativa])
        time.sleep(1)
    respuesta_3= input("Respuesta: ")
    while respuesta_3 not in ("a", "b", "c", "d", "e", "f"):
        respuesta_3 = input('''\033[31mIngrese una respuesta válida porfavor, se reitera usar las letras en minúscula.\033[39m
Coloque su nueva respuesta: ''')
    if respuesta_3 == "c":
        puntaje.append(50)
        print("\033[32mCORRECTO!\033[39m")
    elif respuesta_3 == "f":
        puntaje.append(10000)
        print("\033[35mDesbloqueaste la alternativa misteriosa, y serás recompensado por ello!\033[39m")
    else:
        puntaje.append(-10)
        print("\033[31mINCORRECTO!\033[39m")
    
    suma_puntajes = 0
    #además incluire un puntaje adicional para beneficiar al jugador
    bono_final = random.randint(0,12)
    for punto in puntaje:
        suma_puntajes += punto
    print(f"El bono final aleatorio es: {bono_final}")    
    print(f"\033[36m{nombre} obtuviste un total de {suma_puntajes+bono_final} puntos.\033[39m")
    time.sleep(1)
    #con estas condiciones busco asignar un mensaje de acorde al resultado final
    if suma_puntajes < 20:
        print(f"\nUna pregunta, en qué planeta esta viviendo? Es broma, sé que lo harás mejor despues.")
    elif suma_puntajes < 50:
        print(f"\nUsted sabe algo de fútbol.")
    elif suma_puntajes <= 112:
        print(f"\nUsted es una eminencia del fútbol.")
    else:
        print(f"\nUsted además de saber de fúbtol es un genio. Felicidades por romper la marca.")
    time.sleep(1)
    print("\033[33m\nGracias por participar, si desea mejorar su resultado, intente las veces que desee.\033[39m")
#aqui termina la activida del primer intento
    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input("\033[32mIngresa 'si' para repetir, o cualquier tecla para finalizar:\033[39m ").lower()
#aqui se busca saber si el jugador desea jugar nuevamente
    if repetir_trivia != "si":
        print(f"\033[33m\nEntonces nos despedimos definitivamente {nombre}, cuidate!\033[39m")
        iniciar_trivia = False
# en caso de ya no quiera jugar se coloca falso y el bucle finalizará