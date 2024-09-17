

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
        print("\nOperação não realizada!! Valor informado é inválido")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n Operção falhou!! Você não saldo suficiente para essa operação!")

    elif excedeu_limite:
        print("\n Operação falhou!! O valor do saque excede o limite!")
    elif excedeu_saques:
        print("\n Operação falhou!! Você excedeu o limite de saques")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t \tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n O saque foi realizado com sucesso!!")
    else:
        print("\nOperação falhou!! O Valor informado é inválido!")

    return saldo, extrato

