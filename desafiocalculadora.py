#IMPORTA A BIBLIOTECA 'MATH' COMO M,
import math as m
soma = []
multiplicaca = []


#FUNÇÃO PARA RAIZ QUADRADA
def raiz_quadrada(a):
    m.sqrt(a)
    return a ** 0.5

#FUNÇÃO PARA SOMAR
def somar(a):
    return m.fsum(a)

#FUNÇÃO PARA SUBTRAIR
def subtracao(a,b):
    return a-b

#FUNÇÃO PARA DIVISÃO
def divisao(a,b):
    return a / b 

#FUNÇÃO PARA MULTIPLICAÇÃO
def multiplicacao(a):
    return m.prod(a)

#VARIAVEL PARA DEFINIR QUAL OPERAÇÃO SERÁ REALIZADA.
operacao = str(input('Insira a operação que deseja.\n 1 para somar\n 2 para subtrair\n 3 para multiplicar\n 4 para dividir\n 5 para raiz quadrada\n resposta:'))

#CASO O USUARIO ESCOLHA SOMAR
if operacao == '1':
        soma.append(float(input('insira o primeiro numero:')))
        soma.append(float(input('insira o segundo numero:')))
        print('Soma:',somar(soma))

#CASO O USUARIO ESCOLHA RAIZ QUADRADA
elif operacao == '5':
     a = float(input('Insira um numero:'))
     resultado = raiz_quadrada(a)
     print(resultado)

#CASO O USUARIO ESCOLHA SUBTRAIR 
elif operacao == '2':
    a = (float(input('insira o primeiro numero:')))
    b = (float(input('insira o segundo numero:')))
    resultado = subtracao(a,b)
    print(resultado)

#CASO O USUARIO ESCOLHA MULTIPLICAR
elif operacao == '3':
    multiplicaca.append(float(input('insira o primeiro numero:')))
    multiplicaca.append (float(input('insira o segundo numero:')))
    print('Multiplicar:',multiplicacao(multiplicaca))

#CASO O USUARIO ESCOLHA DIVIDIR
elif operacao == '4':
    a = (float(input('insira o primeiro numero:')))
    b = (float(input('insira o segundo numero:')))
    resultado = divisao(a,b)
    print(resultado)

     








    
