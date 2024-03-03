# Dados que você deseja salvar
info = input("Enter with a text")

dados = ['linha 1', 'linha 2' ]

# Nome do arquivo
nome_arquivo = "arquivo.txt"

# Abre o arquivo no modo de escrita ('w')
with open(nome_arquivo, 'a') as arquivo:
    # Escreve cada linha dos dados no arquivo
    for linha in dados:
        arquivo.write(linha + '\n')  # Adiciona uma quebra de linha ao final de cada linha

print(f"As informações foram salvas no arquivo '{nome_arquivo}'.")
