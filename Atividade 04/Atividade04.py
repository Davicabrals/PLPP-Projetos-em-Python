import time

def cronometro():
    inicio = time.time()

    while True:
        agora = time.time()
        tempo_decorrido = int(agora - inicio)

        horas = tempo_decorrido // 3600
        minutos = (tempo_decorrido % 3600) // 60
        segundos = tempo_decorrido % 60

        print(f"Tempo decorrido: {horas:02}:{minutos:02}:{segundos:02}")
        
        time.sleep(1)

def main():
    print("Cronômetro - Pressione Ctrl+C para sair.")
    try:
        cronometro()
    except KeyboardInterrupt:
        print("\nCronômetro encerrado.")

if __name__ == "__main__":
    main()