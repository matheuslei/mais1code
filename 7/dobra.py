lista_dobrando_while = []
contador_dobrando_while = 1

while contador_dobrando_while <= 1000:
    lista_dobrando_while.append(contador_dobrando_while)
    contador_dobrando_while *= 2

print(lista_dobrando_while)


lista_dobrando_for = []

for contador_dobrando_for in range(11):  # Ajuste para 11 iterações para incluir 1000
    lista_dobrando_for.append(2 ** contador_dobrando_for)

print(lista_dobrando_for[:10])

