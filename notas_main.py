from os import system
import os
from estudiante import Estudiante

class NotasMain():

    #listado_estudiantes = []

    def __init__(self):
        self.estudiantes = Estudiante()
        self.menu()

    # Menú para registrar un nuevo estudiante
    def registro_estudiante(self):
        
        system("cls") # Limpiar Ventana
        
        print("\n|------------------ REGISTRO DE CALIFICACIONES ----------------|\n")
        print("|")
        numero_registros = int(input("| - Cuantos registros desea realizar ? : "))
        print("|")
        for n in range(numero_registros):
            print(f"\n|------------------ Estudiante #{n+1} ----------------|\n")
            identificacion = int(input("| > Digite el codigo del Estudiante: "))
            nombre = input("| > Digite su Nombre: ")
            apellido = input("| > Digite su Apellido: ")
            asignatura = input("| > Digite Asignatura: ")
            nota = float(input("| > Ingrese nota: "))
            
            # self.listado_estudiantes.append((identificacion, nombre, apellido, asignatura, nota))
            self.estudiantes.agregarEstudiantes(identificacion, nombre, apellido, asignatura, nota)
            
        # self.listado_estudiantes.clear()


    # Menú para listar estudiantes de la base de datos
    def consultarEstudiantes(self):
        
        system("cls") # Limpiar pantalla
        
        print("\n|------------------------ LISTADO DE ESTUDIANTES ------------------------|\n")
        self.estudiantes.listarEstudiantes()


    # Menú para actualizar datos de los estudiantes
    def actualizar_datos_estudiante(self):
        
        system("cls")
        
        print("\n|------------------ ACTUALIZAR DATOS ----------------|\n")
        
        codigo_estudiante = int(input("| > Digite código del estudiante: "))
        
        print("\n------ Datos Actuales ------\n")
        self.estudiantes.buscarEstudiante(codigo_estudiante)
        
        nueva_nota = float(input(f"\n| > Digite la NUEVA NOTA para Actualizar: "))
        self.estudiantes.actualizarDatos(codigo_estudiante, nueva_nota)


    # Menú para eliminar un registro de la base de datos
    def eliminar_Registro(self):
        system("cls")
        
        print("\n|------------------ ELIMINACION DE REGISTROS ----------------|\n")
        print(" 1. Eliminar UN Registro.")
        print(" 2. Eliminar TODOS los Registros.")
        print(" 3. Volver al Menú Principal")
        opcion = int(input("\n- Por Favor, Digite una Opción: "))
        match opcion:
            case 1:
                system("cls")
                print("\n|------------------ ELIMINACIÓN DE REGISTROS ----------------|\n")
                codigo_eliminar= int(input("\n > Digite el codigo del Estudiante: "))
                print("\n")
                self.estudiantes.buscarEstudiante(codigo_eliminar)
                
                op = input("\n Esta seguro que desea Eliminar este Registro ? s/n : ")
                match op.lower():
                    case 's':
                        self.estudiantes.eliminar_UnRegistro(codigo_eliminar)
                    case 'n':
                        self.eliminar_Registro()
                    case _ :
                        print("\n Opcion no valida.\n")
            case 2:
                system("cls")
                print("\n|------------------ ELIMINACIÓN DE REGISTROS ----------------|\n")
                self.estudiantes.listarEstudiantes()
                
                op = input("\n Esta seguro que desea Eliminar TODOS los Registros ? s/n : ")
                match op.lower():
                    case 's':
                        self.estudiantes.eliminar_TodosRegistros()
                    case 'n':
                        self.eliminar_Registro()
                    case _ :
                        print("\n Opcion no valida.\n")
            case 3:
                system("cls")
                self.menu()
            case _:
                print("\n Opcion no valida.\n")


    # Menú Principal
    def menu(self):
        
        system("cls")
        
        active = True
        
        while (active):
            print("\n|------------------ REGISTRO DE CALIFICACIONES ----------------|\n")
            print(" 1. Registrar Calificaciones de Estudiantes.")
            print(" 2. Consultar Listado de Estudiantes.")
            print(" 3. Actualizar Nota de Estudiante.")
            print(" 4. Eliminar Registros.")
            print(" 5. Salir.\n")
            opcion = int(input(" Por Favor, Digite una Opcion: "))
            
            match opcion:
                case 1:
                    self.registro_estudiante()
                    os.system("pause")
                    system("cls")
                case 2:
                    self.consultarEstudiantes()
                    os.system("pause")
                    system("cls")
                case 3:
                    self.actualizar_datos_estudiante()
                    os.system("pause")
                    system("cls")
                case 4:
                    self.eliminar_Registro()
                    os.system("pause")
                    system("cls")
                case 5:
                    active = False
                    print("Finalizando......")
                case _:
                    print("\n Opcion no valida, Vuelva a intentar.\n")

if __name__ == "__main__":
    NotasMain()