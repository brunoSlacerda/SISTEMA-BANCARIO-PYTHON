import os

#=-=-=-=-=-=-=-==-=-=-=-=-=-=-Início do Menu=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=--=
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('='*30)
    print("{:^30}". format("SISTEMA BANCÁRIO"))
    print('='*30)
    print("1 - ABRIR CONTA")
    print("2 - REALIZAR DEPÓSITO")
    print("3 - REALIZAR SAQUE")
    print("4 - SIMULAR EMPRÉSTIMO")
    print("5 - EXTRATO")
    print("6 - SAIR")
    resultado = int(input("\nPara prosseguir, informe a opção desejada: "))
    return resultado #RETORNA O NÚMERO ESCOLHIDO PELO USUÁRIO
#=-=-=-=-=-=-=-==-=-=-=-=-=-=-Fim do Menu=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=--=


#=-=-=-=-=-=-=-==-=-=-=-=-=-=-Início das Variáveis=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=--=
saldo_inicial = 0
nome_cliente = ''
valor_depositado = 0
saldo_atual = saldo_inicial + valor_depositado
cont_depositos = 0
cont_saque = 0
valorTotal_depositado = 0
x = 0
enter = 'a'
contagem = 0
opcao = 0
valor_emprestado = 0
quant_parcelas = 0
valor_total_juros = 0
soma_sacada = 0
#=-=-=-=-=-=-=-==-=-=-=-=-=-=-Fim das Variáveis=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=--=


