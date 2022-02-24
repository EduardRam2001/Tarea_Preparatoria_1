import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "Ejercicio11"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM notas;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM notas')
    conexion.commit()

def main():
    nota1=0
    nota2=0
    nota3=0
    prome=0
    apr=''
    print("Ingrese la primera nota")
    iden=False
    while (not iden):
        try: 
            nota1=int(input())
            iden=True
        except ValueError:
            print("Por ingrese una nota valida")

    print("Ingrese la segunda nota")
    ident=False
    while (not ident):
        try: 
            nota2=int(input())
            ident=True
        except ValueError:
            print("Por ingrese una nota valida")

    print("Ingrese la tercera nota 3")
    identi=False
    while (not identi):
        try: 
            nota3=int(input())
            identi=True
        except ValueError:
            print("Por ingrese una nota valida")

    prome=(nota1+nota2+nota3)/3

    if prome>=60:
        apr='Aprobado'
        print("Su promedio es:",prome)
        print("Usted a",apr)
    else: 
        apr='Reprobado'
        print("Su promedio es:",prome)
        print("Usted a",apr)
    cursor.execute("INSERT INTO notas(nota1,nota2,nota3,promedio ,estado) VALUES(%s,%s,%s,%s,%s);" ,(nota1,nota2,nota3,prome,apr))
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
    print("1. Ingresar notas")
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