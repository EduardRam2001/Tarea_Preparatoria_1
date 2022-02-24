import psycopg2 


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Her_5949",
        dbname = "TresNum"
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
    conf=False
    while (not conf):
        print("------Menú-----")
        print("[1]. Ingresar numeros")
        print("[2]. Salir")
        print("-------------------------")
        print("Seleccione una opción")
        iden=False
        while (not iden):
            try: 
                op=int(input())
                iden=True
            except ValueError:
                print("Por favor seleccione una opción correcta")
        ope= ''
        res=0
        num1=0
        num2=0
        num3=0
        if op==1:
            print("Ingrese el primer numero")
            num1=int(input())
            print("Ingrese el segundo numero")
            num2=int(input())
            print("Ingrese el tercer numero")
            num3=int(input())
            print("-------------------------")
            if num1>num2 and num1>num3:
                ope='Suma'
                res=num1+num2+num3
                print(num1,"+" ,num2,"+" ,num3, "=",res,"\n")
                cursor.execute("INSERT INTO datos(operacion,num1,num2,num3,total) VALUES(%s,%s,%s,%s,%s);" ,(ope,num1,num2,num3,res))
                conexion.commit()

            elif num2>num1 and num2>num3:
                ope='Multiplicacion'
                res=num1*num2*num3
                print(num1,"*" ,num2,"*" ,num3, "=",res,"\n")
                cursor.execute("INSERT INTO datos(operacion,num1,num2,num3,total) VALUES(%s,%s,%s,%s,%s);" ,(ope,num1,num2,num3,res))
                conexion.commit()
            elif num3>num1 and num3>num2:
                ope='Concatenar'
                lcd=str(num1)+str(num2)+str(num3)
                res=int(lcd)
                print(num1,num2,num3,"\n")
                cursor.execute("INSERT INTO datos(operacion,num1,num2,num3,total) VALUES(%s,%s,%s,%s,%s);" ,(ope,num1,num2,num3,res))
                conexion.commit()
            elif num1==num2 and num1==num3 and num2==num3:
                ope='Todos son iguales'
                res=0
                print(num1,"=" ,num2,"=",num3,"\n")
                print("Todos son iguales \n")
                cursor.execute("INSERT INTO datos(operacion,num1,num2,num3,total) VALUES(%s,%s,%s,%s,%s);" ,(ope,num1,num2,num3,res))
                conexion.commit()
        elif op==2:
            conf=True
        else:
            print("Por favor seleccione una opción dentro del menú \n")





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
    print("1. Menu de número")
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