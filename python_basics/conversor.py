def conversor (tipo_peso, dolar):

 print("Has seleccionado pesos " + tipo_peso)
 valor = int(input("Ingrese el valor: "))
 final_dolar = valor / dolar
 int(final_dolar)
 print("La cantidad de dolares es:")
 print(final_dolar)


menu = """Bienvenido al sistema de conversor de divisas entre Colombia,
Argentina y Mexico :D

1 - COLOMBIA
2 - MEXICO
3 - ARGENTINA"""

print(menu)

pais = int(input("Ingrese el numero segun el pais "))

if pais == 1:
    conversor(tipo_peso= "colombianos", dolar= 4000)
elif pais == 2:
    conversor(tipo_peso="mexicanos", dolar= 20)
elif pais == 3:
    conversor(tipo_peso="argentinos", dolar=50)        
else:
   print("Que monda pusistess")    