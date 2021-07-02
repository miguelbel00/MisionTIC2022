#Miguel Angel Beltran
#UDFJC


#declaracion de variables
listaJuan = input()
listaCami = input()
paquetesLetras = input()
juan = 0
cami = 0
nuevo = ""

#Primer string Juan
#Segundo string Cami
#Tercer string Paquete de letras

#for para recorrer el tercer string
for i in range(len(paquetesLetras)):
  aux = 0
  aux2 = 0
  y = 0
  #se evalua cada letra del primer string si esta en el tercer string
  #en caso de estarlo se suma punto a juan y se sale del ciclo
  while y < (len(listaJuan)):
    if listaJuan[y] == paquetesLetras[i]:
      juan += 1
      break
    else:
      aux += 1
    y += 1 
  y= 0
  #se evalua cada letra del segundo string si esta en el tercer string
  #en caso de estarlo se suma punto a cami y se sale del ciclo
  while y < len(listaCami):
    if listaCami[y] == paquetesLetras[i]:
      cami += 1
      break
    else:
      aux2 +=2
    y += 1  


   #se evalua quien tiene mas puntos despues de revisar el siguiente caracter del tercer string
  if juan < cami:
    nuevo += "C"

  elif cami == juan:
    nuevo += "E"

  else:
    nuevo += "J"

#se imprime el string con los resultados
print(nuevo)

