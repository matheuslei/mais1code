salario = float(input("Digite o salário do colaborador: "))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5

aumento = salario * percentual / 100
novo_salario = salario + aumento

print(f"Salário antes do reajuste: R$ {salario}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento}")
print(f"Novo salário, após o aumento: R$ {novo_salario}")
