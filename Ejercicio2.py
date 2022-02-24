import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "Ejercicio2"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM datos;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM datos')
    conexion.commit()



def main():
    print("Ingrese el numero inicial")
    num1=int(input())
    print("Ingrese el numero final")
    num2=int(input())
    print("\n")
    cursor.execute("INSERT INTO datos(numero_inicial,numero_final) VALUES(%s,%s);" ,(num1,num2))
    conexion.commit()
    cont=num1
    conf=False
    while (not conf):
        if cont>=num2:
            conf=True
        if cont<=num2:
            print(str(cont),end=",")
        cont=cont+2
    print("\n")



def pedirnumero():
    Valor=False
    num=0
    while (not Valor):
        try:
            Valor=True
            num=int(input())
        except ValueError:
            print("Por favor seleccion una opcion correcta")
    return num


salir= False
while not salir:
    print("--------MENÚ-----------------")
    print("1. Pedir numero")
    print("2. Ver registro")
    print("3. Elimar datos")
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

print("ADIOS :)")