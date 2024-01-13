def contar_divisores(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    
    return count

n = int(input("Digite um valor inteiro e positivo: "))
num_divisores = contar_divisores(n)
print(f'Número de divisores de {n}: {num_divisores}')