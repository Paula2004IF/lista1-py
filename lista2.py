'''
Exercícios sobre os comandos de condição em python
'''

from datetime import date, datetime
from deep_translator import GoogleTranslator # pip3 install deep-translator

HOJE = datetime.now()
tradutor = GoogleTranslator(source = 'en', target = 'pt')

#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q1():
    a = int(input('Digite o primeiro valor inteiro: '))
    b = int(input('Digite o segundo valor inteiro: '))
    
    soma = a + b
    if soma > 10:
        print(f'A soma é: {soma}')
    else:
        print(f'A soma não é maior que 10')

   
  

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
def q2():
    valor1 = (int(input('Digite um número: ')))
    valor2 = (int(input('Digite outro número: ')))
    total = valor1 + valor2
    if total > 20 :
        print (f'Total é igual a: {total+8}')
    else:
        print (f'Total é igual a: {total-5}')


#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q3():
    numero = int(input('Digite um número: '))
    if numero % 3 == 0:
        print(f'É múltiplo de 3')
    else:
        print(f'Não é múltiplo de 3')
    

    

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def q4():
    numero = (int (input ('Digite um número: ')))
    if numero % 5==0:
        print (f'É multiplo de 5.')
    else:
        print (f'Não é múltiplo de 5.')


#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.


def q5():

    
    numero = (int(input('Digite um número: ')))
    if numero % 3 == 0 and numero % 7 == 0:
        print(f'{num}divisível por 3 e por 7')
    else:
        print('Não é divisível por 3 e  por 7')




#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valosr máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.


def q6():
    salario = float(input('Digite o valor do salário:R$ '))
    valor_da_prestacao = float(input('Valor da parcela:R$ '))
    limite = salario * 0.30
    if valor_da_prestacao <= limite:
        print ('Empréstimo aprovado.')
    else:
        print ('Empréstimo negado.')


#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def q7 ():
    numero = int(input())

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".

def q8():
    numero = int(input('Digite um número: '))
    if numero > 20:
        print('Maior que 20')
    elif numero == 20:
        print('É igual a 20')
    else:
        print('Então é menor que 20')


#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.

def q9():
    ano_de_nascimento = int(input('Digite o ano de nascimento: '))
    ano_atual = int(input('Digite o ano atual: '))

    idade = ano_atual - ano_de_nascimento
    print (f'{idade} anos.')
    if idade < 0:
        print ('Idade não válida.')
    else:
        print ('Idade válida')


#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
def q10():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    num3 = int(input('Digite mais um número: '))

    numeros = [num1, num2, num3]
    numeros.sort()
    print (f' Números em ordem crescente: {numeros}')
    


#11. Faça um programa que leia 3 números e imprima o maior deles.
def q11():
    num1 = int (input('Digite um número: '))
    num2 = int (input('Digite outro número: '))
    num3 = int (input('Digite mais número: '))
    maior = max (num1, num2, num3)
    print (f'O maior número é: {maior}')    
#12. Faça um programa que leia a idade de uma pessoa e informe:

#• Se é maior de idade
#• Se é menor de idadea
#• Se é maior de 65 anos

def q12():

    idade = int(input('A idade da pessoa é: '))
    if idade >=65:
        print (f'A pessoa é maior de 65 anos')
    elif idade >= 18:
        print (f'A pessoa é maior de idade.')
    else:
        print (f'A pessoa é menor de idade.')

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).

