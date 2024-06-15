import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")
        self.root.configure(bg='black')

        self.frame = tk.Frame(self.root, padx=20, pady=20, bg='black')
        self.frame.pack()

        self.label_peso = tk.Label(self.frame, text="Peso (kg):", bg='black', fg='white')
        self.label_peso.grid(row=0, column=0, padx=10, pady=5)
        self.entry_peso = tk.Entry(self.frame)
        self.entry_peso.grid(row=0, column=1, padx=10, pady=5)

        self.label_altura = tk.Label(self.frame, text="Altura (m):", bg='black', fg='white')
        self.label_altura.grid(row=1, column=0, padx=10, pady=5)
        self.entry_altura = tk.Entry(self.frame)
        self.entry_altura.grid(row=1, column=1, padx=10, pady=5)

        self.calcular_button = tk.Button(self.frame, text="Calcular IMC", command=self.calculate_bmi, bg='gray', fg='white')
        self.calcular_button.grid(row=2, columnspan=2, padx=10, pady=10)

        self.label_resultado = tk.Label(self.frame, text="Resultado do IMC:", bg='black', fg='white')
        self.label_resultado.grid(row=3, column=0, padx=10, pady=5)
        self.resultado_imc = tk.Label(self.frame, text="", font=("Arial", 12, "bold"), bg='black', fg='white')
        self.resultado_imc.grid(row=3, column=1, padx=10, pady=5)

    def calculate_bmi(self):
        try:
            peso = float(self.entry_peso.get())
            altura = float(self.entry_altura.get())
            imc = peso / (altura ** 2)
            self.resultado_imc.config(text=f"{imc:.2f}")
            self.show_bmi_category(imc)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite números válidos para peso e altura.")

    def show_bmi_category(self, imc):
        categoria = ""
        if imc < 18.5:
            categoria = "Abaixo do peso"
        elif imc < 24.9:
            categoria = "Peso normal"
        elif imc < 29.9:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidade"

        messagebox.showinfo("Categoria IMC", f"Seu IMC indica: {categoria}")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='black')
    app = BMICalculator(root)
    root.mainloop()
