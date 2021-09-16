from datetime import datetime
import os
import shutil
import logging

#-----------Configuração de logging-------------#
logging.basicConfig(filename='C://Users/Patricia Moretto/Desktop/TESTES/Logging.log', level=logging.DEBUG,
                    format='%(name)s %(levelname)s %(asctime)s %(message)s',
                    filemode='a')
#-----------------------------------------------#

#-----------Função que movimenta os arquivos----#
def CriarCaminho(caminho_de_destino, caminho_original):

    for root, dirs, files in os.walk(caminho_original):
    

        for file in files: 
            old_file_path = os.path.join(root, file)
            print(old_file_path)
            new_file_path = os.path.join(caminho_de_destino)
            print(new_file_path)

            if file in files:
                print(old_file_path)
                print(new_file_path)

                shutil.move(old_file_path, new_file_path)
                
                print("file {} movido com sucesso".format(file))
                logging.info("Operacao Realizada-{} - {}".format(caminho_de_destino_CE, file))
                logging.info("Caminho da Pasta - {} - {}".format(caminho_de_destino_PE, file))               
#-----------------------------------------------#

#-----------Variaveis para a função-------------#
dat_atual = datetime.today().strftime('%m/%d')
caminho_de_CE = "C:/VAN_STAGE/Processar/341/CE/REM/{}".format( dat_atual)
caminho_de_PE = "C:/VAN_STAGE/Processar/341/PE/REM/{}".format( dat_atual)
caminho_de_destino_CE = "/var/www/clients/client1/web1/home/prbrasenior/Dados_ftp/"
caminho_de_destino_PE = "/var/www/clients/client1/web1/home/prbrasenior/Dados_ftp/"
#-----------------------------------------------#

#-----------Chamando a fução--------------------#
CriarCaminho(caminho_de_destino_CE, caminho_de_CE)
CriarCaminho(caminho_de_destino_PE, caminho_de_PE)
#-----------------------------------------------#