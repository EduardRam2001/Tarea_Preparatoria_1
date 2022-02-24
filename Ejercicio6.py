import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "Ejercicio6"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM Vocales;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM Vocales')
    conexion.commit()


def contarvocales():
    print("Ingrese una palabra")
    frase=input()

    numA=0
    numE=0
    numI=0
    numO=0
    numU=0
    for i in frase:
        if i in "a":
            numA=numA+1
        if i in "e":
            numE=numE+1
        if i in "i":
            numI=numI+1
        if i in "o":
            numO=numO+1
        if i in "u":
            numU=numU+1

    print("A=",numA)
    print("E=",numE)
    print("I=",numI)
    print("O=",numO)
    print("U=",numU)
    print("\n")

    fra=str(frase)

    cursor.execute("INSERT INTO Vocales(palabra,a,e,i,o,u) VALUES(%s,%s,%s,%s,%s,%s);" ,(fra,numA,numE,numI,numO,numU))
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
    print("1. Ingresar palabra")
    print("2. Ver registro")
    print("3. Eliminar datos")
    print("4. Salir")
    print("-----------------------------")
    print("Ingrese una opción")

    opcion=pedirnumero()

    if opcion==1:
        contarvocales()
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

print("Gracias por usar el contador de vocales :)"