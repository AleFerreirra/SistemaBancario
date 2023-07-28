menu = """
======= Informe a operação =========

[1] Depositar
[2] Sacar
[3] Extrato
[0] sair

=> """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input('Informe o valor de depósito:'))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print('Operação falhou! o valor informado é inválido.')

    elif opcao == "2":

        valor = float(input('Informe o valor do Saque:'))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        execedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print('Falha na operação! saldo insuficiente.')
        elif excedeu_limite:
            print('Falha na operação! Valor limite excedido.')
        elif execedeu_saques:
            (print('Falha na operação! Limite de saques execedido.'))
        elif valor > 0:
            saldo -= valor
            extrato -= f"Saque: R$ {valor:.2f}\n"
            excedeu_limite += 1
        else:
            print ('Falha na Operação! Valor inválido.')
    elif opcao == "3":
        print ('================= Extrato ======================\n')
        print ('\nNão foram realizadas movimentações.\n' if not extrato else extrato)
        print (f"\nSaldo: R$ {saldo:.2f}\n")
        print ('\n================================================')
    elif opcao == "0":
        break

    else:
        ('Operação inválida, selecione novamente a operação desejada.')




     
