class Personaje: 
#Atributos de la clase 
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
#Constructor
#Variable del constructor vacío
mi_personaje = Personaje()
#Modificando valores de los atributos
mi_personaje.nombre="EstebanDido"
mi_personaje.fuerza=300
mi_personaje.inteligencia=-2
mi_personaje.defensa=30
mi_personaje.vida=2
print("El nombre de mi personaje es:",mi_personaje.nombre)
print("La fuerza de mi personaje es:",mi_personaje.fuerza)
print("La inteligencia de mi personaje es:",mi_personaje.inteligencia)
print("La defensa de mi personaje es:",mi_personaje.defensa)
print("La vida de mi personaje es:",mi_personaje.vida)
