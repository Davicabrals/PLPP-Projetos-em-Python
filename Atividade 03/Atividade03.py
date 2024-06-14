def adicionar_contato(agenda, nome, telefone):
    agenda[nome] = telefone
    print("Contato adicionado!")

def remover_contato(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print("Contato removido!")
    else:
        print("Contato não encontrado.")

def exibir_contatos(agenda):
    if agenda:
        print("Lista de Contatos:")
        for nome, telefone in agenda.items():
            print(f"Nome: {nome}, Telefone: {telefone}")
    else:
        print("Agenda vazia.")

def main():
    agenda = {}

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Exibir Contatos")
        print("4. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o número de telefone: ")
            adicionar_contato(agenda, nome, telefone)
        elif opcao == "2":
            nome = input("Digite o nome do contato que deseja remover: ")
            remover_contato(agenda, nome)
        elif opcao == "3":
            exibir_contatos(agenda)
        elif opcao == "4":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()