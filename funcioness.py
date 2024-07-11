import os , time , msvcrt , random

trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodrigez","Laura Hernandez","Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]
plantilla_trabajadores = []


def opc_1():
    limpiar_pantalla()
    print("Asignar sueldos aleatorios.")
    esperar()
    limpiar_pantalla()
    for x in trabajadores:
        nombre=f"{x}"
        sueldo_base= random.randint(300000,2500000)
        desc_salud = (7/100*sueldo_base)
        desc_afp = (12/100*sueldo_base)
        sueldo_liquido = ((desc_afp+desc_salud)-sueldo_base)

        plantilla_trabajador = [nombre,sueldo_base,desc_salud,desc_afp,sueldo_liquido]
        plantilla_trabajadores.append(plantilla_trabajador)

    print("LOS SUELDOS ALEATORIOS SE ASIGNARON A LOS TRABAJADORES CON ÉXITO!")
    esperar()
    tecla_esperar()
    
def opc_2():
    pass
def opc_3():
    pass
def opc_4():
    if len(plantilla_trabajadores) == 0:
        esperar()
        print("No existen sueldos para los trabajadores, porfavor seleccione la opción 1!.")
        esperar()
    else:    
        limpiar_pantalla()
        print("REPORTE DE SUELDOS")
        esperar()
        print(f"{plantilla_trabajadores}")
        tecla_esperar()


def opc_5():
    print("Finalizando programa...")
    esperar()
    print("Desarrollado por Cristóbal Huinca")
    esperar()
    print("RUT 21.827.564-8")
    

def limpiar_pantalla():
    os.system("cls")
def esperar():
    time.sleep(2)
def tecla_esperar():
    print("<<PULSE UNA TECLA PARA CONTINUAR>>")
    msvcrt.getch()