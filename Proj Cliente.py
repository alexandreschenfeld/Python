class cliente:
    def __init__(self, nome, email, tel):
        self.nome = nome
        self.email = email
        self.tel = tel

    def exibir_det(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.tel}")
        print("*" * 30)

class cad:
    def __init__(self):
        self.clientes = []
    def add_cliente(self, cliente):
        self.clientes.append(cliente)
    def Listar_cliente(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            print("Cliente(s) cadastrado(s)!")
            for cliente in self.clientes:
                cliente.exibir_det()

cad = cad()

while True:
    print("1 - Cadastrar novo(s) cliente(s)")
    print("2 - Listar todos os clientes")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        email = input("Digite o Email do cliente: ")
        tel = input("Digite o telefone do cliente: ")

        cliente = cliente(nome, email, tel)
        cad.add_cliente(cliente)
        print("Cliente cadastrado com sucesso!!! \n")

    elif opcao == "2":
        cad.Listar_cliente()

    elif opcao == "3":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Tente novamente. \n")
