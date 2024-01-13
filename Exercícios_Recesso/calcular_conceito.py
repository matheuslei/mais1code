def calcular_conceito(media):
    if media >= 0.0 and media <= 4.9:
        conceito = 'D'
    elif media >= 5.0 and media <= 6.9:
        conceito = 'C'
    elif media >= 7.0 and media <= 8.9:
        conceito = 'B'
    elif media >= 9.0 and media <= 10.0:
        conceito = 'A'
    else:
        conceito = 'Média inválida'
    
    return conceito

media = float(input("Digite a média final do aluno: "))
conceito = calcular_conceito(media)
if conceito == 'Média inválida':
    print(conceito)
else:
    print(f'O conceito do aluno é: {conceito}')