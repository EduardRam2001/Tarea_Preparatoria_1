import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "Ejercicio3"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM divisores;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM divisores')
    conexion.commit()



def main():
    print("Ingrese el numero")
    iden=False
    while (not iden):
        try: 
            num=int(input())
            iden=True
        except ValueError:
            print("Por favor seleccione una opción correcta")
    
    sum=0
    bucle=False
    cont=1
    print("\n")
    print("Los divisores son:")
    while(not bucle):
        if num%cont==0:
             print(str(cont),end=",")
             sum=sum+1
        elif cont>num:
            bucle=True

        cont=cont+1
    print("\n")
    cursor.execute("INSERT INTO divisores(numero,cantidad_divisores) VALUES(%s,%s);" ,(num,sum))
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
    print("1. Pedir Numero")
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