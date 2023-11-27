num_lados = int(input("Por favor, insira o número de lados do polígono: "))
medida_lado = float(input("Por favor, insira a medida do lado (em cm): "))

if num_lados == 3:
    area = (medida_lado ** 2) * (3 ** 0.5) / 4
    print("TRIÂNGULO, Área: ", area, "cm^2")
elif num_lados == 4:
    area = medida_lado ** 2
    print("QUADRADO, Área: ", area, "cm^2")
elif num_lados == 5:
    print("PENTÁGONO")
else:
    print("Polígono não suportado")
