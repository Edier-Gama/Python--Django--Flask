def numeros():

  
    num = (input("Ingresa un numero: "))
    assert num.isnumeric(), "Debes ingresar un NUMERO"
    print(int(num))


def run():

    try:
      num = int(input("Ingresa un numero: "))
      if num < 0:
          return ValueError
      print (f"Tu numero es: {num}")
    except ValueError as ve:
        print(ve)
        print("Solo solo se pueden ingresar numeros positivos")  

    
    
if __name__ == "__main__":
    run()    