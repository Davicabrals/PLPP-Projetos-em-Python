class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print("Este contato já existe na agenda.")
        else:
            self.contatos[nome] = telefone
            print("Contato adicionado com sucesso!")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado.")

    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print(f"Nome: {nome}, Telefone: {self.contatos[nome]}")
        else:
            print("Contato não encontrado.")

    def listar_contatos(self):
        if self.contatos:
            print("Lista de Contatos:")
            for nome, telefone in self.contatos.items():
                print(f"Nome: {nome}, Telefone: {telefone}")
        else:
            print("Agenda vazia.")


def menu():
    agenda = AgendaTelefonica()

    while True:
        print("\n=== Menu ===")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Pesquisar Contato")
        print("4. Listar Contatos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif opcao == "2":
            nome = input("Digite o nome do contato que deseja remover: ")
            agenda.remover_contato(nome)
        elif opcao == "3":
            nome = input("Digite o nome do contato que deseja pesquisar: ")
            agenda.pesquisar_contato(nome)
        elif opcao == "4":
            agenda.listar_contatos()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Escolha uma opção de 1 a 5.")


if __name__ == "__main__":
    menu()
