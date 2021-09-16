from datetime import datetime
import os
import shutil
import logging

logging.basicConfig(filename='C://Users/Patricia Moretto/Desktop/TESTES/Logging.log', level=logging.DEBUG,
                    format='%(name)s %(levelname)s %(asctime)s %(message)s',
                    filemode='a'
                    )

def CriarCaminho(caminho_novo, caminho_original):
    try: 
        os.makedirs(caminho_novo)

    except FileExistsError as e:
        print("A pasta {} já existe".format(caminho_novo))

    for root, dirs, files in os.walk(caminho_original):

        for file in files: 
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(caminho_novo, file)

            if banc in file:

                shutil.move(old_file_path, new_file_path)
                print("file {} movido com sucesso".format(file))


def RemOuRet(rem_ou_ret): 
    if rem_ou_ret.upper() == str("REM"):
        rem_ou_ret = str("/{}".format(rem_ou_ret))
        print("Tudo certo! Sua remesa esta a caminho!")
        x = 2
    elif rem_ou_ret.upper() == str("RET"):
        rem_ou_ret = str("/{}".format(rem_ou_ret))
        print("Tudo certo! Seu retorno esta a caminho!")
        x = 2
    else: 
        print()
        print()
        print("Operção inválida")
        print("-" * 20)
        print("Operações aceitas:")
        print("REM - remesa")
        print("RET - retorno")
        print("-" * 20)
        x = 3



processar = ("processar")
caminho_original = ()
banc = input("Qual o código do banco? ")
dat_atual = datetime.today().strftime('%m /%d')


try:
    if banc == str("341"):
        op_usu = input("Qual operação deseja fazer? ")

        if op_usu.upper() == str("PE"):
            rem_ou_ret = input("Enviar remesa ou receber retoro? ")
            RemOuRet(rem_ou_ret)

        elif op_usu.upper() == str("CE"):
            rem_ou_ret =  input("Enviar remesa ou receber retoro? ")
            RemOuRet(rem_ou_ret)

        elif op_usu.upper() == str("EXT"):
                rem_ou_ret = str("RET")
                rem_ou_ret = str("{}".format(rem_ou_ret))
                print("Tudo certo! Seu retorno esta a caminho!")

        elif op_usu.lower() == str("inbox"):
            x = 2
        
        else: 
            print("Erro ao inserir a operação!")
            print("-"*20)
            print("Operações disponíveis:")
            print("PE - Pagamento eletrônico")
            print("CE - Cobrança estrutural")
            print("EXT - Extrato")
            print("Inbox")
    else :
        print("Este banco ainda não é aceito pelo sistema")
        print("-" * 20)
        print("Bancos aceitos:")
        print("Itaú - 341")
        x = 3

finally:
    try:
        if x == ("1") :
            caminho_novo = str("C:/VAN_STAGE/{}/{}/{}/{}/{}".format(processar, banc, op_usu.upper(),rem_ou_ret.upper(), dat_atual))
            logging.info("Operacao Realizada-{}-{}-{} ".format(banc.upper(),op_usu.upper(), rem_ou_ret.upper()))
            logging.info("Caminho da Pasta - {}".format(caminho_novo))
            print(caminho_novo)
            CriarCaminho(caminho_novo, caminho_original)

        elif x == ("2"):
            caminho_novo = str("C:/VAN_STAGE/{}/{}/{}".format(banc, op_usu.upper(), dat_atual))
            logging.info("Operacao Realizada-{}-{}".format(banc.upper(),op_usu.upper()))
            logging.info("O caminho da Pasta - {}".format(caminho_novo))
            print(caminho_novo)
            CriarCaminho(caminho_novo, caminho_original)
        elif x == ("3"):
            print("Tente novamente.")

    except NameError:
        pass
    except OSError:
        print("Arquivo não encontrado")
