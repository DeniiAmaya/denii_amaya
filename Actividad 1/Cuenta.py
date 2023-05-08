import csv #importar libreria
import re 

class Email:
    def __init__(self):
        self.idcuenta = input("ID cuenta de correo: ")
        self.dominio = input("Dominio de correo: ")
        self.tipo_dominio = input("Tipo de dominio: ")
        self.password = input("Contraseña: ")
    
#el constructor se debe declarar los atributos de instancia 
#realiza el ingreso de los atributos por teclado    
    #se creo el constructor como pide el enunciado

    def retornaEmail(self): #retorna el email de los datos ingresados anteriormente
        return f'{self.idcuenta}@{self.dominio}.{self.tipo_dominio}'
    #se retorna la direccion del email 
    #ejemplo facultad_informatica@gmail.com 
    
    def getDominio(self):
        print("El dominio de la cuenta ID es: {self.dominio}")
        return self.dominio
     #se imprime el dominio del retorno de la cuenta
     
     #puede ser hotmail,gmail,yahoo, u otro dominio de correo
    
    def crearCuenta(self,direccion):
        """
        Este metodo es crear una cuenta a partir de la direccion que donde debe estar con el sig formato
        idcuenta@dominio.tipodominio
        """
        if re.match(r"[^@]+@[^@]+\.[^@]+",direccion):
            correo = direccion.split("@") #divide el correo en particiones
    #las particiones se dividen en el  arroba. 
            id_cuenta = correo[0]
            tpodominio = correo[1].split(".")
            dominio = tpodominio[0]
            tpodominio = tp_dominio[1]
            return Email(idcuenta,dominio,tipo_dominio,password)
        
        else: 
            print("Direccion de correo invalida")
            
            #en este apartado debe tener en cuenta
            #que se comprueba que la direccion de correo sea valida
            #si se tiene   @ contenga un arrooba y un punto es una direcicon de correo
        
        