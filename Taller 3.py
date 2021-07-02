#Miguel Angel Beltran
#UDFJC

#al momento de almacenar el string reemplazamos el " " por ""
entrada = input("").replace(" ", "")
i = 0
contador = 1
tamano = len(entrada)
numeros = []
letras = []


#iniciamos el ciclo para recorrer el string introducido
for i in range(tamano):
    # debemos hacer la aclaracion que el for no puede 
    # recorrer el tamano por que no existe ese index
    # creamos el apartador para el ultimo elemento del string
  if i == (tamano-1):
      # en caso de que el contador sea mayor que 1 significa que
      # debemos aumentar en 1 el contador por que el elif ya evaluo que es igual a el n-1 caracter
    if contador > 1:
      letras.append(entrada[i])
      numeros.append(contador)
    else:
    #en caso contrario reiniciamos el contador
      contador=1
      letras.append(entrada[i])
      numeros.append(contador)
    #se evalua si el caracter i es igual a i+1
    # en caso verdadero se suma 1 al contador
  elif entrada[i] == entrada[i+1]:
    contador +=1
  else:
      #en caso que el caracter sea diferente se guardara el contador y pondra en 1 otra vez
    letras.append(entrada[i])
    numeros.append(contador)
    contador=1
    
#ciclos para imprimir las respuestas almacenadas en las listas
for elemento in letras:
  print(elemento, sep=" ", end=" ")
print("\n")
for elemento2 in numeros:
  print(elemento2, sep=" ", end=" ")



  