def q13():
    nome = input ('Digite o nome do aluno: ')
    nota1 = float (input('Digite a primeira nota: '))
    nota2 = float (input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2

    print (f'A média é: {media}')
    if media >= 7:
        print (f'Aluno aprovado!')
    elif media < 3:
        print ('Aluno reprovado!')
    else:
        print (f'Aluno irá para Prova Final!')
#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%

def q14():
    salario = float(input('Valor do salário: R$'))
    if salario <= 600:
        desconto = 0
        print (f'Isento.')
    elif salario <= 1200:
        desconto = 0,.20* salario
        print (f'Desconto de 20% no salário.')
    elif salario <= 2000:
        desconto = 0.25 * salario
        print (f'Desconto de 25% no salário.')
    else:
        desconto = 0.30 * salario
        print (f'Desconto de 30% no salário.')
#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda:

def q15():
    valor_do_produto = float (input('Digite o valor de compra do produto: R$'))
    if valor_do_produto < 20:
        valor_venda = valor_do_produto * 1.45
        print (f'O valor de venda deste produto é: R${valor_venda}')
    else:
        valor_venda = valor_do_produto * 1.30
        print (f'O valor de venda deste produto é: R${valor_venda}')


#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos
def q16():
        idade = int(input("Digite a idade do nadador:"))
        if 5 <= idade <= 7:
            print (f'Nadador pertence a Categoria Infantil A')
        elif 8 <= idade <= 10:
            print (f'Nadador pertence a Categoria Infantil B')
        elif 11 <= idade <= 13:
            print (f'Nadador pertence a Categoria Juvenil A')
        elif 14 <=idade <= 17:
            print (f'Nadador pertence a Categoria Juvenil B')
        else:
            print (f'Nadador pertence a Categoria Sênior.')

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

    

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

def q18():
    mes = int (input('Digite o número do mês: '))
    if mes < 1 or mes> 12:
        print ('Mês inválido')
    else:
        data = datetime.strptime(f'01/{mes}/24','%d/%m/%y')
        mes_extenso = data.strftime('%B')
        print(tradutor.translate(mes_extenso))


#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

def q20():
    saldo_medio = float (input('Digite o saldo médio da conta bancária: R$'))
    
    if saldo_medio <= 500:
        print (f'Nenhum crédito.')
    elif saldo_medio <= 1001:
        print (f'Tem um saldo de crédito de 30%.')
    elif saldo_medio <= 3000:
        print (f'Saldo de crédito de 40%.')
    else:
        print (f'Saldo de crédito de 50%')
#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal
def q23():
    pratos = '''
Pratos
1 - Vegetariano 
2 - Peixe
3 - Frango
4 - Carne

 Opção: 
    '''
    sobremesas = '''
    Sobremesas:
    1 - Abacaxi
    2 - Sorvete Diet
    3 - Mousse Diet
    4 - Mousse Chocolate
    Opção: 
    '''
    bebidas = '''
    Bebidas:
    1 - Chá
    2 - Suco de Laranja
    3 - Suco de Melão
    4 - Refrigerante Diet

     Opção: 
    '''
    prato = int(input(pratos))
    sobremesa = int(input(sobremesas))
    bebida = int(input(bebidas))

    cal = 0
    cal += 180 if prato == 1 else 0
    cal += 230 if prato == 2 else 0
    cal += 250 if prato == 3 else 0
    cal += 350 if prato == 4 else 0    
    cal += 75 if sobremesa == 1 else 0
    cal += 110 if sobremesa == 2 else 0
    cal += 170 if sobremesa == 3 else 0
    cal += 200 if sobremesa == 4 else 0
    cal += 20 if bebida == 1 else 0
    cal += 70 if bebida == 2 else 0
    cal += 100 if bebida == 3 else 0
    cal += 65 if bebida == 4 else 0    
    print(f'Total de calorias: {cal}')

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos

questao = int(input('Questão a ser executada: '))
match questao:
    case 1:
        q1()
    case 2:
        q2()
    case 3:
        q3()
    case 4:
        q4()
    case 5:
        q5()
    case 6:
        q6()
    case 7:
        q7()
    case 8:
        q8()
    case 9:
        q9()
    case 10:
        q10()
    case 11:
        q11()
    case 12:
        q12()
    case 13:
        q13()
    case 14:
        q14()
    case 15:
        q15()
    case 16:
        q16()
    case 17:
        q17()
    case 18:
        q18()
    case 19:
        q19()
    case 20:
        q20()
    case 23:
        q23()
        

        
