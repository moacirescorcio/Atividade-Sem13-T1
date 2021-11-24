n = int(input("Insira um valor: "))
lista1 = []
lista2 = []
lista3 = []
lista4 = []
if n > 0:
    #Letra a
    for a in range(1, n+1):
        lista1.append(a*0)

    print(lista1)

    #Letra b
    for b in range (1, n+1):
        lista2.append(b)

    print(lista2)

    #Letra c
    for c in range(n):
        z = int(input("Insira um valor: "))
        lista3.append(z)
    print(lista3)

    #Letra d
    for d in range(n):
        i = int(input("Insira um valor: "))
        lista4.insert(0, i)

    print(lista4)

else:
    for d in range(4):
        print(lista1)



