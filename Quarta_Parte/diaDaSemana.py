numero = int(input("Digite um número: "))

dias_da_semana = {
    1: "Domingo",
    2: "Segunda",
    3: "Terça",
    4: "Quarta",
    5: "Quinta",
    6: "Sexta",
    7: "Sábado"
}

if numero in dias_da_semana:
    print(dias_da_semana[numero])
else:
    print("Valor inválido")
