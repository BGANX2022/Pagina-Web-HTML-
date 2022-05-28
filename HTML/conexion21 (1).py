
import pymysql
import os

# aqui pide el nombre del usuario y lo guarda en una variable nombre
nombre=input("ingrese su nombre: \n ")
edad=int(input("ingrese su edad: \n"))
# aqui imprime la informacion que el usuario metio
print(f"su nombre es {nombre} y tienes {edad} años")
# aqui hacemos una condicion  if para que el usuario
# cumpla con el requisito de la edad minima para entrar
if edad < 12:
    print("no puedes pasar por que eres muy joven")
else:
    print(f"bienvenido {nombre} \t")
    input("Press enter para continuar...")
def menu():
    os.system('cls')
    print("selecciona cualquiera de las siguientes opciones ")
    print("\t1 - primera opción  insertar datos a la tabla datos")
    print("\t2 - segunda opción mostar datos de la tabla datos")
    print("\t3 - tercera opción")
    print("\t9 - salir")
while True:
    menu()
    opcionmenu = input("ingrese una de las opciones ")
    if opcionmenu == "1":
        print("")
        import pymysql
 
        conexion = pymysql.connect(host='localhost',
                             user='cristian',
                             password='nomelase',
                             db='formulario')
 
        mycursor = conexion.cursor()
 
        sql = "INSERT INTO datos (nombres,apellidos,direccion,telefono,correo) VALUES (%s, %s, %s, %s, %s)"
        nombres = input("inserte el nombre: ")
        apellidos = input("inserte el apellido: ")
        direccion = input("Ingrese su direccion de domicilio: ")
        telefono = int(input("inserte el numero de telefono: "))
        correo = input("Ingrese su correo electronico: ")
 
        mycursor.execute(sql, (nombres, apellidos, direccion, telefono, correo))
 
        conexion.commit()
 
        print(mycursor.rowcount, "Registro insertado correctamente.")
        input("Has pulsado la opción 1...\npulsa una tecla para continuar")
    elif opcionmenu == "2":
        print("")
        import pymysql
 
        conn = pymysql.connect(host='localhost', port=3306, user='cristian', passwd='nomelase', db='formulario')
 
        cur = conn.cursor()
        cur.execute("SELECT * FROM datos")
 
        print(cur.description)
        print()
 
        for row in cur:
            print(row)
 
        cur.close()
        conn.close()
        input("Has pulsado la opción 2...\npulsa una tecla para continuar")
    elif opcionmenu == "3":
        print("")
        input("Has pulsado la opción 3...\npulsa una tecla para continuar")
    elif opcionmenu == "9":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")



Grant all on  *.*  to 'bgam'e'localhost'  IDENTIFIED  BY 'D1s3t3c0m' WITH GRANT OPTION;
