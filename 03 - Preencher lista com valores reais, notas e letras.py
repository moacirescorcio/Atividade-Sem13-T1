n = int(input())
lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []

#Letra a
for i in range (n):
    i = float(input())
    lista1.insert(0, i)

print(lista1)

#Letra b
if n == 0:
    print(lista2)
    print('SEM NOTAS')
    
else:
    for j in range (n):
        j = float(input())
        lista2.append(j)
    print(lista2)
    print(f'{sum(lista2) / len(lista2):.1f}')

#Letra c
for k in range(n):
    y = input()[0]
    lista4.append(y)

qtd = 0
for a in lista4:
    if a in 'AaEeIiOoUu':
        qtd += 1
    else:
        lista5.append(a)

print(qtd)
print(lista5)