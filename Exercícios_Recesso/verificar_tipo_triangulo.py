def verificar_tipo_triangulo(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        if x == y and y == z:
            tipo = "Triângulo Equilátero"
        elif x == y or x == z or y == z:
            tipo = "Triângulo Isósceles"
        else:
            tipo = "Triângulo Escaleno"
    else:
        tipo = "Não é possível formar um triângulo"
    
    return tipo

x = float(input("Digite o valor do primeiro lado do triângulo: "))
y = float(input("Digite o valor do segundo lado do triângulo: "))
z = float(input("Digite o valor do terceiro lado do triângulo: "))
tipo_triangulo = verificar_tipo_triangulo(x, y, z)
print(f'Tipo de triângulo formado: {tipo_triangulo}')