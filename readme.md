

# Conversor de Imagens para BASE64 e Vice-Versa

Este é um programa em Python que converte imagens nos formatos **JPG**, **JPEG** e **PNG** para **BASE64** e vice-versa. Ele permite que o usuário selecione o tipo de conversão, o caminho da pasta de origem e o caminho da pasta de destino.

---

## Funcionalidades

- **Conversão de imagens para BASE64**:
  - Converte imagens nos formatos JPG, JPEG e PNG para strings Base64.
  - Salva o resultado em arquivos de texto com a extensão `.txt`.

- **Conversão de BASE64 para imagens**:
  - Converte strings Base64 de volta para imagens nos formatos JPG, JPEG ou PNG.
  - Salva as imagens com a extensão `.png`.

- **Tratamento de erros**:
  - Verifica se os caminhos das pastas existem.
  - Detecta e trata erros ao decodificar Base64 inválido.
  - Exibe mensagens de erro claras para facilitar a depuração.

- **Manipulação segura de caminhos**:
  - Utiliza a biblioteca `pathlib` para garantir compatibilidade entre sistemas operacionais.

---

## Requisitos

- **Python 3.x**:
  - Certifique-se de ter o Python instalado. Você pode baixá-lo em [python.org](https://www.python.org/).

- **Biblioteca Pillow (PIL)**:
  - Instale a biblioteca Pillow para manipulação de imagens:
    ```bash
    pip install pillow
    ```

---

## Como Instalar e Executar

1. **Baixe o código**:
   - Clone este repositório ou faça o download do arquivo `conversor.py`.

2. **Instale as dependências**:
   - No terminal, execute o seguinte comando para instalar a biblioteca Pillow:
     ```bash
     pip install pillow
     ```

3. **Execute o programa**:
   - Navegue até a pasta onde o arquivo `conversor.py` está localizado e execute:
     ```bash
     python conversor.py
     ```

4. **Siga as instruções no terminal**:
   - Escolha o tipo de conversão:
     - Digite `1` para converter imagens para Base64.
     - Digite `2` para converter Base64 para imagens.
   - Informe o caminho da pasta de origem (onde estão os arquivos a serem convertidos).
   - Informe o caminho da pasta de destino (onde os arquivos convertidos serão salvos).

---

## Exemplo de Uso

### Convertendo imagens para Base64:
```bash
Deseja converter imagens para BASE64 ou de BASE64 para imagens?
Digite 1 para BASE64 ou 2 para imagens: 1
Digite o caminho da pasta com as imagens: /home/usuario/imagens
Digite o caminho da pasta para salvar as imagens convertidas: /home/usuario/base64_files
Conversão concluída com sucesso!
```

### Convertendo Base64 para imagens:
```bash
Deseja converter imagens para BASE64 ou de BASE64 para imagens?
Digite 1 para BASE64 ou 2 para imagens: 2
Digite o caminho da pasta com as imagens/arquivos: /home/usuario/base64_files
Digite o caminho da pasta para salvar as imagens/arquivos convertidos: /home/usuario/imagens
Conversão concluída com sucesso!
```

---

## Estrutura do Projeto

Após a execução, a estrutura do projeto pode ficar assim:

```
conversor-base64/
│
├── conversor.py            # Código do programa
├── README.md               # Documentação do projeto
├── imagens/                # Pasta com imagens originais
│   ├── foto1.jpg
│   ├── foto2.png
├── base64_files/           # Pasta com arquivos Base64 convertidos
│   ├── foto1.txt
│   ├── foto2.txt
└── imagens_convertidas/    # Pasta com imagens convertidas de Base64
    ├── foto1.png
    ├── foto2.png
```

---

## Tratamento de Erros

- **Caminhos inválidos**:
  - O programa verifica se os caminhos das pastas existem antes de iniciar a conversão.

- **Base64 inválido**:
  - Se um arquivo `.txt` contiver um Base64 inválido, o programa exibirá uma mensagem de erro e continuará com o próximo arquivo.

- **Erros durante a conversão**:
  - Qualquer erro durante o processo de conversão será exibido no terminal para facilitar a depuração.

---

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests** com melhorias ou correções.

---

## Licença

Este projeto está licenciado sob a Licença Creative Commons (CC BY-NC 4.0). Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Agora o `README.md` está completo e pronto para ser utilizado! Ele fornece todas as informações necessárias para instalar, executar e entender o funcionamento do programa. 😊
