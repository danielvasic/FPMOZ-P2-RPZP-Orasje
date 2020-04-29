# Rad s listama

lista_1 = []

for i in range(1, 100):
    lista_1.append(i)

# ili jednostavnije
lista_2 = range (1, 100)
#ispis prve liste
for i in lista_1:
    print(i)
#ispis druge liste
for i in lista_2:
    print(i)
# uklanjanje elemenata liste
for i in range(50, 100):
    lista_1.remove(i)
#ispis prve liste
for i in lista_1:
    print(i)

# uklonjeni su elementi od 50 do 100
print()
#skidanje zadnjeg elementa iz liste
print(lista_1.pop())
print(lista_1.pop())
print(lista_1.pop())
# sada će lista ići do 46 (uključno)