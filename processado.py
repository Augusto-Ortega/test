
from datetime import datetime
import os
import logging
import shutil


#-----------------------------------------------#






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
                logging.info("Operacao Realizada-{} - {}".format(caminho_de_destino_CE, file))
                logging.info("Caminho da Pasta - {} - {}".format(caminho_de_destino_PE, file))
#-----------------------------------------------#
               
#-----------Variaveis para a função-------------#
dat_atual = datetime.today().strftime('%m/%d')
Caminho_de_EXT= "/RETORNOTESTE"
caminho_de_CE = "/RETORNOTESTE"
caminho_de_PE = "/RETORNOTESTE"
caminho_de_destino_CE ="C:/VAN_STAGE/Processado/341/CE/RET/{}".format( dat_atual) 
caminho_de_destino_PE ="C:/VAN_STAGE/Processado/341/PE/RET/{}".format( dat_atual)
Caminho_de_destino_EXT="C:/VAN_STAGE/Processado/341/EXT/RET/{}".format( dat_atual)
#-----------------------------------------------#

#-----------Comando para cirar o caminho--------#
try:
    os.mkdir("caminho_de_destino_PE")
    
except FileExistsError:
    pass
try:
    os.mkdir("caminho_de_destino_CE")
except FileExistsError:
    pass
try:
    os.mkdir("caminho_de_destino_EXT")
except FileExistsError:
    pass
#-----------------------------------------------#

#-----------Chamando a fução--------------------#
CriarCaminho(caminho_de_destino_CE, caminho_de_CE)
CriarCaminho(caminho_de_destino_PE, caminho_de_PE)
#-----------------------------------------------#
