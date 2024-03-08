from time import sleep
from comandos import *
def linha(tam=42):
    return "-" * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho("MENU PRINCIPAL")
    sleep(1)
    c = 1
    for item in lista:
        print(f"\033[1;33m{c}\033[m - \033[1;34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt("\033[1;32mSua Opção:\033[m ")
    return opc