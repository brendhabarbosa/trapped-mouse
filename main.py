from maze import Maze, inicializar_labirinto

print("Bem-vindo ao Labirinto!")

escolha = input(
    "Deseja inserir o labirinto manualmente (M) ou ler de um arquivo (A)? "
).strip().upper()

if escolha == "M":
    linhas = []

    print(
        "Digite o labirinto linha por linha "
        "(use '0' para caminhos, '1' para paredes, "
        "'e' para a saída e 'm' para o rato)."
    )
    print("Digite uma linha vazia para finalizar:")

    while True:
        linha = input()

        if linha == "":
            break

        for caractere in linha:
            if caractere not in ["0", "1", "e", "m"]:
                print("Caractere inválido no labirinto.")
                exit()

        linhas.append(linha)

    labirintos = [linhas]

elif escolha == "A":
    entrada = input("Digite o caminho do arquivo do labirinto: ")

    with open(entrada, "r") as arquivo:
        linhas = []
        labirintos = []

        for linha in arquivo:
            linha = linha.strip()

            if linha == "":
                if linhas:
                    labirintos.append(linhas)
                    linhas = []
                continue

            for caractere in linha:
                if caractere not in ["0", "1", "e", "m"]:
                    print("Caractere inválido no labirinto.")
                    exit()

            linhas.append(linha)

        if linhas:
            labirintos.append(linhas)

else:
    print("Opção inválida.")
    exit()

for linhas in labirintos:
    maze = inicializar_labirinto(linhas)
    labirinto = Maze(maze)

    labirinto.exitMaze()

    for linha in labirinto.maze:
        print(linha)

    print()