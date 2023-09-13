import shutil
import os   

pasta_origem = "/caminho/para/a/pasta/origem"
pasta_destino = "/caminho/para/a/pasta/destino"

arquivos = os.listdir(pasta_origem)

for arquivo in arquivos:
    caminho_origem = os.path.join(pasta_origem, arquivo)
    caminho_destino = os.path.join(pasta_destino, arquivo)

    if os.path.isfile(caminho_origem):
        try:
            shutil.copy(caminho_origem, caminho_destino)
            print(f"Arquivo {arquivo} copiado com sucesso!")
        except Exception as e:
            print(f"Erro ao copiar {arquivo}: {str(e)}")

print("Concluido")
