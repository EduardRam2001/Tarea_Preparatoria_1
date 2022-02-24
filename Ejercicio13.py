import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "Ejercicio13"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM Bisiesto;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM Bisiesto')
    conexion.commit()


def main():
    print("Ingrese el año")
    iden=False
    while (not iden):
        try: 
            año=int(input())
            iden=True
        except ValueError:
            print("Por ingrese un año valido y con numeros")
    
    bis=''

    if año % 4 != 0: 
        print("El año",año,"no es bisiesto")
        bis='No es bisiesto'
    elif año % 4 == 0 and año % 100 != 0: 
        print("El año",año,"es bisiesto")
        bis='Es bisiesto'
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
        print("El año",año,"no es bisiesto")
        bis='No es bisiesto'
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
        print("El año",año,"es bisiesto")
        bis='Es bisiesto'
    print("\n")
    cursor.execute("INSERT INTO Bisiesto(año,estado) VALUES(%s,%s);" ,(año,bis))
    conexion.commit()




def pedirnumero():
    Valor=False
    op=0
    while (not Valor):
        try:
            Valor=True
            op=int(input())
        except ValueError:
            print("Por favor seleccion una opcion correcta")
    return op

salir= False
while not salir:
    print("--------MENÚ-----------------")
    print("1. Ingresar año")
    print("2. Ver registro")
    print("3. Eliminar datos")
    print("4. Salir")
    print("-----------------------------")
    print("Ingrese una opción")

    opcion=pedirnumero()

    if opcion==1:
        main()
    elif opcion==2:
        Histprial()
    elif opcion==3:
        Borradatos()
    elif opcion==4:
        salir=True
    else:
        print("Por favor ingrese un número que este en el menú \n")

cursor.close()
conexion.close()  

print("Gracias por usar el programa")