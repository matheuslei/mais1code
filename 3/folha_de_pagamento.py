valor_hora = float(input("Por favor, insira o valor da sua hora: "))
horas_trabalhadas = int(input("Por favor, insira a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    desconto_ir = 0
elif salario_bruto <= 1500:
    desconto_ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    desconto_ir = salario_bruto * 0.10
else:
    desconto_ir = salario_bruto * 0.20

desconto_inss = salario_bruto * 0.10

fgts = salario_bruto * 0.11

total_descontos = desconto_ir + desconto_inss

salario_liquido = salario_bruto - total_descontos

print("Salário bruto (", valor_hora, " * ", horas_trabalhadas, "): R$ ", salario_bruto)
print("( – ) IR (5%): R$ ", desconto_ir)
print("( – ) INSS (10%): R$ ", desconto_inss)
print("FGTS (11%): R$ ", fgts)
print("Total de descontos: R$ ", total_descontos)
print("Salário Líquido: R$ ", salario_liquido)
