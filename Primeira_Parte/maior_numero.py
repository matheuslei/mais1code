num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior_numero = num1

if num2 > maior_numero:
    maior_numero = num2
if num3 > maior_numero:
    maior_numero = num3

print(f"O maior número é: {maior_numero}")
