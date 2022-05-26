def run():
    
 palabra = input("Ingrese una palabra ")
 palabra = palabra.replace(" ", "")
 palabra = palabra.lower()
 palindromo = palabra[::-1]
 if palabra == palindromo:
  print("es un palindromo")
 else:
    print("no es un palindroo")


if __name__ == "__main__":
 run()
 
 