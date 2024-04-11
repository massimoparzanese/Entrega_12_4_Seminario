def Crear_estructura_jugadores(nombre,goles,evitados,asis,lista_jugadores):
    """Esta funcion la utilizo en el inciso 1, en esta lo que hago es recibir las listas
    con los datos de todos los jugadores junto con la lista donde voy a guardar en este caso
    diccionarios, donde cada diccionario tiene 4 claves, todas autoexplicativas de lo que 
    guardan dentro:Nombre,goles,goles evitados y asistencias. Cada diccionario representa un único jugador."""
    jugador={}
    for i in range(len(nombre)):
      jugador["nombre"]=nombre[i]
      jugador["goles"]=goles[i]
      jugador["goles evitados"]=evitados[i]
      jugador["asistencias"]=asis[i]
      lista_jugadores.append(jugador)
      jugador={} 
    #jugador={}
    #jugador["nombre"]=nombre
    #jugador["goles"]=goles
    #jugador["goles evitados"]=evitados
    #jugador["asistencias"]=asis


def obtener_goleador(lista):
   """Esta funcion obtiene como parametro la lista de los jugadores, creo 1 variable max para buscar el maximo goleador/a del equipo, 
   y una variable nom, para retornar su nombre. En este caso decido retornar tambien los goles 
   para corrovorar que esta bien, y a su vez, que el usuario sepa cuantos goles hizo el goleador/a.
    Utilizo esta función para el inciso 2 """
   max = -1
   nom = ""
   for i in lista:
       if i["goles"]  > max:
           nom = i["nombre"]
           max = i["goles"] 
   jug = {}
   jug["nombre"]=nom
   jug["goles"]=max
   return jug
 
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
    sus goles, goles evitados y asistencias(en el mismo orden que estan escritos acá, estan guardados en la tupla). Lo primero que hago es declarar la variable max, para ir comparando a medida que recorro la lista
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

def promedio_goles_equipo(partidos_temporada,lista_jugadores):
    """Esta funcion la utilizo para resolver el sub-inciso 4, la cual recibe 2 parametros: 
    .Partidos temporada: es una tupla con los partidos jugados en toda la temporada
    .lista_jugadores: Es una lista de diccionarios con los datos de todos los jugadores
    La variable tot la usaré para ir sumando los goles de todos los jugadores para conseguir la cantidad total de goles
    del equipo, con el for recorro y sumo, luego transformo los goles y los partidos a numeros reales, para tener un resultado mas 
    exacto y luego retorno"""
    tot = 0
    for i in lista_jugadores:
        tot = tot + i["goles"]
    tot = float(tot)
    numero = float(partidos_temporada)
    tot = tot / numero
    return tot

def promedio_del_goleador(lista_jugadores,partidos_temporada):
    """Esta funcion la utilizo para el sub-inciso 5, recibiendo como parametro la lista de jugadores y los partidos 
    que jugo el equipo en toda la temporada. En esta funcion llamo a la funcion que me devuelve el goleador del equipo
    y luego retorno su promedio goleador dividiendo la cantidad de goles por los partidos jugados"""
    goleador =  obtener_goleador(lista_jugadores)
    goles = float(goleador["goles"])
    return goles / partidos_temporada