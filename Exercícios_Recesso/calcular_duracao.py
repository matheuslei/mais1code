def calcular_duracao(hora_inicio, minuto_inicio, hora_termino, minuto_termino):
    duracao_horas = hora_termino - hora_inicio
    duracao_minutos = minuto_termino - minuto_inicio

    if duracao_minutos < 0:
        duracao_horas -= 1
        duracao_minutos += 60

    if duracao_horas < 0:
        duracao_horas += 24

    return duracao_horas, duracao_minutos

hora_inicio = int(input("Digite a hora de início do jogo: "))
minuto_inicio = int(input("Digite o minuto de início do jogo: "))
hora_termino = int(input("Digite a hora de término do jogo: "))
minuto_termino = int(input("Digite o minuto de término do jogo: "))
duracao = calcular_duracao(hora_inicio, minuto_inicio, hora_termino, minuto_termino)
print(f'Duração do jogo: {duracao[0]} horas e {duracao[1]} minutos')