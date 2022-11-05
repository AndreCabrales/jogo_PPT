# Funções

import cor
from time import sleep
import os
import random


def inteligencia_artifical():
    PEDRA = 1
    PAPEL = 2
    TESOURA = 3

    resultado = (random.randint(1, 3))

    # resultado do sorteio
    if resultado == PEDRA:
        robo = 1

    elif resultado == PAPEL:
        robo = 2

    elif resultado == TESOURA:
        robo = 3

    return robo


def logica(jogada, robo):

    # pedra 1 & papel 2
    if (jogada == 1) and (robo == 2):
        return f'''\nVocê escolheu PEDRA e o Computador PAPEL\n
        {cor.cores.FAIL}O compurador ganhou !!!{cor.cores.RESET}'''
    # pedra 1 & testoura 3
    elif (jogada == 1) and (robo == 3):
        return f'''\nVocê escolheu PEDRA e o Computador TESOURA\n
        {cor.cores.MAGENTA}Você ganhou !!!{cor.cores.RESET}'''
    # papel 2 & tesoura 3
    elif (jogada == 2) and (robo == 3):
        return f'''\nVocê escolheu PAPEL e o Computador TESOURA\n
        {cor.cores.FAIL}O compurador ganhou !!!{cor.cores.RESET}'''
    # papel 2 & pedra 1
    elif (jogada == 2) and (robo == 1):
        return f'''\nVocê escolheu PAPEL e o Computador PEDRA\n
        {cor.cores.MAGENTA}Você ganhou !!!{cor.cores.RESET}'''
    # tesoura 3 & Papel 2
    elif (jogada == 3) and (robo == 2):
        return f'''\nVocê escolheu TESOURA e o Computador PAPEL\n
        {cor.cores.MAGENTA}Você ganhou !!!{cor.cores.RESET}'''
    # tesoura 3 & pedra 1
    elif (jogada == 3) and (robo == 1):
        return f'''\nVocê escolheu TESOURA e o Computador PEDRA\n
        {cor.cores.FAIL}O compurador ganhou !!!{cor.cores.RESET}'''
     # resultado iguais
    else:
        return '\n      Empate'


def partida():

    while True:
        robo = inteligencia_artifical()
        print(
            f'{cor.cores.WARNING}[1]-Pedra  [2]-Papel  [3]-Tesoura [4]-Sair{cor.cores.RESET}')
        jogada = (
            input(str(f'{cor.cores.OK}Digite a opção: {cor.cores.RESET}')))

        if (jogada == '1') or (jogada == '2') or (jogada == '3'):
            jogada = int(jogada)
            resultado = logica(jogada, robo)
            print(resultado)
            input("\nAperte qualquer tecla para continuar...")
            break
        elif jogada == '4':
            os.system('cls')
            print(
                f'{cor.cores.AZUL}<<<<<< Até a próxima partida! >>>>>>{cor.cores.RESET}')
            sleep(2)
            break
        else:
            print(f'{cor.cores.FAIL}Opcão inválida!{cor.cores.RESET}')
            sleep(1)
            os.system('cls')
