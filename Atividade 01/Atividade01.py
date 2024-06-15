def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

def menu():
    print("\nEscolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def calculadora():
    while True:
        menu()
        opcao = input("Digite sua escolha (1/2/3/4/5): ")

        if opcao not in ['1', '2', '3', '4', '5']:
            print("Escolha inválida! Por favor, selecione uma opção de 1 a 5.")
            continue

        if opcao == '5':
            print("Saindo da calculadora...")
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Por favor, digite números válidos.")
            continue

        if opcao == '1':
            print(f"Resultado: {num1} + {num2} = {somar(num1, num2)}")
        elif opcao == '2':
            print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
        elif opcao == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
        elif opcao == '4':
            resultado = dividir(num1, num2)
            print(f"Resultado: {num1} / {num2} = {resultado}")

if __name__ == "__main__":
    calculadora()
