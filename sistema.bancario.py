
nome = 'John'
saldo = 2000
numeros_saques = 0
SAQUE_LIMITE = 3
limite = 500 
extrato = ""

apresentacao = (f"Olá, {nome} seja bem-vindo(a) ao nosso sistema bancário!")
print(apresentacao)

menu = (f"""
Escolha a operação que você deseja realizar :
[1] Depósito
[2] Saque
[3] Emitir extrato
[0] Sair 
""")

while True:
    opcao = input(menu)
    
    if opcao == '1':
        print('Você escolheu depósito.')
        valor_deposito = float(input(f'Digite o valor que você deseja depositar : R$ '))
        if valor_deposito > 0:
            extrato += (f'Você depositou: R${valor_deposito:.2f}\n')
            saldo += valor_deposito
            print(f'Valor de R${valor_deposito} depositado com sucesso!')
        else: 
            print('Operação não realizada.')

    elif opcao == '2':
        print('Você escolheu Saque.') 
        valor_saque = float(input(f'Digite o valor que deseja sacar : R$'))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numeros_saques >= SAQUE_LIMITE

        if excedeu_saldo: 
             print('O Valor do saque excede o saldo.')
            
        elif excedeu_limite:
             print('O valor do saque excedeu o limite de R$500,00 de saque. ')
        
        elif excedeu_saques:
             print('Você não pode realizar essa operação de saque, pois excedeu o limite diários de saques.')

        elif valor_saque > 0:
            extrato += (f'Você sacou: R${valor_saque:.2f}\n')
            saldo -= valor_saque
            numeros_saques += 1
            print(f'Valor de R${valor_saque:.2f} sacado com sucesso!')
        
        else:
            print('Não foi possível concluir a operação.')
        
    elif opcao == '3':
        print(f'Você quer emitir o extrato, aqui está :\nEmitindo extrato...')
        print(f'######################EXTRATO######################\n{extrato}')
        print(f'Esse é o seu saldo bancário: R${saldo:.2f}')
        print('###################################################')
    
    elif opcao == '0':
        print(f'Agradecemos pela preferência do nosso sistema {nome}, volte sempre!')
        break

    else:
        print('Opção inválida, por favor digite uma opção do menu.')