anos = int(input("Digite a quantidade de anos: "))
meses = int(input("Digite a quantidade de meses: "))
dias = int(input("Digite a quantidade de dias: "))

total_dias = anos * 365 + meses * 30 + dias

print(f"A idade expressa em dias é: {total_dias} dias.")