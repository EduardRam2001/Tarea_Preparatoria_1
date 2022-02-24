import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "Ejercicio9"
    )
    print("Conexión exitosa hacia la base de datos \n ")
except psycopg2.Error as e:
     print("Ocurrio un error en la conexión")
     print("Verifique los parametro")

cursor = conexion.cursor()


def Histprial():
    cursor.execute('SELECT*FROM AreaFig;')
    valores=cursor.fetchall()
    print(valores)

def Borradatos():
    cursor.execute('DELETE FROM AreaFig')
    conexion.commit()




def main():
    print("--------Menu-------")
    print("[1]. Area de circulo")
    print("[2]. Area de triangulo")
    print("[3]. Area de cuadrado")
    print("[4]. Area de Rectangulo")
    print("---------------------")
    iden=False
    while (not iden):
        try: 
            op=int(input())
            iden=True
        except ValueError:
            print("Por favor seleccione una opción correcta")

    base=0
    alt=0
    radio=0
    area=0
    val=''
    if op==1:
        print("Ingrese el radio")
        radio=int(input())
        pi=3.141592
        area=radio*radio* pi
        val='Circulo'
        cursor.execute("INSERT INTO AreaFig(figura,dimension1,dimesion2,area) VALUES(%s,%s,%s,%s);" ,(val,radio,pi,area))
        conexion.commit()
    elif op==2:
        print("Ingrese la base")
        base=int(input())
        print("Ingrese la altura")
        alt=int(input())
        area=base*alt/2
        val='Triangulo'
        cursor.execute("INSERT INTO AreaFig(figura,dimension1,dimesion2,area) VALUES(%s,%s,%s,%s);" ,(val,base,alt,area))
        conexion.commit()
    elif op==3:
        print("Ingrese su lado")
        base=int(input())
        area=base*base
        val='Cuadrado'
        cursor.execute("INSERT INTO AreaFig(figura,dimension1,dimesion2,area) VALUES(%s,%s,%s,%s);" ,(val,base,base,area))
        conexion.commit()
    elif op==4:
        print("Ingrese la base")
        base=int(input())
        print("Ingrese la altura")
        alt=int(input())
        area=base*alt
        val='Rectangulo'
        cursor.execute("INSERT INTO AreaFig(figura,dimension1,dimesion2,area) VALUES(%s,%s,%s,%s);" ,(val,base,alt,area))
        conexion.commit()
    print("El",val,"tiene area de:",area)
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
    print("1. Calculadora de Area")
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

print("Gracias por usar la calculadora de area de figuras geometricas")