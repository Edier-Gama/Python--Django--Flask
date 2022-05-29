class personaje:
    nombre = 'Edier'
    fuerza = 1000
    inteligencia = 4000
    defensa = 200
    vida = 1287
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
    def atributos(self):
        
        print(self.nombre, ':')
        print('Fuerza :', self.fuerza)    
        print('Inteligencia :', self.inteligencia)    
        print('Defensa :', self.defensa)    
        print('Vida :', self.vida)  
    
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def esta_vivo(self):
        
        return self.vida > 0          
            
            
mi_personaje = personaje("Luisito Comunica", 200, 344, 888, 0)
print(mi_personaje.esta_vivo())