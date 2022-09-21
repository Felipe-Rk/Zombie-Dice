from random import randint


def pegarDadosVerde():
    return ("C", "P", "C", "T", "P", "C")

def pegarDadosAmarelo():
    return ("T", "P", "C", "T", "P", "C")

def pegarDadosVermelhos():
    return ("T", "P", "T", "C", "P", "T")

def initDadosCopo(copo):
    # colocar dados verdes no copo
    for i in range(0, 6):
        copo.append(pegarDadosVerde())

        # colocar dados amarelos no copo
    for i in range(0, 4):
        copo.append(pegarDadosAmarelo())

    # colocar dados vermelhos no copo
    for i in range(0, 3):
        copo.append(pegarDadosVermelhos())

        return copo

def pegarDadosCopo(copo):
    # Quantidade de dados no copo
    if len(copo) != 0:
        numDados = (len(copo) - 1)
        index = randint(0, numDados)
        dado = copo[index]
        del (copo[index])
        return dado, copo
    else:
        print("Copo Vazio!!")
        return -1, copo

def lancarDado(dado):
    faceDado = randint(0, 5)
    if dado[faceDado] == "C":
            print("Cerebro!!!")
            return 'C'
    elif dado[faceDado] == "T":
            print("Tiro!!!")
            return 'T'
    else:
            print("Passos!!!")
            return 'P'

def mostrarDadosCopo(copo):
    listDado = []
    for dado in copo:
        if dado == ("C", "P", "C", "T", "P", "C"):
                listDado.append("verde")
        elif dado == ("T", "P", "C", "T", "P", "C"):
                listDado.append("amarelo")
        else:
                listDado.append("vermelho")
                print(listDado)

def mostrarDado(dado):
    if dado == ("C", "P", "C", "T", "P", "C"):
        print("verde")
    elif dado == ("T", "P", "C", "T", "P", "C"):
        print("amarelo")
    else:
        print("vermelho")

def verificarScore(primeiro, segundo, terceiro):
    tiro = 0
    cerebro = 0
    passos = 0
    # primeiro dado
    if primeiro == "C":
        cerebro += 1
    elif primeiro == "T":
        tiro += 1
    else:
        passos += 1

    # segundo dado
    if segundo == "C":
        cerebro += 1
    elif segundo == "T":
        tiro += 1
    else:
        passos += 1

    # terceiro dado
    if terceiro == "C":
        cerebro += 1
    elif terceiro == "T":
        tiro += 1
    else:
        passos += 1
    return cerebro, tiro, passos

#Apresentação do jogo
print("zombie dice")
print("bem vindos ao zombie dice")
print("protótico criado por Felipe Roiko Felix da Silva!")
print("Turma : 11100010563_20222_01 / Professor Galbas!")

# Copo vazio
copo = []
copo = initDadosCopo(copo)
listPlayers = []
numPlayers = 0
while (numPlayers < 2):
        try:

            numPlayers = int(input("Digite o numero de jogadores: "))
            if (numPlayers < 2):
                print(("devem jogar no minimo 2 jogadores"))

        except ValueError:
            print("valor invalido,somente numeros")

        print("Agora Gritem ZUMMMBIEEEEEE, Quem Gritar mais alto, inicia colocando seu nome")

        if numPlayers >= 2:
            for ind in range (0, numPlayers):
                    nome = input("Entre com o nome do jogador: ").upper()
                    cerebro = 0
                    tiro = 0
                    player = [ind, nome, cerebro, tiro]
                    listPlayers.append(player)

play = True
while (play):
        for player in listPlayers:
            cod = player[0]
            nome = player[1]
            print("*-*-*-*-*-*-*-*-*-- Player " + nome +  "--*-*-*-*-*-*-*-*-*")
            mostrarDadosCopo(copo)
            turno = True
            # Para os dados com face "passos"
            blockDado1 = True
            blockDado2 = True
            blockDado3 = True

            primeiroDado = -1
            segundoDado = -1
            terceiroDado = -1

            while (turno):
                playGame = input("Continuar ou sair do jogo:: sim - continuar ou nao sair do jogo: ").upper()
                if playGame == "S" or playGame == "SIM":
                    pass
                else:
                    turno = False
                    play = False
                    break
                print("Dados Sorteados:")
                if blockDado1:
                    primeiroDado, copo = pegarDadosCopo(copo)
                mostrarDado(primeiroDado)
                if blockDado2:
                    segundoDado, copo = pegarDadosCopo(copo)
                mostrarDado(segundoDado)
                if blockDado3:
                    terceiroDado, copo = pegarDadosCopo(copo)
                mostrarDado(terceiroDado)

                print("Mostrar Dados Copo:")
                mostrarDadosCopo(copo)

                one = ""
                two = ""
                three = ""
                # play dice
                if primeiroDado != -1:
                    one = lancarDado(primeiroDado)
                if segundoDado != -1:
                    two = lancarDado(segundoDado)
                if terceiroDado != -1:
                    three = lancarDado(terceiroDado)

                # Para os dados com face "passos"
                blockDado1 = True
                blockDado2 = True
                blockDado3 = True

                cerebro, tiro, passos = verificarScore(one, two, three)

                # Verificar se a vítima escapou
                if passos > 0:
                    if one == "P":
                        blockDado1 = False
                    if two == "P":
                        blockDado2 = False
                    if three == "P":
                        blockDado3 = False

                listPlayers[cod][2] = player[2] + cerebro
                listPlayers[cod][3] = player[3] + tiro
                print("Player: " + listPlayers[cod][1])
                print("Cerebro: " + str(listPlayers[cod][2]))
                print("Tiro: " + str(listPlayers[cod][3]))

                if listPlayers[player[0]][3] > 2:
                    print("Voce morreu!!!\n")
                    listPlayers[player[0]][2] = 0
                    listPlayers[player[0]][3] = 0
                    copoReset = []
                    copo = initDadosCopo(copoReset)
                    mostrarDadosCopo(copo)
                    turno = False

                if listPlayers[player[0]][2] > 12:
                        print("Parabens, voce venceu!!!\n")
                        play = False
                        turno = False

                if turno:
                        continueTurno = input("Voce deseja continuar? (s - sim / n - nao)").upper()
                        if continueTurno == "S" or continueTurno == "SIM":
                            pass
                        else:
                            listPlayers[player[0]][3] = 0
                            copoReset = []
                            copo = initDadosCopo(copoReset)
                            mostrarDadosCopo(copo)
                            turno = False




