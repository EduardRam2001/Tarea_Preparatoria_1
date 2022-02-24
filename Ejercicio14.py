import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "Ejercicio14"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM Carros;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM Carros')
    conexion.commit()



def carros():
    print("Ingrese el modelo del carro")
    iden=False
    while (not iden):
        try: 
            año=int(input())
            iden=True
        except ValueError:
            print("Por ingrese un modelo de carro valido")

    print("Ingrese el kilometraje")

    buc=False
    while (not buc):
        try: 
            kim=int(input())
            buc=True
        except ValueError:
            print("Por ingrese un kilometraje valido")
    
    esta=''
    if año<2007 and kim>20000:
        esta='Renovación'
        print("El carro debe renovarse")
    elif  año>=2007 and año<=2013 and kim==20000:
        esta='Mantenimiento'
        print("El carro debe tener mantenimiento")
    elif año>2013 and kim<10000:
        esta='Optimas condiciones'
        print("El carro esta en optimas condiciones")
    else:
        esta='Mecánico'
        print("Mecánico")
    print("\n")

    cursor.execute("INSERT INTO Carros(modelo,kilometraje,estado) VALUES(%s,%s,%s);" ,(año,kim,esta))
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
    print("1. Ingresar información del carro")
    print("2. Ver registro")
    print("3. Eliminar datos")
    print("4. Salir")
    print("-----------------------------")
    print("Ingrese una opción")

    opcion=pedirnumero()

    if opcion==1:
        carros()
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