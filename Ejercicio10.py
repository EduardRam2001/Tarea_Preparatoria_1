import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "Ejercicio10"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM Triangulo;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM Triangulo')
    conexion.commit()

def main():
    lado1=0
    lado2=0
    lado3=0

    print("Ingrese lado 1")
    iden=False
    while (not iden):
        try: 
            lado1=int(input())
            iden=True
        except ValueError:
            print("Por favor seleccione una opción correcta")

    print("Ingrese lado 2")
    ident=False
    while (not ident):
        try: 
            lado2=int(input())
            ident=True
        except ValueError:
            print("Por favor seleccione una opción correcta")

    print("Ingrese lado 3")
    identi=False
    while (not identi):
        try: 
            lado3=int(input())
            identi=True
        except ValueError:
            print("Por favor seleccione una opción correcta")

    triangulo=''
    if lado1!=lado2 and lado1!=lado3:
        triangulo='Escaleno'
    elif lado1==lado2 and lado1==lado3:
        triangulo='Equilátero'
    else:
        triangulo='Isósceles'
    print("Lado1=",lado1,",lado2=",lado2,", lado3=",lado3,", es un trinagulo:",triangulo)
    print("\n")
    cursor.execute("INSERT INTO Triangulo(figura,lado1,lado2,lado3) VALUES(%s,%s,%s,%s);" ,(triangulo,lado1,lado2,lado3))
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
    print("1. Ingresar lados del triangulo")
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