while opcao!=6:
    opcao = menu() #RECEBE O NÚMERO ESCOLHIDO PELO USUÁRIO PARA TESTAR OS IF'S
    os.system('cls' if os.name == 'nt' else 'clear')
    #OPÇÃO 1 - ABRIR CONTA
    if opcao == 1 and contagem == 0:
        print( "ACESSE SUA CONTA")
        nome_cliente = input("Informe seu nome: ")
        saldo_inicial = float(input("Informe seu saldo inicial: R$"))
        print("\nAbertura de conta efetuada! Escolha outra opção para continuar.")
        saldo_atual = saldo_inicial
        contagem+=1 #SISTEMA PARA NÃO REPETIR OPÇÃO 1
   

    #OPÇÃO 2 - DEPÓSITO
    if opcao == 2 and contagem == 1:
        while True:
            valor_depositado = float(input("\nInforme o valor a ser depositado: R$"))
            if valor_depositado<=0:
                print("Informe um número válido.")
            else:
                print("Depósito realizado com sucesso!")
                saldo_atual = saldo_atual + valor_depositado
                cont_depositos+=1
                valorTotal_depositado += valor_depositado
                print(f"Seu novo saldo é de: R${saldo_atual:.2f}")
                break
        print("")
        enter = str(input("Para retornar ao menu pressione ENTER"))    
   

    #OPÇÃO 3 - SAQUE
    if opcao == 3 and contagem == 1:
        print(f"Saldo disponível: R${saldo_atual:.2f}")
        
        while True:
            valor_sacado = float(input("Informe o valor a ser sacado: R$"))
            valor_desconto = valor_sacado
            
            
            if valor_sacado > saldo_atual:
                print("Saldo insuficiente! Tente novamente.")
                a = input("Digite ENTER para voltar ao MENU")
                break
                
            if valor_sacado<=0:
                print("Valor inválido! Tente novamente.")
                a = input("Digite ENTER para voltar ao MENU")
                break

            nota200 = 0
            nota100 = 0
            nota50 = 0
            nota20 = 0
            nota10 = 0
            nota5= 0 
            nota2 = 0
            while True:
                if valor_sacado>=200:
                    valor_sacado = valor_sacado-200
                    nota200+=1
                              
                elif valor_sacado<200 and valor_sacado>=100:
                    valor_sacado = valor_sacado-100
                    nota100+=1
                
                elif valor_sacado<100 and valor_sacado>=50:
                    valor_sacado = valor_sacado-50
                    nota50+=1
                    
                elif valor_sacado<50 and valor_sacado>=20:
                    valor_sacado = valor_sacado-20
                    nota20+=1
                
                elif valor_sacado<20 and valor_sacado>=10:
                    valor_sacado = valor_sacado-10
                    nota10+=1 

                elif valor_sacado<10 and valor_sacado>=5:
                    valor_sacado = valor_sacado-5
                    nota5+=1

                elif valor_sacado<5 and valor_sacado>=2:
                    valor_sacado = valor_sacado-2
                    nota2+=1
                
                if valor_sacado == 0:
                    print("Seu saque foi concluido! Abaixo a quantidade de notas a serem retiradas:")
                    print(f"NOTA DE 200 - {nota200}")
                    print(f"NOTA DE 100 - {nota100}")
                    print(f"NOTA DE 50 - {nota50}")
                    print(f"NOTA DE 20 - {nota20}")
                    print(f"NOTA DE 10 - {nota10}")
                    print(f"NOTA DE 5 - {nota5}")
                    print(f"NOTA DE 2 - {nota2}")
                    saldo_atual = saldo_atual - valor_desconto
                    soma_sacada = soma_sacada + valor_desconto
                    cont_saque+=1
                    print(f"Seu saldo atual é de: R${saldo_atual:.2f}")
                    a = input("Digite ENTER para voltar ao MENU")
                    break

                if valor_sacado == 1:
                    print("Valor inválido! Volte ao menu e tente um novo valor.")
                    a = input("Digite ENTER para voltar ao MENU")
                    valor_sacado-=1
                    break
            
            break
                        
                
    #OPÇÃO 4 - EMPRÉSTIMO
    if opcao == 4 and contagem == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        valor_emprestado = float(input("Informe o valor a ser simulado R$"))
        quant_parcelas = int(input("Em quantas vezes: "))
        
        valor_juros = valor_emprestado*0.02
        valor_parcela = (valor_emprestado/quant_parcelas)+valor_juros
        valor_total_juros = valor_parcela * quant_parcelas - valor_emprestado #VALOR TOTAL DOS JUROS
        valor_tot_emprestimo = valor_emprestado + valor_total_juros #CÁLCULO VALOR TOTAL DO EMPRÉSTIMO
        print("="*30)
        print("O valor total de juros é R${:.2F}". format(valor_total_juros))
        print("No total serão {} parcelas de R${:.2f}". format(quant_parcelas, valor_parcela))
        print("="*30)
        for i in range (1, quant_parcelas + 1):
            print("{}° parcela no valor de R${:.2f}". format(i, valor_parcela))
        print("="*30)
        print("Para um emprestimo de R${:.2f}, em {} vezes, o valor total a ser pago é de R${:.2f}". format(valor_emprestado, quant_parcelas , valor_tot_emprestimo))
        while True:
            realizar = input("Deseja realizar este emprestimo S/N? ").upper() #UPPER PARA TORNAR O DÍGITO MAIÚSCULO
            if realizar == "S":
                saldo_atual += valor_emprestado
                print("Seu saldo atual agora é R${:.2f}, com empréstimo de R${:.2f}". format(saldo_atual, valor_emprestado))
                print("")
                enter = str(input("Para retornar ao menu pressione ENTER"))
                break
            else:
                break

    
    #OPÇÃO 5 - EXTRATO
    if opcao == 5 and contagem == 1:
        print('='*30)
        print("{:^30}". format("SEU EXTRATO"))
        print('='*30)
        print("NOME DO CLIENTE: {}". format(nome_cliente))
        print(f"SEU SALDO INICIAL ERA DE: R${saldo_inicial:.2f}")
        print(f"SALDO FINAL:R${saldo_atual:.2f}")
        print(f"QUANTIDADE DE VEZES DEPOSITADAS NA CONTA: {cont_depositos}")
        print(f"VALOR TOTAL DEPOSITADO NA CONTA: R${valorTotal_depositado:.2f}")
        print(f"QUANTIDADE DE SAQUES REALIZADOS: {cont_saque}")
        print("VALOR TOTAL QUE FOI SACADO DA CONTA R${:.2f}". format(soma_sacada))
        print("VALOR TOTAL DE JUROS RECEBIDOS: R${:.2f}". format(valor_total_juros))
        print("")
        enter = str(input("Para retornar ao menu pressione ENTER"))
    
    if opcao == 6:
        print("SAINDO...")