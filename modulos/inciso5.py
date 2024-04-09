def promedio_del_goleador(goleador,partidos_temporada):
    """Esta funcion la utilizo para el sub-inciso 5, recibiendo como parametro el jugador/a que fue goleador/a y la tupla con los 
       partidos jugados en la temporada, obtengo en la variable goles la cant de goles del jugador/a, lo convierto a flotante junto con los partidos
       para poder obtener un resultado exacto, y luego retorno"""
    
    goles = goleador["goles"]
    goles = float(goles)
    part = float(partidos_temporada)
    return goles/part