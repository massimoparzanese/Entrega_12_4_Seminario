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
 