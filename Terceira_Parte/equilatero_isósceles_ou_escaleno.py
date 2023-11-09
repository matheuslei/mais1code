lado1 = float(input("Por favor, insira a medida do primeiro lado: "))
lado2 = float(input("Por favor, insira a medida do segundo lado: "))
lado3 = float(input("Por favor, insira a medida do terceiro lado: "))

if lado1 == lado2 == lado3:
    print("O triângulo é Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é Isósceles")
else:
    print("O triângulo é Escaleno")
