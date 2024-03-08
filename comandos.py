 # LÊ SOMENTE AS RESPOSTAS DO USUÁRIO EM FORMA DE STRING
def leiaTexto(msg):
    while True:
        try:
            n = str(input(msg))
            if n.replace(" ", "").isalpha(): # CASO USUÁRIO DIGITE ALGO QUE CONTENHA ESPAÇO, O PROGRAMA RETIRA!
                return n
            else:
                print("\033[1;31mPor favor, digite apenas letras.\033[m")
        except KeyboardInterrupt:
            print("\033[1;31mO usuário preferiu não digitar um número!\033[m")
            return 0

        # LÊ AS RESPOSTA DO USÚARIO SOMENTE COM NÚMEROS INTEIROS
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print("\033[1;31mERRO!! Digite um número inteiro válido\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[1;31mO usuário preferiu não digitar o número!!\033[m")
            return 0
        else:
           return n


 # FORMA O CNPJ CONFORME PADRÃO NACIONAL
def formatar_cnpj(msg):
    while True:
        try:
            cnpj = input(msg)
            # VERIFICA SE O A QUANTIDADE DE  NÚMEROS QUE O USUÁRIO DIGITAR É IGUAL Á 14.
            if len(cnpj) == 14 and cnpj.isdigit():
                cnpj_formatado = '{}.{}.{}/{}-{}'.format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])
                return cnpj_formatado
            else:
                print("\033[1;31mPor favor, digite exatamente 14 dígitos numéricos para o CNPJ.\033[m")
        except KeyboardInterrupt:
            print("\033[1;31mO usuário preferiu não digitar o CNPJ.\033[m")
            return None

    # FORMA O CPF CONFORME O PADRÃO NACIONAL
def formatar_cpf(msg):
    while True:
        try:
            cpf = input(msg)
            # VERIFICA SE O A QUANTIDADE DE  NÚMEROS QUE O USUÁRIO DIGITOU É IGUAL Á 11.
            if len(cpf) == 11 and cpf.isdigit():
                cpf_formatado = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
                return cpf_formatado
            else:
                print("\033[1;31mPor favor, digite exatamente 11 dígitos numéricos para o CPF.\033[m")
                continue
        except KeyboardInterrupt:
            print("\033[1;31mO usuário preferiu não digitar o CPF.\033[m")
            return None


    # FORMATA O NÚMERO DE TELEFONE CONFORME PADRÃO NACIONAL
def formatar_telefone(msg):
    while True:
        try:
            telefone = input(msg)
            if len(telefone) == 11 and telefone.isdigit():
                formatar_telefone = "{} {}-{}".format(telefone[:2], telefone[2:7],telefone[7:11])
                return formatar_telefone
            else:
                print("\033[1;31mPor favor, digite exatamente 11 números (incluindo o DDD) para o Telefone.\033[m")
                continue
        except KeyboardInterrupt:
            print("\033[1;31mO usuário preferiu não digitar o CPF.\033[m")
            return None
