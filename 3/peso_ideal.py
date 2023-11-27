altura = float(input("Por favor, insira sua altura em metros: "))
sexo = input("Por favor, insira seu sexo (M para masculino, F para feminino): ")

# Calcula o peso ideal
if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

print("Seu peso ideal é: ", peso_ideal, "kg")