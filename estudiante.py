import sqlite3

class Estudiante :

    def __init__(self):
        pass


    # Método para crear la Base de datos
    def crearBD(self):
        conexionDB = sqlite3.connect("estudiantes.db")
        conexionDB.commit()
        conexionDB.close()


    # Método para crear tabla
    def crearTabla(self):
        conexionDB = sqlite3.connect("estudiantes.db")
        
        cursor = conexionDB.cursor()
        
        cursor.execute(
            '''CREATE TABLE notas_estudiantes(
                codigo integer PRIMARY KEY,
                nombre varchar(20),
                apellido varchar(20),
                asignatura varchar(30),
                nota float
            )'''
        )
        
        conexionDB.commit()
        conexionDB.close()


    # Método para registrar un nuevo estudiantes
    def agregarEstudiantes(self, codigo, nombre, apellido, asignatura, nota):
        conexionDB = sqlite3.connect("estudiantes.db")
        
        cursor = conexionDB.cursor()
        
        instruccion = f"INSERT INTO notas_estudiantes VALUES({codigo}, '{nombre}', '{apellido}', '{asignatura}', {nota})"
        try:
            cursor.execute(instruccion)
            print("\n|---------------**** REGISTRO EXITOSO ****--------------------|\n")
        except:
            print(f"\n *** FATAL ERROR, CODIGO {codigo} YA EXISTENTE ***\n")
        conexionDB.commit()
        conexionDB.close()


    # Método para mostrar todos los registros de la base de datos
    def listarEstudiantes(self):
        conexionDB = sqlite3.connect("estudiantes.db")
        
        cursor = conexionDB.cursor()
        
        instruccion = "SELECT * FROM notas_estudiantes"
        cursor.execute(instruccion)
        
        datos = cursor.fetchall()
        
        conexionDB.commit()
        conexionDB.close()
        
        for estudiante in datos :
            print(f"| {estudiante[0]} | \t | {estudiante[1]} | \t | {estudiante[2]} | \t | {estudiante[3]} | \t | {estudiante[4]} |\n")


    # Método para buscar un estudiante por su codigo en la base de datos
    def buscarEstudiante(self, identificacion):
        conexionDB = sqlite3.connect("estudiantes.db")
        
        cursor = conexionDB.cursor()
        
        instruccion = f"SELECT * FROM notas_estudiantes WHERE codigo = {identificacion}"
        cursor.execute(instruccion)
        
        datos_encontrados = cursor.fetchall()
        
        conexionDB.commit()
        conexionDB.close()
        
        for estudiante in datos_encontrados :
            print(f"| {estudiante[0]} | \t | {estudiante[1]} | \t | {estudiante[2]} | \t | {estudiante[3]} | \t | {estudiante[4]} |\n")

    # Método para actualizar los datos de la base de datos
    def actualizarDatos(self, identificacion, nueva_nota):
        conexionDB = sqlite3.connect("estudiantes.db")
        
        cursor = conexionDB.cursor()
        
        instruccion = f"UPDATE notas_estudiantes SET nota = {nueva_nota} WHERE codigo = {identificacion}"
        cursor.execute(instruccion)
        
        instruccion = f"SELECT * FROM notas_estudiantes WHERE codigo = {identificacion}"
        cursor.execute(instruccion)
        
        datos_encontrados = cursor.fetchall()
        
        conexionDB.commit()
        conexionDB.close()
        
        print("\n ----------- DATOS ACTUALIZADOS -----------\n")
        for estudiante in datos_encontrados :
            print(f"| {estudiante[0]} | \t | {estudiante[1]} | \t | {estudiante[2]} | \t | {estudiante[3]} | \t | {estudiante[4]} |\n")


    # Método para eliminar un solo registro por la identificacion del estudiante
    def eliminar_UnRegistro(self, identificacion):
        conexionDB = sqlite3.connect("estudiantes.db")
        
        cursor = conexionDB.cursor()
        
        instruccion = f"DELETE FROM notas_estudiantes WHERE codigo = {identificacion}"
        cursor.execute(instruccion)
        
        conexionDB.commit()
        conexionDB.close()
        
        print("\n**** REGISTRO ELIMINADO CON EXITO ****\n")
    
    
    # Método para eliminar Todos los registros de la base de datos
    def eliminar_TodosRegistros(self):
        conexionDB = sqlite3.connect("estudiantes.db")
        
        cursor = conexionDB.cursor()
        
        instruccion = f"DELETE FROM notas_estudiantes"
        cursor.execute(instruccion)
        
        conexionDB.commit()
        conexionDB.close()
        
        print("\n**** REGISTROS ELIMINADOS CON EXITO ****\n")
