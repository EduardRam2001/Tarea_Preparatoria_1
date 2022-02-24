import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "Ejercicio12"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM factorial;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM factorial')
    conexion.commit()

def main():
    num=0
    res=''
    print("Ingrese un numero")
    iden=False
    while (not iden):
        try: 
            num=int(input())
            iden=True
        except ValueError:
            print("Por ingrese un numero valido")


    if num%7==0:
        contador=0
        mult=1
        verdadero=False
        while(not verdadero):
            contador=contador+1
            if contador<=num:
                mult=mult*contador
            elif contador>num:
                verdadero=True
        print("El numero es divisible dentro de 7")
        print("Su factorial es:",mult)
        res='Es divisible dentro de 7'
    else:
        print("El numero no es divisible dentro de 7 ")
        res='No es divisible dentro de 7'
        mult=0
    cursor.execute("INSERT INTO factorial(numero,estado,factorial) VALUES(%s,%s,%s);" ,(num,res,mult))
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