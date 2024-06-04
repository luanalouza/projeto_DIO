import os

mov = []
saldo = 0

def select1(mov, saldo):
    while True:
        try:
            op = int(input('Selecione a opção desejada : '))
            if op == 1:
                clear()
                deposito(mov, saldo)
                break
            elif op == 2:
                clear()
                saque(mov, saldo)
                break
            elif op == 3:
                clear()
                extrato(mov, saldo)
                break
            else:
                print('Opção inválida, digite novamente.')
        except ValueError:
            print('Entrada inválida, por favor insira um número.')

def clear():
    os.system('cls')

def deposito(mov, saldo):
    try:
        valor = float(input('Digite o valor para depósito: '))
        saldo += valor
        mov.append(f'Depósito: +{valor:.2f}')
        print(f'Valor depositado: {valor:.2f}')
    except ValueError:
        print('Valor inválido, operação cancelada.')
    finally:
        main_menu(mov, saldo)

def saque(mov, saldo):
    try:
        valor = float(input('Digite o valor para saque: '))
        if valor > saldo:
            print('Saldo insuficiente.')
        else:
            saldo -= valor
            mov.append(f'Saque: -{valor:.2f}')
            print(f'Valor sacado: {valor:.2f}')
    except ValueError:
        print('Valor inválido, operação cancelada.')
    finally:
        main_menu(mov, saldo)

def extrato(mov, saldo):
    print("Extrato de Movimentações:")
    for item in mov:
        print(item)
    print(f'Saldo atual: {saldo:.2f}')
    input("Pressione Enter para continuar...")
    main_menu(mov, saldo)

def main_menu(mov, saldo):
    clear()
    print("--------------------------------------------------------------")
    print("                      SISTEMA BANCARIO                        ")
    print("                      1-Depositar                             ")
    print("                      2-Sacar                                 ")
    print("                      3-Extrato                               ")
    select1(mov, saldo)

main_menu(mov, saldo)
