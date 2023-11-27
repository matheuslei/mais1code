peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo biológico (M/F): ")

imc = peso / (altura ** 2)

if sexo.upper() == "M":
    if imc < 20:
        classificacao = "Magreza"
    elif imc < 25:
        classificacao = "Normal"
    elif imc < 30:
        classificacao = "Obesidade leve"
    elif imc < 40:
        classificacao = "Obesidade moderada"
    else:
        classificacao = "Obesidade mórbida"
elif sexo.upper() == "F":
    if imc < 19:
        classificacao = "Magreza"
    elif imc < 24:
        classificacao = "Normal"
    elif imc < 29:
        classificacao = "Obesidade leve"
    elif imc < 39:
        classificacao = "Obesidade moderada"
    else:
        classificacao = "Obesidade mórbida"
else:
    print("Sexo inválido")
    exit(0)

print(f"IMC: {imc}")
print(f"Classificação: {classificacao}")
