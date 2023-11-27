valor1 = int(input("Por favor, insira o primeiro valor: "))
valor2 = int(input("Por favor, insira o segundo valor: "))
valor3 = int(input("Por favor, insira o terceiro valor: "))

if valor1 <= valor2 and valor1 <= valor3:
    menor = valor1
    if valor2 <= valor3:
        meio = valor2
        maior = valor3
    else:
        meio = valor3
        maior = valor2
elif valor2 <= valor1 and valor2 <= valor3:
    menor = valor2
    if valor1 <= valor3:
        meio = valor1
        maior = valor3
    else:
        meio = valor3
        maior = valor1
else:
    menor = valor3
    if valor1 <= valor2:
        meio = valor1
        maior = valor2
    else:
        meio = valor2
        maior = valor1

print("Os valores em ordem crescente são: ", menor, meio, maior)
