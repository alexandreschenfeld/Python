from calc import operacoes
def menu():
    print("\nEscolha uma operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Mutiplicar")
    print("4 - Dividir")
    print("5 - Potência")
    print("6 - Raiz quadrada")
    print("0 - Sair")

def num(mens):
    while True:
        try:
            return float(input(mens))
        except ValueError:
            print("Por favor, digite um número válido!!!")

print("Bem-vindo ao Calculadora em Python!!!")

while True:
    menu()
    escolha = input("Digite sua escolha: ")
    if escolha == "0":
        print("Saindo do programa, até logo...")
        break
    if escolha in "12345":
        num1 = num("Digite o primeiro número: ")
        num2 = num("Digite o segundo número: ")
        if escolha == "1":
            resultado = operacoes.somar(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif escolha == "2":
            resultado = operacoes.subtrair(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif escolha == "3":
            resultado = operacoes.multiplicar(num1, num2)
            print(f"Resultado: {num1} x {num2} = {resultado}")
        elif escolha == "4":
            resultado = operacoes.dividir(num1, num2)
            print(f"Resultado: {num1} / {num2} = {resultado}")
        elif escolha == "5":
            resultado = operacoes.potencia(num1, num2)
            print(f"Resultado: {num1} ** {num2} = {resultado}")
    elif escolha == "6":
            num1 = num("Digite um número maior ou igual a 0: ")
            resultado = operacoes.raiz(num1)
            print(f"Resultado: Raiz quadrada de {num1} = {resultado}")
    else:
            print("Opção inválida!!! Tente novamente... ")