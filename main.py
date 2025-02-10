import base64
from io import BytesIO
from pathlib import Path

from PIL import Image


def converter_para_base64(caminho_origem, caminho_destino):
    if not caminho_origem.exists():
        print(f"Erro: O caminho '{caminho_origem}' não existe.")
        return

    caminho_destino.mkdir(parents=True, exist_ok=True)

    formatos_aceitos = ['.jpg', '.jpeg', '.png']
    for arquivo in caminho_origem.iterdir():
        if arquivo.suffix.lower() in formatos_aceitos:
            with open(arquivo, "rb") as imagem_arquivo:
                encoded_string = base64.b64encode(imagem_arquivo.read()).decode('utf-8')
                caminho_saida = caminho_destino / f"{arquivo.stem}.txt"
                with open(caminho_saida, "w") as arquivo_saida:
                    arquivo_saida.write(encoded_string)
                print(f"Convertido: {arquivo.name} -> {arquivo.stem}.txt")

def base64_to_image(base64_string):
    # Remove o prefixo "data:image" se presente
    if "data:image" in base64_string:
        base64_string = base64_string.split(",")[1]

    # Decodifica a string Base64 em bytes
    image_bytes = base64.b64decode(base64_string)
    return image_bytes

def create_image_from_bytes(image_bytes):
    # Cria um objeto BytesIO para manipular os bytes da imagem
    image_stream = BytesIO(image_bytes)

    # Abre a imagem usando Pillow (PIL)
    image = Image.open(image_stream)
    return image

def converter_de_base64(caminho_origem, caminho_destino):
    if not caminho_origem.exists():
        print(f"Erro: O caminho '{caminho_origem}' não existe.")
        return

    caminho_destino.mkdir(parents=True, exist_ok=True)

    for arquivo in caminho_origem.iterdir():
        if arquivo.suffix == '.txt':
            try:
                with open(arquivo, "r") as arquivo_entrada:
                    encoded_string = arquivo_entrada.read()

                    # Converte Base64 para bytes
                    image_bytes = base64_to_image(encoded_string)

                    # Cria a imagem a partir dos bytes
                    img = create_image_from_bytes(image_bytes)

                    # Salva a imagem com a extensão .png
                    caminho_saida = caminho_destino / f"{arquivo.stem}.png"
                    img.save(caminho_saida)
                    print(f"Convertido: {arquivo.name} -> {arquivo.stem}.png")
            except base64.binascii.Error:
                print(f"Erro: O arquivo {arquivo.name} não contém um BASE64 válido.")
                continue
            except Exception as e:
                print(f"Erro ao processar o arquivo {arquivo.name}: {e}")
                continue

def main():
    print("Deseja converter imagens para BASE64 ou de BASE64 para imagens?")
    escolha = input("Digite 1 para BASE64 ou 2 para imagens: ")

    caminho_origem = Path(input("Digite o caminho da pasta com as imagens/arquivos: "))
    caminho_destino = Path(input("Digite o caminho da pasta para salvar as imagens/arquivos convertidos: "))

    if escolha == '1':
        converter_para_base64(caminho_origem, caminho_destino)
    elif escolha == '2':
        converter_de_base64(caminho_origem, caminho_destino)
    else:
        print("Escolha inválida. Por favor, digite 1 ou 2.")

    print("Conversão concluída com sucesso!")

if __name__ == "__main__":
    main()