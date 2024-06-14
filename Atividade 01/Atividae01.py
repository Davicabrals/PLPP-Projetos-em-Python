def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Erro: divisão por zero"
    return num1 / num2

def main():
    while True:
        print("\nEscolha uma operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        opcao = input("Opção: ")

        if opcao in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == '1':
                resultado = somar(num1, num2)
                print(f"Resultado: {resultado}")
            elif opcao == '2':
                resultado = subtrair(num1, num2)
                print(f"Resultado: {resultado}")
            elif opcao == '3':
                resultado = multiplicar(num1, num2)
                print(f"Resultado: {resultado}")
            elif opcao == '4':
                resultado = dividir(num1, num2)
                print(f"Resultado: {resultado}")

        elif opcao == '5':
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()