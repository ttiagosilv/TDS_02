hora = int(input("Digite a hora: "))
minuto = int(input("Digite o minuto: "))
segundo = int(input("Digite o segundo: "))

total_segundos = hora * 3600 + minuto * 60 + segundo

print("Desde a última meia-noite, se passaram", total_segundos, "segundos.")
