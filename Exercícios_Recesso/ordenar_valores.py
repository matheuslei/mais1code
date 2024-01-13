def ordenar_valores(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    
    return a, b, c

a = int(input("Digite o primeiro valor inteiro: "))
b = int(input("Digite o segundo valor inteiro: "))
c = int(input("Digite o terceiro valor inteiro: "))
valores_ordenados = ordenar_valores(a, b, c)
print(f'Valores ordenados: {valores_ordenados}')