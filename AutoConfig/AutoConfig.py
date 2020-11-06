import os
from clean import clean
from downloadFile import downloadGameFile
from csGo import csGo
from r6 import r6

try:
    clean()
    name = input("Digite o nome do player: ").upper()
    clean()
    game = input("Digite de qual jogo quer as configurações como exemplos abaixo\nPara Counter Strike Global Offensive digite ➡  CS \nPara Rainbow Six Siege digite ➡  R6\nDigite: ").upper()

    fileTxt = downloadGameFile(game, name)

    if(game == "CS"):
        csGo(fileTxt)
    elif(game == "R6"):
        r6(fileTxt)

except:
    clean()
    print("Nome do jogador pode estar inválido ou ele não tem configurações nesse jogo 😢")