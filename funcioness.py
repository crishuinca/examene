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
        sueldo_liquido = (sueldo_base-(desc_afp+desc_salud))

        plantilla_trabajador = [nombre,round(sueldo_base),round(desc_salud),round(desc_afp),round(sueldo_liquido)]
        plantilla_trabajadores.append(plantilla_trabajador)

    print("LOS SUELDOS ALEATORIOS SE ASIGNARON A LOS TRABAJADORES CON ÉXITO!")
    esperar()
    tecla_esperar()
    
def opc_2():
    if len(plantilla_trabajadores) == 0:
        limpiar_pantalla()
        print("No existen sueldos para los trabajadores, porfavor seleccione la opción 1!.")
        tecla_esperar()
    else:
        limpiar_pantalla()
        print("CLASIFICAR SUELDOS")
        esperar()
        limpiar_pantalla()
        for w in plantilla_trabajadores:
            if str({w[1]}) < 8000000:
                menos_800k = menos_800k+1
            elif str({w[1]}) == 800000 and str({w[1]}) < 2000000:
                entre_800y2m = entre_800y2m+1
            elif str({w[1]}) >=2000000:
                mas_2m = mas_2m+1
        print(f"Sueldos menores a $800.000 ={menos_800k}")
        print(f"Sueldos entre $800.000 y $2.000.000 ={entre_800y2m}")
        print(f"Sueldos mayores a $2.000.000 ={mas_2m}")
        tecla_esperar()
def opc_3():
    if len(plantilla_trabajadores) == 0:
        limpiar_pantalla()
        print("No existen sueldos para los trabajadores, porfavor seleccione la opción 1!.")
        tecla_esperar()
    else:
        pass
def opc_4():
    if len(plantilla_trabajadores) == 0:
        limpiar_pantalla()
        print("No existen sueldos para los trabajadores, porfavor seleccione la opción 1!.")
        tecla_esperar()
    else:    
        limpiar_pantalla()
        print("REPORTE DE SUELDOS")
        esperar()
        print("Nombre empleado\t Sueldo Base\t Descuento salud\t Descuento AFP\t Sueldo Liquido\n")
        for z in plantilla_trabajadores:
                print(f"{z[0]}\t\t ${z[1]}\t\t\t ${z[2]}\t\t\t\t ${z[3]}\t\t\t\t ${z[4]}\n")
        esperar()
        print("Los datos tambien se guardaran en un archivo .JSON")
        tecla_esperar()
        limpiar_pantalla()
        with open("reporte_sueldos.json","w",newline="") as archivo:
            archivo.write("Nombre empleado\t Sueldo Base\t Descuento salud\t Descuento AFP\t Sueldo Liquido\n")
            for z in plantilla_trabajadores:
                
                archivo.write(f"{z[0]}\t\t ${z[1]}\t\t\t ${z[2]}\t\t\t\t ${z[3]}\t\t\t\t ${z[4]}\n")
        limpiar_pantalla()
        print("El archivo .JSON fue creado con exito")
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