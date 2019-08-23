from pymongo import MongoClient
from random import uniform, randrange
#driver de coneccion mysql y especificacion de base de datos a usar; Librerias a usar


mongodb_connection = MongoClient(port=27017)
db = mongodb_connection.Notas
#expecificacion de puerto; conexion a la base de datos


def Nombres():
    VNom=['Jose','Luis','Angel','Roy','Andres','Juan','Pedro','Joel','Mario','Geremias','Elias','Abraham','Isaias','Jesus','Abelardo','Pepe','Carlos','Diego','Javier','Jacob','Moises','Merlin','Antonio','Agustin','Pablo','Sacarias','Daniel','David','Eladio','Hermenejildo','Manuel','Mateo','Leopoldo','Marcos','Martin','Leonidas','Erodes',
          'Ana','Elizabeth','Juana','Tereza','Delia','Maribel','Luz','Sandra','Rosa','Evelyn','Alis','Tina','Margarita','Vielca','Zuleika','Violeta','Lilibeth','Betty','Betzaida','Beatriz','Elsa','Olga','Lesly','Paula','Esther','Paola','Maria','Maruquel','Maite','Laura','Clementina','Delfina','Marta','Mabdalena','Diana','Chelin','Dunia']
    return VNom[randrange(0,len(VNom))]
#Definicion de nombres para registro aleatorio


def Apellidos():
    VApell=['Gomez','Hudson', 'Fernandez', 'Castaño', 'Morales', 'Alcedo','Parodi','Torres', 'Aguilar', 'Sauco', 'Mangano', 'Ruiz', 'Aragon','Candon', 'Acosta', 'Cabeza', 'Soto', 'Ezequiel', 'Pericacho', 'Rodriguez','Garcia','Laso','Espinoza','Morales','Samaniego','Calderon','Hudson','Ospina','Aleman','Varela','Carrion','Rojas','Alvarado',
            'Cañizales','Vega','Lopez','Miranda','Zuñiga','Salsedo']
    return VApell[randrange(0, len(VApell))]
# Definicion de apellidos para registro aleatorio


def Notas_():
    return ("{0:.2f}".format(uniform(0, 100)))
#Definicion de notas para registro aleatorio


print("Conexion exitosa")
for x in range(1, 1000001):
    Nombre = Nombres()
    Apellido = Apellidos()
    Nota = Notas_()
    Registro = {'Nombre' : Nombre, 'Apellido' : Apellido, 'Nota' : Nota}
    Insertar = db.estudiante.insert_one(Registro)
    print('Creando {0} de 1,000,000 como {1}'.format(x,Insertar))

print('He terminado Con Exito!!!')
#Introduccion formal de datos aleatorios en la base de datos



Nota_maxima = db.estudiante.find().sort("Nota",-1).limit(1)
for x in Nota_maxima:
  print(x)
#Consulta para saber la nota mas alta encontrada



Borrador = db.estudiante.drop()
print("Registros borrados con exito quedaron",Borrador ," Archivos")
#Borra todos los registros de mi Tabla