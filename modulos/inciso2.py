def obtener_goleador(lista):
   max = -1
   nom = ""
   for i in lista:
       if i["goles"]  > max:
           nom = i["nombre"]
           max = i["goles"] 
   jug = ["El jugador/a goleador/a del club fue:"]
   jug.append(nom)
   jug.append("con la cantidad de")
   jug.append(max)
   jug.append("goles")
   return jug
 