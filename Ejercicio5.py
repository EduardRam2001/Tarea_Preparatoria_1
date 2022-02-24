import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "Ejercicio5"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM CantVocales;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM CantVocales')
    conexion.commit()



def contarvocales():
    print("Ingrese una palabra")
    palabra=input()

    contador=0
    for i in palabra:
        if i in "aeiou":
            contador=contador+1
    
    letra=' vocales'
    cantidad=str(contador)+letra
    pal=str(palabra)

    cursor.execute("INSERT INTO CantVocales(palabra,cantidad_vocales) VALUES(%s,%s);" ,(pal,cantidad))
    conexion.commit()
    print("\n")
    print("La palabra",palabra,"tiene",contador, "vocales")
    print("\n")



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

print("Gracias por usar el contador de vocales :)")