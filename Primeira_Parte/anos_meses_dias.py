dias = int(input("Digite a quantidade de dias: "))

anos = dias // 365
dias_restantes = dias % 365

meses = dias_restantes // 30
dias_restantes = dias_restantes % 30

print(f"A idade expressa em anos, meses e dias é: {anos} anos, {meses} meses e {dias_restantes} dias.")
