import csv 
from Cuenta import Email 
def modificar_password(cuenta):
    passwordActual_1 = input("Ingrese la contraseña actual: ")
    if passwordActual_1 == cuenta.password:
        cuenta.passwordM = input("Ingrese la contraseña nueva: ")
        cuenta.passwordV = input("Ingrese la contraseña nueva nuevamente: ")
        if cuenta.passwordV == cuenta.passwordM: 
            print("La contraseña se modifico con exito")
        
        else:
            print("La contraseñas no coincide, intente nuevamente")
    
    else:
        print("La contraseña ingresada es incorrecta, ingrese nuevamente")

def crear_email(direccion):
    if "@" not in direccion or "." not in direccion.split("@")[1]:
        print("La direccion de correo electronico es invalida")
        return None
    
    
    idcuenta,dominio,tipo_dominio = direccion.split("@")
    dominio,tipo_dominio = dominio.split(".")
    return Email(idcuenta,dominio,tipo_dominio)


#funcion para contar cuentas de correos 
#realizo el inciso 3

#4a leer archivo separado por comas 10 direccion de email
#crear cuentas correspondiente solo para direcciones validas 
#para novalidas mostrar mensaje error indicando que la direcion de email es incorrecta
def lectura_archivo(archivo):
    with open("fichero.csv", newline="") as csvfile:
        reader = csv.reader(csvfile,delimiter = ',',quotechar = '|')
        for row in reader:
                    
        # se itera por cada fila del archivo
        #accede a cada columna del indice 
        #row es recorrer la lectura del ciclo for 
        #recorre hasta terminada la lista de cada de cada linea
        #join une todos los elementos de cada fila separados con coma
        
            direccion = row[0]
            cuenta = crear_email(direccion)
            
            if cuenta:
                print("Cuenta creada exitosamente para ",direccion)
              
            else:
                print("Error al crear una cuenta para ",direccion)
                  
        
        #termina el modulo de lectura de archivo
    #4b ingresar dominio e indicar cuantos objetos de la clase email tiene igual dominio
    
def cantidad_dominio(email,dominio):
    cant = 0 #se inciara un contador de dominios 
    
    for cuenta in email.cuentas:
        if cuenta.domino == dominio:
            cant+=1
    
    return cant
#definir programa principal 

if __name__== "__main__":
    #crear cuenta  
    nombre = input("Nombre: ") #ingresa nombre
    direccion = input("Direcion de correo electronico: ") #ingresa direccion 
    
    print (f'Estimado {nombre} te enviaremos tus mensajes a la direccion {direccion}') #se imprime un mensaje 
 #se crea una cuenta con el nombre ingresado
    #modificar contraseña e ingresar la actual 
    #debe ser igual a la registrada previamente
    #se debe ingresar nuevamente la nueva contraseña
    
    cuenta = crear_email(direccion)
    """
    Evalua si la cuenta sea diferente de none 
    Es decir que se asegura que haya podido crear una cuenta valida 
    antes de ejecutarlo 
    
    En caso que la cuenta no se haya creado entonces la direccion es invalida
    Su resulta es none (vacio)
    
    Si la cuenta fue creada su resultado es la instancia de la clase email
    """
    if cuenta is not None: 
        modificar_password(cuenta)
    #modificar contraseña e ingresar la actual
    #debe ser igual a la registrada previamente
    #se debe ingresar la nueva contraseña y modificarla
    
    lectura_archivo("fichero.csv")
    
    #termino el punto 4a
    dominio = input("Ingresar dominio:")
    cantidad = cantidad_dominio(cuenta,dominio)
    print(f"La cantidad de correos electronicos que tiene igual dominio al ingresado por teclado es de {cantidad}")
#se termino el punto 4b
