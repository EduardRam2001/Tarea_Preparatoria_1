import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "Ejercicio8"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM Impares;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM Impares')
    conexion.commit()



def sumatoria():
    print("Ingrese un numero")
    iden=False
    while (not iden):
        try: 
            num=int(input())
            iden=True
        except ValueError:
            print("Por favor seleccione una opción correcta")

    contador=0
    sumador=0
    verdadero=False


    print("Lon numeros impares son:")
    while(not verdadero):
        contador=contador+1
        if contador>num:
            verdadero=True
        elif contador%2==1:
            sumador=sumador+1
            print(str(contador),end=",")

    print("\n")
    print("El total de numero impares son:")
    print(sumador)
    print("\n")
    cursor.execute("INSERT INTO Impares(numero,cantidad_impares) VALUES(%s,%s);" ,(num,sumador))
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
    print("1. Ingresar numero")
    print("2. Ver registro")
    print("3. Eliminar datos")
    print("4. Salir")
    print("-----------------------------")
    print("Ingrese una opción")

    opcion=pedirnumero()

    if opcion==1:
        sumatoria()
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

print("Gracias por usar la sumatoria de numero")

