import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "Ejercicio4"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM Mayor_Menor;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM Mayor_Menor')
    conexion.commit()



def main():
    print("Ingrese el primer numero")
    iden=False
    while (not iden):
        try: 
            num1=int(input())
            iden=True
        except ValueError:
            print("Por favor seleccione una opción correcta")
    print("Ingrese el segundo numero")
    ident=False
    while (not ident):
        try: 
            num2=int(input())
            ident=True
        except ValueError:
            print("Por favor seleccione una opción correcta")


    print("\n")
    print("Lista de numero desde el mayor al menor")
    if num1>num2:
        cont=num1
        corr=False
        while (not corr):
            if cont>=num2:
                print(str(cont),end=",")
            elif cont<num2:
                corr=True
            cont=cont-1
        print("\n")
        cursor.execute("INSERT INTO Mayor_Menor(numero1,numero2,mayor,menor) VALUES(%s,%s,%s,%s);" ,(num1,num2,num1,num2))
        conexion.commit()

    if num2>num1:
        cont=num2
        corr=False
        while (not corr):
            if cont>=num1:
                print(str(cont),end=",")
            elif cont<num1:
                corr=True
            cont=cont-1
        print("\n")
        cursor.execute("INSERT INTO Mayor_Menor(numero1,numero2,mayor,menor) VALUES(%s,%s,%s,%s);" ,(num1,num2,num2,num1))
        conexion.commit()



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
    print("1. Ingresar numeros")
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