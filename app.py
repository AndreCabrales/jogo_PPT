# Game: Pedra/Papel/Tesousa
# autor: André Cabral
# version: 1.0 - 28/10/2022

import os
from time import sleep
import jogar
import cor


def menu():
    while True:
        os.system('cls')
        print(f'''{cor.cores.WARNING}
        +--------------------------------+
        | Jogo - Pedra & Papel & Tesoura |
        +--------------------------------+
    {cor.cores.RESET}''')
        print(
            f'{cor.cores.WARNING}[1]-Jogar   [2]-Sair: {cor.cores.RESET}')
        opcao = input(str(f'{cor.cores.OK}Digite a opção: {cor.cores.RESET}'))

        if opcao == '1':
            os.system('cls')
            jogar.partida()

        elif opcao == '2':
            os.system('cls')
            print(
                f'{cor.cores.AZUL}<<<<<< Até a próxima partida! >>>>>>{cor.cores.RESET}')
            sleep(2)
            exit()

        else:
            print(f'{cor.cores.FAIL}Opcão inválida!{cor.cores.RESET}')
            sleep(1)


menu()
