from interface import *


# SE O ARQUVO EXISTE O PROGRAMA ABRE
def arquivoExiste(nome):
    try:
        a = open(nome, "rt")  # TENTA ABRIR O ARQUIVO EM TXT
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

    # CRIA O ARQUIVO DE TEXTO


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")  # VERIFICA SE EXISTE O ARQUIVO CRIADO, SE NÃO EXISTIR ELE CRIA!
        a.close()
    except:
        print("Houve um erro na criação do arquivo")
    else:
        print(f"Arquivo {nome} encontrado com sucesso!")

    # CADASTRA AS PESSOAS


def cadastrar(arq, nome="desconhecido", idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um erro na abertura do aquivo")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um erro na hora de escrever os dados")
            a.close()


# APAGA A ÚLTIMA PESSOA CADASTRADA
def apagarUltimoCadastro(arq):
    try:
        with open(arq, 'r') as arquivo:
            linhas = arquivo.readlines()
        if linhas:
            linhas.pop()
            with open(arq, 'w') as arquivo:
                arquivo.writelines(linhas)
            print("\033[1;34mÚltimo cadastro apagado com sucesso\033[m")
        else:
            print("Não há pessoas cadastradas para apagar.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except:
        print("Ocorreu um erro ao apagar o último cadastro.")

    # LÊ O ARQUIVO E O TIPO DE PESSOA


def lerArquivoTipoPessoa(arq, tipo_pessoa):
    try:
        with open(arq, 'rt') as arquivo:
            cabeçalho("PESSOAS CADASTRADAS")
            print("-=" * 45)
            if tipo_pessoa == "F":
                print("\033[1;34mNOME".rjust(10), "IDADE".rjust(20), "CPF".rjust(15), "TELEFONE".rjust(23),
                      "ENDEREÇO\033[m".rjust(20))
            elif tipo_pessoa == "J":
                print("\033[1;34mRAZÃO SOCIAL".ljust(20), "CNPJ".rjust(15), "ATIVIDADE".rjust(20), "TELEFONE".rjust(20),
                      "ENDEREÇO\033[m".rjust(21))

            # PERCORRE TODO O ARQUIVO E ALINHA OS MESMO CONFORME A QUANTIDADE ABAIXO
            for linha in arquivo:
                dados = linha.strip().split(";")
                if tipo_pessoa == "F" and dados[0] == "F":
                    print(dados[1].ljust(20), dados[2].ljust(10), dados[3].ljust(20), dados[4].ljust(20), dados[5])
                elif tipo_pessoa == "J" and dados[0] == "J":
                    print(dados[1].ljust(15), dados[2].ljust(10), dados[3].rjust(15), dados[4].rjust(23),
                          dados[5].rjust(15))
            print("-=" * 45)
        # MOSTRA O TIPO DE ERRO AO LISTAR O ARQUIVO
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao listar pessoas: {str(e)}")

    # APAGA TODAS AS PESSOAS CADASTRADAS


def apagarTodasPessoas(arq):
    try:
        with open(arq, 'w') as arquivo:
            arquivo.truncate(0)  # EXCLUI O CONTEÚDO LISTADO NO ARQUIVO
        print("\033[1;38mTodas as pessoas cadastradas foram apagadas com sucesso.\033[m")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except:
        print("Ocorreu um erro ao apagar todas as pessoas cadastradas.")