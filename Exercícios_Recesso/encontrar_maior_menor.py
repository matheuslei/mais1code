def encontrar_maior_menor():
    valores = []
    for i in range(50):
        valor = int(input("Digite um valor: "))
        valores.append(valor)
    
    maior = max(valores)
    menor = min(valores)
    
    return maior, menor

maior_menor = encontrar_maior_menor()
print(f'Maior valor: {maior_menor[0]}')
print(f'Menor valor: {maior_menor[1]}')