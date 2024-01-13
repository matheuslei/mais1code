def encontrar_divisores(n):
    divisores = []
    for i in range(1, n+1):
        if n % i == 0:
            divisores.append(i)
    
    return divisores

n = int(input("Digite um valor inteiro e positivo: "))
divisores = encontrar_divisores(n)
print(f'Divisores de {n}: {divisores}')