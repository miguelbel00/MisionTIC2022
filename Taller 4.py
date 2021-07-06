#Miguel Angel Beltran
#UDFJC

import json

##declaracion de variables y carga de json 
cadena  = input()
cadenajson = json.loads(cadena)
listaproductos = input().split(sep=" ")
psalida = ""
nsalida = 0


##se evalua en ciclos si existe en la cadena la palabra
## lo que rota es la cadena en la lista de productos
##por ende la primer palabra encontrada se guardara
for x in listaproductos:
  for y in cadenajson:
    ##si se encuentra similitud ente las palabras
    if x == y:
      ##se suman los valores del diccionaro json encontrados por la clave 
      nsalida += cadenajson[y]
      ##se suman los strings(claves)
      psalida += y
      ##se pone un espacio entre cada string
      psalida += " "
##se imprimen los resultados
print(nsalida)
print(psalida)

