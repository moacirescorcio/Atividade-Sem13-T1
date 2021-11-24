lista_A = []
lista_B = []
lista_C = []
for a in range(25):
    A = int(input())
    lista_A.append(A)

for b in range(25):
    B = int(input())
    lista_B.append(B)

lista_C = lista_A + lista_B
lista_C[::2] = lista_A
lista_C[1::2] = lista_B


print(lista_A)
print(lista_B)
print(lista_C)

