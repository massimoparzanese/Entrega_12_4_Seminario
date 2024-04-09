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