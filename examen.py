from funcioness import *
import os,time,random,msvcrt 

while True:
    limpiar_pantalla()
    print("""
          _______________________________
                PROTOTIPO
          _______________________________
          1)Asignar sueldos aleatorios
          2)Clasificar sueldos
          3)Ver estadisticas
          4)Reporte de sueldos
          5)Salir del programa
          _______________________________""")
    

    try:
        opc = int(input("Ingrese la opción deseada : "))
        if opc == 1:
            opc_1()
        elif opc ==2:
            opc_2()
        elif opc ==3:
            opc_3()
        elif opc ==4:
            opc_4()
        elif opc ==5:
            opc_5()
            break
        else:
            print("ERROR. La opción tiene que ser entre 1 y 5!")
            time.sleep(2)
    except:
        print("ERROR! OPCION INVALIDA")
        time.sleep(2)
