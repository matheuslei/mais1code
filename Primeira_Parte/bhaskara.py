a = float(input("Digite o coeficiente 'a': "))
b = float(input("Digite o coeficiente 'b': "))
c = float(input("Digite o coeficiente 'c': "))

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    x = -b / (2*a)
    print(f"A equação possui uma raiz real: x = {x}")
else:
    x1 = (-b + (delta)**0.5) / (2*a)
    x2 = (-b - (delta)**0.5) / (2*a)
    print(f"A equação possui duas raízes reais: x1 = {x1} e x2 = {x2}")
