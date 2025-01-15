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

#Constructor
#Variable del constructor 
mi_personaje = Personaje("EsteBandido", 140,50,45,100)
mi_enemigo=Personaje("Ángel",70,100,40,100)
mi_personaje.imprimir_atributos() 
mi_personaje.atacar(mi_enemigo)
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
