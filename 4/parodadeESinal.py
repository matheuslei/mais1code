num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Qual operação você deseja realizar? (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero")
        exit(0)
else:
    print("Operação inválida")
    exit(0)

print(f"Resultado: {resultado}")

if resultado % 2 == 0:
    print("O resultado é par")
else:
    print("O resultado é ímpar")

if resultado > 0:
    print("O resultado é positivo")
elif resultado < 0:
    print("O resultado é negativo")
else:
    print("O resultado é zero")
