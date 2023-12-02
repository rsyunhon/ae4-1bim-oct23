#from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import Column, Integer, String
# se importa el engine
from base_datos import engine

# se crea la clase llamada Base que permite definir las clases bajo las
# características de SQLAlchemy
# Base = declarative_base()

db = engine.matriculas
coleccion = db.matriculaEstudiante

continuar=True

while continuar:
    strIdentificacion= input("Ingrese su numero de identificacion: ")
    strNombreApellido= input("Ingrese su nombre y apellido: ")
    strCarrera=input("Ingrese su carrera: ")
    strUniversidad=input("Ingrese el nombre de su universidad: ")

    #infodata = {"identificacion": strIdentificacion,"nombres": strNombreApellido, "carrera": strCarrera, "universidad" : strUniversidad}
    #coleccion.insert_one(infodata)
    infodata = {"identificacion": strIdentificacion,"nombres": strNombreApellido, "carrera": strCarrera, "universidad" : strUniversidad}
    coleccion.insert_one(infodata)

    validar=input("Desea agregar mas informacion s/n: ")
    if  validar.lower()=="n":
        continuar=False
    else:
        continuar=True

dataInput= coleccion.find()

for registro in dataInput:
    print(registro)

print("\n\n\n")

#
#
#
#

coleccionVehiculos = db.matriculaVehiculos

continuarVehiculo=True

while continuarVehiculo:
    strPlaca= input("Ingrese su Placa: ")
    strMarca= input("Ingrese su Marca: ")
    strModelo=input("Ingrese su Modelo: ")    
    strOcupantes=input("Ingrese el cant ocupantes: ")

    infodata = {"Placa": strPlaca,"Marca": strMarca, "Modelo": strModelo, "Cantidad_Ocupantes" : strOcupantes}
    coleccionVehiculos.insert_one(infodata)

    validar=input("Desea agregar mas informacion s/n: ")
    if  validar.lower()=="n":
        continuarVehiculo=False
    else:
        continuarVehiculo=True
        #infodata = {"Placa": strPlaca,"Marca": strMarca, "Modelo": strModelo, "Cantidad_Ocupantes" : strOcupantes}
        #coleccionVehiculos.insert_one(infodata)

dataVehiculo= coleccionVehiculos.find()

for registroVehiculo in dataVehiculo:
    print(registroVehiculo)

print("\n\n\n")




#print("Su identificacion es: ",strIdentificacion, "\nSu Nombres y Apellidos: ", strNombreApellido,"\nPertenece a la carrera: ",strCarrera,"\nDe la universidad ",strUniversidad)

'''
# Se crea la una entidad llamada Autor, que hereda
# de Base
class Ciudad(Base):
    __tablename__ = 'ciudad' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    nombreCiudad = Column(String) # atributo de tipo String
    pais = Column(String)
    poblacion = Column(Integer)

    def __str__(self):
        return "%s %s %sgit  " % (self.nombreCiudad, self.pais, self.poblacion)


class Estadio(Base):
    __tablename__ = 'estadio' # El nombre de la entidad en sqlite
    # Se definen los atributos
    id = Column(Integer, primary_key=True) # este atributo es entero y
                                        # se lo considera como llave
                                        # primaria
    nombreEstadio = Column(String) # atributo de tipo String
    direccionEstadio = Column(String)
    capacidad = Column(Integer)

    def __str__(self):
        return "%s %s %s " % (self.nombreEstadio, self.direccionEstadio,  self.capacidad)


# Sentencia que permite crear o migrar las clases en Python al
# gestor de base de datos, expresado en el engine.
Base.metadata.create_all(engine)
'''