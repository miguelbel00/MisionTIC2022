#Miguel Angel Beltran
#UDFJC

#primer funcion con parametros:  1 lista
def generos (listgen):
  lista1 = listgen
  lista2 = []
  #se crea el ciclo que va a averificar si algun elemento
  #no esta en la lista, en caso verdadero, se adiciona a una lista vaci
  for i in lista1:
    if i not in lista2:
      lista2.append(i)
  #se devuelve la lista generada con los elementos que no estan en la lista
  return lista2
  
#segunda funcion con parametros: 2 listas 1 string
def filtrar_por_genero(listin, listgene, gener):
  listaindice = listin
  listagenero = listgene
  genero = gener
  #se crea la lista auxiliar
  aux = []
  #se recorre la lista de indices ubicando los elementos como
  #indices de la lista de generos, en caso de que el genero del parametro
  #sea igual al elemento de la lista de generos en el indice de parametro
  #se adicionara a la lista auxiliar
  for indice in listaindice:
    if listagenero[indice] == genero:
      aux.append(indice)
  return aux
  
#tercera funcion con parametros : 2 listas
def comparar_inventarios(inv1,inv2):
  inventario1 = inv1
  inventario2 = inv2
  #creacion de la lista auxiliar
  aux2 = []
  #se recorre los elementos del inventario1 y se evalua si no esta en inventario2
  #en caso verdadero se adiciona a la lista auxiliar
  for elemento1 in inventario1:
    if elemento1 not in inventario2:
      aux2.append(elemento1)
  return aux2
  
#cuarta funcion con parametros: 2 listas
def se_pueden_mover(suc1, suc2):
  sucursal1 = suc1
  sucursal2 = suc2
  #se crean las 2 listas auxiliares donde se guardaran los elementos sin repetir de cada inventario
 
  libros1 = []
  libros2 = []
  #ciclo para seleccionar los elementos de la sucursal1 que no esten en la sucursal2
  #luego se adiciona a la lista auxiliar1
  for elemento1 in sucursal1:
    if elemento1 not in sucursal2:
      libros1.append(elemento1)
      
  #ciclo para seleccionar los elementos de la sucursal2 que no esten en la sucursal1
  #luego se adiciona a la lista auxiliar2
  for elemento2 in sucursal2:
    if elemento2 not in sucursal1:
      libros2.append(elemento2)
  
  #se evalua cual lista es la mas reducida y se devuelve ese valor
  if len(libros1) > len(libros2):
    return len(libros2)
  else:
    return len(libros1)
