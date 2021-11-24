lista1 = []
par = []
impar = []
for i in range(20):
    n = int(input())
    lista1.append(n)

for i in lista1:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(lista1)
print(par)
print(impar)
