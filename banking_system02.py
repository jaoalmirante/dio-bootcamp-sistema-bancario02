

def menu():
    menu = """\n
    ########### MENU ###########
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar contas
    [nu]\tNovo Usuário
    [q]\tSair
    ==> """

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"## Depósito realizado com sucesso! ##"
    else:
        print("\n@@@ Operação não realizada!! Valor informado é inválido")
    return saldo, extrato

