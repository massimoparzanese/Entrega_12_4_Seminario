def influencia_total(goles,numero1,goles_evitados,numero2,asis,numero3):
    """Esta funcion lo que hace es: multiplicar los valores goles, goles_evitados y asistencias, por el numero correspondiente 
    por el que debo multiplicarlo. Que en este caso son: numero1, numero2 y numero3. 
    Y retorna en la variable total la suma de los 3 ya multiplicados por las variables.
    La utilizo para el inciso 3, la hago aparte de la funcion principal para mayor legibilidad"""
    
    goles = goles * numero1
    goles_evitados = goles_evitados * numero2
    asis = asis * numero3
    tot = goles + goles_evitados + asis
    return tot

def mas_influyente(influencia,lista_jugadores):
    """Esta funcion recibe por parametro una tupla llamada influencia y una lista de diccionarios de los jugadores del club.
    La tupla me servirá para resolver el sub-inciso 3, la tupla tiene los valores para sacar la influencia de cada jugador segun
    sus goles, goles evitados y asistencias. Lo primero que hago es declarar la variable max, para ir comparando a medida que recorro la lista
    y jugador será la variable donde guadaré cual fue dicho jugador. En el for solo recorro, llamo a la funcion influencia_total, que me devuelve
    el valor a comparar y luego comparo si es mayor al maximo o no, esta funcion retorna el jugador mas influyente"""
    max = -1
    jugador = [{}]
    for i in lista_jugadores:
        total = influencia_total(i["goles"],influencia[0],i["goles evitados"],influencia[1],i["asistencias"],influencia[2])
        if total > max :
            max = total
            jugador[0] = i
    return jugador