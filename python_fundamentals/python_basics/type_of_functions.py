# Campana sobre campanaaa y funcion sobre funcioooooon xD

"""Funciones como objetos de primera-clase"""

# Estas funciones reciben como parámetro a otra funcion, y la
# retornan

def run():

 def saludar(nombre):
    return print(f"Hola, {nombre} estudiemos python")

 def funcion_sobre_funcion(saludar):
   return saludar('Edier')

 # funcion_sobre_funcion(saludar)

"""Funciones anidadas"""

def anuncios():
    print("Soy la funcion mayor y soy indispensable para correr los anuncios")

    def anuncio_1():
        print("Hola, soy el anuncio 1")

    def anuncio_2():
        print('soy el anuncio 2')

    anuncio_1()
    anuncio_2()    

# Para acceder a los anuncios primero debo acceder a la funcion anuncio()
# ya que estos anuncios estan anidados DENTRO de anuncios()
# el scope de estas variables es limitado         






if __name__ == "__main__":
  run()
  anuncios()

  