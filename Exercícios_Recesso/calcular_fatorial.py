def calcular_fatorial(n):
    if n == 0 or n == 1:
        fatorial = 1
    else:
        fatorial = n * calcular_fatorial(n-1)
    
    return fatorial

n = int(input("Digite um valor inteiro e positivo: "))
fatorial = calcular_fatorial(n)
print(f'O fatorial de {n} é: {fatorial}')