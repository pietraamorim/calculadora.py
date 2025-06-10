# Funções para as operações
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a / b

def exponenciar(a, b):
    return a ** b

def resto_divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a % b

# Função principal
def calculadora():
    print("Bem-vindo(a) à calculadora da Pita!")
    
    while True:
        print("\nEscolha uma operação:")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Exponenciação (**)")
        print("6. Resto da divisão (%)")
        print("0. Sair")
        
        escolha = input("Digite o número da operação desejada: ")
        
        if escolha == "0":
            print("Encerrando a calculadora. Até logo!")
            break
        
        if escolha in ["1", "2", "3", "4", "5", "6"]:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, digite apenas números válidos.")
                continue
            
            if escolha == "1":
                resultado = somar(num1, num2)
                operador = "+"
            elif escolha == "2":
                resultado = subtrair(num1, num2)
                operador = "-"
            elif escolha == "3":
                resultado = multiplicar(num1, num2)
                operador = "*"
            elif escolha == "4":
                resultado = dividir(num1, num2)
                operador = "/"
            elif escolha == "5":
                resultado = exponenciar(num1, num2)
                operador = "**"
            elif escolha == "6":
                resultado = resto_divisao(num1, num2)
                operador = "%"

            print(f"\nResultado: {num1} {operador} {num2} = {resultado}")
        else:
            print("Opção inválida. Tente novamente.")

# Chamada da função principal
calculadora()
