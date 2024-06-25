CARGO=['ceo','desarrollador','analista de datos']

def registrar_trabajador:(trabajadores)
  
  nombre= input("ingrese nombre y apellido del trabajador")
  cargo= input("ingrese cargo respectivo (ceo/desarrollador/analista de datos)")

  while cargo not in CARGO :
  
  print("cargo no existe: ")
  cargo= input("ingrese cargo respectivo (ceo/desarrollador/analista de datos)")

  sueldobruto= int(input("ingrese sueldo bruto: "))
  descuentosalud= sueldobruto * 0.07
  descuentoafp= sueldobruto * 0.12
  liquidoapagar= sueldobruto - descuentosalud -descuentoafp


trabajadores.append ({nombre,cargo,sueldobruto,descuentosalud,descuentoafp,liquidoapagar})

def listar_trabajadores:(trabajadores)
  for trabajador in trabajadores: 
     print(trabajador)
     
def imprimir_planilla:(trabajadores)     
  print()