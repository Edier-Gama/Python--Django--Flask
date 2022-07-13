# La abstraccion es el proceso mediante el cual nosotros solo nos
# nos fijamos en los detalles mas relevantes al momento de hacer un
# analisis, esto se logra mediante los metodos privados.

# A continuacion el ejemplo de una lavadora, la lavadora tiene ciertos
# procesos que no nos importan (como usuarios) su funcionamiento, asi que van privados
# (_metodo <--- eso es un metodo privado)


class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura = 'Caliente'):
        self._llenar_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()

        #Los métodos son privados, ya que esta es información que al usuario NO
        # le debería importar como funciona internamente su lavadora.

    def _llenar_agua(self, temperatura):
        print(f'llenando tanque a la siguiente temperatura {temperatura}')

    def _añadir_jabon(self):
        print('Añadiendo Jabón')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('centrifugando la ropa')        

if __name__ == "__main__":
    lavadora = Lavadora()
    lavadora.lavar()