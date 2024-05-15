minimo = input(int("inserisci il minimo"))
massimo = input(int("inserisci il massimo"))
somma = 0
lista = []
while minimo < massimo:
    if minimo % 7 == 0:
        lista.append("buzz")
    else: 
        lista.append(minimo)
        somma = somma + minimo
    minimo += 1
print(somma)
print(lista)