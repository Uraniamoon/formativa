import funciones as fun

trabajadores=[]

while True:
    try:
    print("bienvenidos a la plataforma de trabajdores")
    print("1.registar trabjador")
    print("2.listar los trabajadores")
    print("3.imprimir planilla")
    print("salir")

opcion = int(input("ingrese una opcion"))

if opcion == 1:
     fun.registar_trabajador(trabajadores)
elif opcion == 2:
     fun.listar_trabajadores(trabajadores)
elif opcion == 3:
     fun.imprimir_planilla(trabajadores)
elif opcion == 4:
   break
else:
     print("opcion invalida,intente nuevamente")
except: ValueError