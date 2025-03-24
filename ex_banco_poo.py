class ContaBancaria:
    def __init__(self, titular,):
        self.titular = titular
        self.saldo = 0
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Deposito efetuado com sucesso!! Seu saldo é R$ {self.saldo},00\n')
        else:
            print('O valor para deposito tem que ser positivo\n')


    def sacar(self, valor):
        if valor < 0:
            print('O valor para saque tem que ser positivo\n')
        if valor < self.saldo and valor > 0:
            self.saldo -= valor
            print(f'Saque efetuado com sucesso!! Seu saldo é R$ {self.saldo},00\n')
        elif valor > self.saldo:
            print('Saldo insuficiente!!\n')

    def exibir_saldo(self):
        print(f'Seu saldo é R$: {self.saldo},00\n')

def banco():
    
    opcao = 0
    conta = ContaBancaria(None)
    while True:
        opcao = int(input(
        '1 - Criar conta\n'
        '2 - Depositar dinheiro\n'
        '3 - Sacar dinheiro\n'
        '4 - Consultar saldo\n'
        '5 - Sair\n'
        '\nEscolha uma opção: '))
        print('')

        match opcao:
            case 1:
                if conta.titular == None:
                    titular = (str(input('Digite o nome do titular da conta: ')))
                    print('')
                    conta = ContaBancaria(titular)
                else:
                    print('Conta ja criada!!\n')

            case 2:
                if conta.titular == None:
                    print('Primeiro cadastre uma nova conta!!!\n')
                else:
                    deposito = int(input('Digite o valor que deseja depositar: '))
                    print('')
                    conta.depositar(deposito)
            case 3:
                if conta.titular == None:
                    print('Primeiro cadastre uma nova conta!!!\n')
                else:
                    saque = int(input('Digite o valor que deseja sacar: '))
                    print('')
                    conta.sacar(saque)
            case 4:
                if conta.titular == None:
                    print('Sem Cliente cadastrado!!!\n')
                else:
                    conta.exibir_saldo()
            case 5:
                print('Saindo...')
                break
            case _:
                print('Opçao invalida, tente novamente !!\n')


banco()