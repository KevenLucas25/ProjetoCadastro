from interface import *
from arquivo import *
from time import sleep
from comandos import *

arq = "cadastrodepessoas.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver Pessoas Cadastradas", "Cadastrar Nova Pessoa", "Apagar Última Pessoa Cadastrada", "Apagar Todas as Pessoas Cadastradas", "Sair do Sistema"])

    if resposta == 1:
        tipo_pessoa = leiaTexto("Você deseja ver Pessoa Física [F] ou Pessoa Jurídica [J]? ").strip().upper()
        if tipo_pessoa in ["F", "J"]:
            lerArquivoTipoPessoa(arq, tipo_pessoa)
        else:
            print("OPÇÃO INVÁLIDA. DIGITE [F] PARA FÍSICA E [J] PARA PESSOA JURÍDICA.")
    elif resposta == 2:
        cabeçalho("NOVO CADASTRO")
        tipo = leiaTexto("Digite [F] para pessoa Física  e [J] para pessoa Jurídica: ").strip().upper()
        if tipo == "F":
            nome = leiaTexto("Digite o nome: ")
            cpf = formatar_cpf("Digite o CPF: ")
            idade = leiaInt("Qual sua idade? ")
            telefone = formatar_telefone("Digite seu número de telefone: ")
            endereco = leiaTexto("Digite o endereço: ")
            dados = f"F;{nome};{idade};{cpf};{telefone};{endereco}"
            cadastrar(arq, dados)
            print(f"\033[1;35mUsuário {nome} cadadastrado com sucesso! \033[m")
            sleep(2)
        elif tipo == "J":
            nome = leiaTexto("Digite a Razão Social: ")
            cnpj = formatar_cnpj("Digite o CNPJ:")
            telefone = formatar_telefone("Digite o telefone da empresa: ")
            atividade = leiaTexto("Digite o tipo de atividade da empresa: ")
            endereco = leiaTexto("Digite o endereço da empresa: ")
            dados = f"J;{nome};{cnpj};{atividade};{telefone};{endereco}"
            cadastrar(arq, dados)
    elif resposta == 3:
        apagarUltimoCadastro(arq)
    elif resposta == 4:
        apagarTodasPessoas(arq)
    elif resposta == 5:
        cabeçalho("\t\t\033[1;35mSaindo do sistema... Até logo\033[m")
        break
    else:
        print("\033[1;31mERRO! Digite uma opção válida!\033[m")
        sleep(2)
