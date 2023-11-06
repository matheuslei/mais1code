segundos_total = int(input("Digite o tempo de duração do evento em segundos: "))

horas = segundos_total // 3600
segundos_restantes = segundos_total % 3600

minutos = segundos_restantes // 60
segundos_restantes = segundos_restantes % 60

print(f"O tempo de duração do evento é: {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")
