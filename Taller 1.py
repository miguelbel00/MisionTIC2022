#Miguel Angel Beltran 
#UDFJC

#funcion para calcular el numero de platanos y tocinetas
def pasabocas(numeroPapitas ):

  platanos = 4 + (2*numeroPapitas)
  tocinetas = int((platanos + numeroPapitas)/5)
  return platanos, round(tocinetas)

#funcion para calcular el tamano del paquete
def tamanoPaquete(tocinetas):
  if (tocinetas >=0 and tocinetas <= 20):
    return "uno"
  elif (tocinetas >=21 and tocinetas <=30):
    return "dos"
  elif (tocinetas >=31 and tocinetas <=50):
    return "tres"
  elif tocinetas >50:
    return "cuatro"
#ingresa el numero de papitas
print("Digite el numero de papitas: ")

papitas = int(input())

# el valor de platanos y tocinetas son los 2 valores retorno de la funcion pasabocas

platanos, tocinetas = pasabocas(papitas)
#Mostrar en pantalla los resultados
print(papitas, platanos, tocinetas)

print(tamanoPaquete(tocinetas))
