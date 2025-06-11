# --------------------------------------------------------
# Diário de Aprendizado – Construção da Calculadora com Python
# Disciplina: DGT2817 – Lógica, Algoritmos e Programação de Computadores
# Aluna: Pita
# Curso: Desenvolvimento Full Stack – Estácio (EAD) – 1º Período
# Repositório do Projeto: https://github.com/pietraamorim/calculadora.py
# --------------------------------------------------------

# INTRODUÇÃO
# Olá! Eu sou a Pita, estudante de Desenvolvimento Full Stack, autista e borderline.
# Este arquivo é um resumo do que aprendi durante o desenvolvimento do meu trabalho prático.
# Aqui estão as microatividades, explicações pessoais e o código final da calculadora interativa.
# Foi desafiador, mas muito gratificante entender como essas estruturas funcionam juntas.

# --------------------------------------------------------
# MICROATIVIDADE 1 – Estrutura Condicional IF e ELSE
# --------------------------------------------------------

temperatura = 29

if temperatura < 30:
    print('A temperatura hoje está amena')
else:
    print('Hoje está fazendo calor')

temperatura = 31
if temperatura < 30:
    print('A temperatura hoje está amena')
else:
    print('Hoje está fazendo calor')

# --------------------------------------------------------
# MICROATIVIDADE 2 – Estrutura Condicional ELIF
# --------------------------------------------------------

tempoExperiencia = 5

if tempoExperiencia < 2:
    print('Nível de conhecimento júnior.')
elif 2 <= tempoExperiencia < 5:
    print('Nível de conhecimento pleno.')
else:
    print('Nível de conhecimento sênior.')

# --------------------------------------------------------
# MICROATIVIDADE 3 – Estrutura de Repetição WHILE
# --------------------------------------------------------

entrada_idade = ''

while entrada_idade != '0':
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
    print('Número digitado:', entrada_idade)

# --------------------------------------------------------
# MICROATIVIDADE 4 – Estrutura de Repetição FOR
# --------------------------------------------------------

texto = 'Olá, laço for.'

for item in texto:
    print('Caractere:', item)

for numero in range(1, 11):
    print('Número do intervalo:', str(numero))

# --------------------------------------------------------
# MICROATIVIDADE 5 – Funções sem parâmetros
# --------------------------------------------------------

def imprimir_variavel():
    texto = 'Olá, funções em Python'
    print(texto)

imprimir_variavel()

# --------------------------------------------------------
# MICROATIVIDADE 6 – Funções com parâmetros
# --------------------------------------------------------

def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')

# --------------------------------------------------------
# PROJETO FINAL – Calculadora com Funções, Condicionais e Repetição
# --------------------------------------------------------

def adicao(a, b):
    return a + b

def subracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

def calculadora(num1, num2, operacao):
    operacao = operacao.lower()
    if operacao == '+' or operacao == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao':
        resultado = subracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida'
    return resultado

saida = ''

while saida != 'n':
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operacao = input('Digite a operação (+, -, *, / ou nome da operação): ')
    resultado = calculadora(num1, num2, operacao)
    print('Resultado da operação:', resultado)
    saida = input('Deseja continuar? (S/N): ').lower()

# --------------------------------------------------------
# CONSIDERAÇÕES FINAIS
# --------------------------------------------------------

# Esse trabalho me ensinou muito sobre lógica, paciência e como programar pode ser divertido e estruturado.
# Como autista, achei a organização dos blocos e funções algo reconfortante.
# Estou muito feliz de ter feito esse projeto do meu jeito e com explicações que fazem sentido pra mim 💖

# Repositório do projeto no GitHub:
# https://github.com/pietraamorim/calculadora.py
