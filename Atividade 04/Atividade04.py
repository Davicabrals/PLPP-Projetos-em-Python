import tkinter as tk

def atualizar_tempo():
    global tempo_decorrido, rodando
    if rodando:
        tempo_decorrido += 1
        horas = tempo_decorrido // 360000
        minutos = (tempo_decorrido % 360000) // 6000
        segundos = (tempo_decorrido % 6000) // 100
        centesimos = tempo_decorrido % 100
        label.config(text=f"{horas:02}:{minutos:02}:{segundos:02}:{centesimos:02}")
        root.after(10, atualizar_tempo)

def iniciar():
    global rodando
    if not rodando:
        rodando = True
        atualizar_tempo()

def pausar():
    global rodando
    rodando = False

def resetar():
    global tempo_decorrido, rodando
    rodando = False
    tempo_decorrido = 0
    label.config(text="00:00:00:00")

root = tk.Tk()
root.title("Cronômetro Digital")
root.configure(bg="black")

tempo_decorrido = 0
rodando = False

label = tk.Label(root, text="00:00:00:00", font=("Helvetica", 48), fg="white", bg="black")
label.pack(pady=20)

frame_botoes = tk.Frame(root, bg="black")
frame_botoes.pack()

botao_iniciar = tk.Button(frame_botoes, text="Iniciar", command=iniciar)
botao_iniciar.pack(side=tk.LEFT, padx=5)

botao_pausar = tk.Button(frame_botoes, text="Pausar", command=pausar)
botao_pausar.pack(side=tk.LEFT, padx=5)

botao_resetar = tk.Button(frame_botoes, text="Resetar", command=resetar)
botao_resetar.pack(side=tk.LEFT, padx=5)

root.mainloop()
