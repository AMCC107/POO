class Personaje: 
    def __init__(self, nombre, fuerza, inteligencia, defensa,vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
#Pregunta de examen ¿Qué es self en programación? R= Es una referencia al mismo objeto
#¿Qué es el método init? R= Constructor  que inicializa atributos de un objeto
#¿Por qué se usa dobre guión bajo para init? R= Dunder. Método especial de Python, método mágico, predefinido por python
#¿Cuándo se ejecuta el método init? R= Se ejecuta automáticamente al crear un objeto
#signo de igual es asignar una variable
#Atributos de la clase 
    #nombre = 'Default'
    #fuerza = 0
    #inteligencia = 0
    #defensa = 0
    #vida = 0
    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:",self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)
    def subir_nivel(self,fuerza, inteligencia, defensa):
        self.fuerza=self.fuerza+fuerza
        #self.fuerza+=fuerza
        self.inteligencia=self.inteligencia+inteligencia
        self.defensa=self.defensa+defensa
    def esta_vivo(self):
        return self.vida > 0
    def morir(self):
        self.vida=0
        print(self.nombre, "ha muerto")
    def dañar(self, enemigo):
        daño = self.fuerza - enemigo.defensa
        return max(daño, 0)
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("Vida de", enemigo.nombre, "es", enemigo.vida)
class Guerrero(Personaje):
    #sobreescribir el constructor
    def __init__(self,nombre,fuerza,inteligencia,defensa, vida,espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada=espada
    #sobreescribir impresión de atributos 
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada:", self.espada)
#El mismo método puede tener un comportamiento diferente dependiendo del objeto que lo llame
#sobreescribir el cálculo del daño 
    def dañar (self,enemigo):
        return self.fuerza*self.espada - enemigo.defensa
#Escoger navaja
    def escoger_navaja (self):
        opcion=int(input ("Escoge la navaja de la muerte:\n(1) Navaja Suiza,daño 10.\n(2)Navaja pioja,daño 6.\n>>>>>>"))
        if (opcion==1):
            self.espada=10
        elif (opcion==2):
            self.espada=6
        else: 
            print("Valor inválido, intente nuevamente")
    #vuelva ejecutar el método escoger_navaja
            self.escoger_navaja()
class Mago(Personaje):
    #sobreescribir el constructor
    def __init__(self,nombre,fuerza,inteligencia,defensa, vida,libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro=libro
    #sobreescribir impresión de atributos 
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Libro:", self.libro)
#El mismo método puede tener un comportamiento diferente dependiendo del objeto que lo llame
#sobreescribir el cálculo del daño 
    def dañar (self,enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
#Escoger navaja
    def escoger_libro (self):
        opcion=int(input ("Escoge el libro de la muerte:\n(1) el principito,daño 10.\n(2) Crepusculo,daño 6.\n>>>>>>"))
        if (opcion==1):
            self.libro=10
        elif (opcion==2):
            self.libro=6
        else: 
            print("Valor inválido, intente nuevamente")
    #vuelva ejecutar el método escoger_navaja
            self.escoger_navaja()

persona=Personaje ("Angel Suárez",12,3000,2,100)
arturoSuarez=Guerrero("Arturo Suarez",12,3000,2,100,.5)
Gandalf= Mago("Gandalf",12,300,2,100,5)
arturoSuarez.escoger_navaja()
arturoSuarez.imprimir_atributos()
#Atributos antes de la trajedia 
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
Gandalf.imprimir_atributos()
#Ataques sin piedad 
persona.atacar(arturoSuarez)
arturoSuarez.atacar(Gandalf)
Gandalf.atacar(persona)
#Atributos después de la trajedia 
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
Gandalf.imprimir_atributos()
#print("El valor de espada es:", arturoSuarez.espada)

#Constructor
#Variable del constructor 
#mi_personaje = Personaje("EsteBandido", 140,50,45,100)
#mi_enemigo=Personaje("Ángel",70,100,40,100)
#mi_personaje.imprimir_atributos() 
#mi_personaje.atacar(mi_enemigo)
# mi_personaje.subir_nivel(15,5,10)
# print("Valores actualizados")
# mi_personaje.imprimir_atributos()
#Modificando valores de los atributos
# mi_personaje.nombre="EstebanDido"
# mi_personaje.fuerza=300
# mi_personaje.inteligencia=-2
# mi_personaje.defensa=30
# mi_personaje.vida=2
# print("El nombre de mi personaje es:",mi_personaje.nombre)
# print("La fuerza de mi personaje es:",mi_personaje.fuerza)
# print("La inteligencia de mi personaje es:",mi_personaje.inteligencia)
# print("La defensa de mi personaje es:",mi_personaje.defensa)
# print("La vida de mi personaje es:",mi_personaje.vida)
