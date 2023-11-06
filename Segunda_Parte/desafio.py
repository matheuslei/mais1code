velocidade_ms = float(input("Digite a velocidade em metros por segundo (m/s): "))

velocidade_kmh = velocidade_ms * 3.6

print("A velocidade em quilômetros por hora é: ", velocidade_kmh, "Km/h")

distancia_km = 435
tempo_viagem = distancia_km / velocidade_kmh

print("O tempo de viagem de São Paulo até o Rio de Janeiro é: ", tempo_viagem, "horas")
