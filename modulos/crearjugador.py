def datos_jug(nombre,goles,evitados,asis):
    """Esta funcion la utilizo en el inciso 1, en esta lo que hago es recibir cada dato de un jugador(nombre,goles,goles evitados y asistencias), 
    con ello hago un diccionario donde cada clave es lo que representa y lo retorno para agregarlo en la estructura de datos. Esto podría hacer mas cosas, pero se me ocurrio hacerlo así"""
    
    jugador={}
    jugador["nombre"]=nombre
    jugador["goles"]=goles
    jugador["goles evitados"]=evitados
    jugador["asistencias"]=asis
    return jugador
    