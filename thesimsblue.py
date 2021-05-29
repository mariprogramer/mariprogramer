import random


class Relogio:
    def __init__(self):
        self.horas = 17
        self.minutos = 0

    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d}"

    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1

    def atrasado(self):
        return (self.horas > 22 or (self.horas == 22 and self.minutos > 0))


class Dormir:
    def __init__(self):
        self.cansado = True
        self.sujo = True
        self.fome = True
        self.sono = True
        self.sanidade = 100


class Personagem(Dormir):
    def __init__(self):
        super().__init__()
        self.PassearCachorro = True
        self.Estudar = True
        self.LavarRoupa = True
        self.LigarFamilia = True
        self.VarrerAcasa = True
        self.ATv = True
        self.Escrever = True
        self.ComprarRoupa = True
        self.Cinema = True
        

    def __str__(self):
        if dia == 1:
            return "Ele está ou precisa: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ cansado" if self.cansado else "\n⚫ Descansado")+("\n⚫ Com sono" if self.sono else "\n⚫ Ele dormiu." )+("\n⚫ Precisando comprar roupas" if self.ComprarRoupa else "\n⚫ Renovou seu guarda-roupa")+("\n⚫ Devendo um passeio para o cachorro " if self.PassearCachorro else "\n⚫ Passeou com Thor ")+("\n⚫ Ver TV " if self.ATv else "\n⚫ Viu TV. ")+("\n⚫ E sua sanidade esta em " + str(self.sanidade)) + "% "
        if dia == 2:
            return "Ele está ou precisa: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ cansado" if self.cansado else "\n⚫ Descansado")+("\n⚫ Com sono" if self.sono else "\n⚫ Ele dormiu." )+("\n⚫ Estudar" if self.Estudar else "\n⚫ Ja estudou")+("\n⚫ Lavar roupa" if self.LavarRoupa else "\n⚫ Roupas limpas")+("\n⚫ Ligar para a familia" if self.LigarFamilia else "\n⚫ Telefonou")+(f"\n⚫ E sua sanidade esta em " + str(self.sanidade)) + "% "
        if dia == 3:
            return "Ele está ou precisa: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ cansado" if self.cansado else "\n⚫ Descansado")+("\n⚫ Com sono" if self.sono else "\n⚫ Ele dormiu." )+("\n⚫ Devendo um passeio para o cachorro " if self.PassearCachorro else "\n⚫ Passeou com Thor ")+("\n⚫ Escrever no diário" if self.Escrever else "\n⚫ Descreveu seu dia")+("\n⚫ Ver TV " if self.ATv else "\n⚫ Viu TV. ")+(f"\n⚫ E sua sanidade esta em " + str(self.sanidade)) + "% "
        if dia == 4:
            return "Ele está ou precisa: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ cansado" if self.cansado else "\n⚫ Descansado")+("\n⚫ Com sono" if self.sono else "\n⚫ Ele dormiu." )+("\n⚫ Ir ao cinema" if self.Cinema else "\n⚫ O filme foi ótimo!!!!!")+("\n⚫ Varrer a casa" if self.VarrerAcasa else "\n⚫ Chão limpo")+(f"\n⚫ E sua sanidade esta em " + str(self.sanidade)) + "% "
        if dia == 5:
            return "Ele está ou precisa: " + ("\n⚫ Sujo" if self.sujo else "\n⚫ Limpo")+("\n⚫ Com" if self.fome else "\n⚫ Sem")+" fome"+("\n⚫ cansado" if self.cansado else "\n⚫ Descansado")+("\n⚫ Com sono" if self.sono else "\n⚫ Ele dormiu." )+("\n⚫ Devendo um passeio para o cachorro " if self.PassearCachorro else "\n⚫ Passeou com Thor ")+("\n⚫ Escrever no diário" if self.Escrever else "\n⚫ Descreveu seu dia")+("\n⚫ Ver TV " if self.ATv else "\n⚫ Viu TV. ")+(f"\n⚫ E sua sanidade esta em " + str(self.sanidade)) + "% "

if(__name__ == "__main__"):
    dia = 0
    relogio = Relogio()
    personagem = Personagem()
    while True:
        dia += 1
        relogio.horas = 17
        relogio.minutos = 0
        while dia == 1:
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            print("São "+str(relogio)+" do Dia "+str(dia) +
                  f". {nome} tem que ir dormir às 22:00.")
            print(personagem)
            print("")
            print("Ações:")
            print("1 - Tomar banho e escovar os dentes")
            print("2 - Jantar")
            print("3 - Comprar roupas")
            print("4 - Levar o cachorro para passear")
            print("5 - Assistir TV")
            print("6 - Dormir")
            print("0 - Sair do jogo")
            opcao = input("Escolha sua ação:")
            if opcao == '1':
                if personagem.ComprarRoupa == False:
                    print(
                        '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                    print(
                        '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                    print(
                        '┃                      ┃Banho e Escovar os Dentes...┃                  ┃')
                    print(
                        '┃         _            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
                    print(
                        '┃       _|___                _______  _______               _          ┃')
                    print(
                        '┃      |_/_\_|              |_o_|_o_||_o_|_o_|             |o|         ┃')
                    print(
                        '┃       || ||               |___o___||___o___|          ___| |         ┃')
                    print(
                        '┃       ||=||               |___o___||___o___|         (    .‘         ┃')
                    print(
                        '┃       || ||                ||   ||  ||   ||           )__(           ┃')
                    print(
                        '┃══════════════════════════════════════════════════════════════════════┃')
                    print(
                        '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                    print()

                    personagem.sujo = False
                    d4 = random.randint(1, 4)
                    if d4 == 1:
                        print(
                            'A resistencia do chuveiro queimou e você teve que arrumar, você permanece sujo!')
                        personagem.sujo = True
                        relogio.avancaTempo(15)
                        personagem.sanidade -= 5
                    elif d4 != 1:
                        relogio.avancaTempo(45)        
            elif opcao == '2':
                if personagem.ComprarRoupa == False:
                    print(
                        '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                    print(
                        '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                    print(
                        '┃                      ┃         Jantando..         ┃                  ┃')
                    print(
                        '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
                    print(
                        '┃                        ;)( ;                                         ┃')
                    print(
                        '┃                       :----:     o8Oo./                              ┃')
                    print(
                        '┃                      C|====| ._o8o8o8Oo_.                            ┃')
                    print(
                        '┃                       |    |  \========/                             ┃')
                    print(
                        '┃                       `----‘   ‘------‘                              ┃')
                    print(
                        '┃══════════════════════════════════════════════════════════════════════┃')
                    print(
                        '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                    print()

                    personagem.fome = False
                    d4 = random.randint(1, 4)
                    if d4 == 1:
                        print('O arroz queimou e você ainda não saciou sua fome')
                        personagem.fome = True
                        relogio.avancaTempo(10)
                        personagem.sanidade -= 5
                    elif d4 != 1:
                        relogio.avancaTempo(45)
            elif opcao == '3':
                personagem.ComprarRoupa = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'Devido ao transito você levou mais tempo do que o necessário')
                    relogio.avancaTempo(135)
                if d4 != 1:
                    relogio.avancaTempo(120)
            elif opcao == '4':
                if personagem.ComprarRoupa == False:
                    personagem.PassearCachorro = False
                    relogio.avancaTempo(30)

            elif opcao == '5':
                if personagem.ComprarRoupa == False:
                    print(
                        '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                    print(
                        '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                    print(
                        '┃                      ┃     Indo para o Trabalho...┃               ■■■┃')
                    print(
                        '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛             ■■■■■┃')
                    print(                ##VAI NO COMEÇO "VOLTANDO DO TRABALHO"
                        '┃                                                               ■■■■■■■┃')
                    print(
                        '┃                           ____________                     ╔═════════┃')
                    print(
                        '┃      ◙     ©           _/_|[][][][][] |                    ║[ ]   [ ]┃')
                    print(
                        '┃     /█\    ║          (      Onibus   |                    ║  ╔══╗   ┃')
                    print(
                        '┃     / \    ║        =--OO-------OO--=dwb                   ║  ║• ║   ┃')
                    print(
                        '┃═══╦════════╬═══════════════════════════════════════════════╠══╩══╩═══┃')
                    print(
                        '┗━━━╨━━━━━━━━╨━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╨━━━━━━━━━┛')
                    print()
                
                    personagem.ATv == False
                    personagem.cansado == False
                    relogio.avancaTempo(60)

            elif opcao == "6":
                if personagem.ComprarRoupa == False:
                    personagem.sono == False
                    if personagem.fome == True:
                        personagem.sanidade -= 10
                    if personagem.sujo == True:
                        personagem.sanidade -= 10
                    if personagem.cansado== True:
                        personagem.sanidade -= 10
                    if personagem.PassearCachorro == True:
                        personagem.sanidade -= 10
                    if personagem.ComprarRoupa == True:
                        personagem.sanidade -= 10    
                    if relogio.atrasado():
                        personagem.sanidade -= 15
                    print(
                        "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                    print(f"{nome} foi dormir no seguinte estado: ")
                    print(personagem)
                    print(
                        "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                    if 0 < personagem.sanidade < 80:
                        print(f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem.sanidade,
                            '%, cuidado! você não pode zerar sua sanidade!')
                    if 80 <= personagem.sanidade < 90:
                        print(
                            f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem.sanidade, '%')
                    if personagem.sanidade >= 90:
                        print(f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem.sanidade,
                            '%'' muito bem! continue assim, deixe sua sanidade o \nmais alta possível')
                    break

        while dia == 2:
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            relogio.avancaTempo(60)    
            print("São "+str(relogio)+" do Dia "+str(dia) +
                  f". {nome} tem que ir dormir às 22:00.")
            print(personagem)
            print("")
            print("Ações:")
            print("1 - Tomar banho e escovar os dentes")
            print("2 - Jantar")
            print("3 - Estudar")
            print("4 - Lavar roupa")
            print("5 - Ligar para a Familia ")
            print("6 - Dormir")
            print("0 - Sair do jogo")
            opcao = input("Escolha sua ação:")
            
            if opcao == '1':
                    print(
                        '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                    print(
                        '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                    print(
                        '┃                      ┃Banho e Escovar os Dentes...┃                  ┃')
                    print(
                        '┃         _            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
                    print(
                        '┃       _|___                _______  _______               _          ┃')
                    print(
                        '┃      |_/_\_|              |_o_|_o_||_o_|_o_|             |o|         ┃')
                    print(
                        '┃       || ||               |___o___||___o___|          ___| |         ┃')
                    print(
                        '┃       ||=||               |___o___||___o___|         (    .‘         ┃')
                    print(
                        '┃       || ||                ||   ||  ||   ||           )__(           ┃')
                    print(
                        '┃══════════════════════════════════════════════════════════════════════┃')
                    print(
                        '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                    print()

                    personagem.sujo = False
                    d4 = random.randint(1, 4)
                    if d4 == 1:
                        print(
                            'A resistencia do chuveiro queimou e você teve que arrumar, você permanece sujo!')
                        personagem.sujo = True
                        relogio.avancaTempo(15)
                        personagem.sanidade -= 5
                    elif d4 != 1:
                        relogio.avancaTempo(45)        
            elif opcao == '2':
                    print(
                        '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                    print(
                        '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                    print(
                        '┃                      ┃         Jantando..         ┃                  ┃')
                    print(
                        '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
                    print(
                        '┃                        ;)( ;                                         ┃')
                    print(
                        '┃                       :----:     o8Oo./                              ┃')
                    print(
                        '┃                      C|====| ._o8o8o8Oo_.                            ┃')
                    print(
                        '┃                       |    |  \========/                             ┃')
                    print(
                        '┃                       `----‘   ‘------‘                              ┃')
                    print(
                        '┃══════════════════════════════════════════════════════════════════════┃')
                    print(
                        '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                    print()

                    personagem.fome = False
                    d4 = random.randint(1, 4)
                    if d4 == 1:
                        print('O arroz queimou e você ainda não saciou sua fome')
                        personagem.fome = True
                        relogio.avancaTempo(10)
                        personagem.sanidade -= 5
                    elif d4 != 1:
                        relogio.avancaTempo(45)
            elif opcao == '3':
                personagem.Estudar = False
                d4 = random.randint(1, 4)
                if d4 == 1:
                    print(
                        'Devido a má conexão você levou mais tempo do que o necessário')
                    relogio.avancaTempo(60)
                    personagem.sanidade -= 5
                if d4 != 1:
                    relogio.avancaTempo(45)
            elif opcao == '4':
                    personagem.LavarRoupa= False
                    relogio.avancaTempo(45)

            elif opcao == '5':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃     Indo para o Trabalho...┃               ■■■┃')
                print(
                    '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛             ■■■■■┃')
                print(                ##VAI NO COMEÇO "VOLTANDO DO TRABALHO"
                    '┃                                                               ■■■■■■■┃')
                print(
                    '┃                           ____________                     ╔═════════┃')
                print(
                    '┃      ◙     ©           _/_|[][][][][] |                    ║[ ]   [ ]┃')
                print(
                    '┃     /█\    ║          (      Onibus   |                    ║  ╔══╗   ┃')
                print(
                    '┃     / \    ║        =--OO-------OO--=dwb                   ║  ║• ║   ┃')
                print(
                    '┃═══╦════════╬═══════════════════════════════════════════════╠══╩══╩═══┃')
                print(
                    '┗━━━╨━━━━━━━━╨━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╨━━━━━━━━━┛')
                print()
            
                personagem.LigarFamilia == False
                personagem.cansado == False
                relogio.avancaTempo(60)

            elif opcao == "6":
                personagem.sono == False
                if personagem.fome == True:
                    personagem.sanidade -= 10
                if personagem.sujo == True:
                    personagem.sanidade -= 10
                if personagem.cansado== True:
                    personagem.sanidade -= 10
                if personagem.Estudar == True:
                    personagem.sanidade -= 10
                if personagem.LavarRoupa == True:
                    personagem.sanidade -= 10   
                if personagem.LigarFamilia == True:
                    personagem.sanidade -= 10     
                if relogio.atrasado():
                    personagem.sanidade -= 15
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                print(f"{nome} foi dormir no seguinte estado: ")
                print(personagem)
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                if 0 < personagem.sanidade < 80:
                    print(f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem.sanidade,
                          '%, cuidado! você não pode zerar sua sanidade!')
                if 80 <= personagem.sanidade < 90:
                    print(
                        f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem.sanidade, '%')
                if personagem.sanidade >= 90:
                    print(f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem.sanidade,
                          '%'' muito bem! continue assim, deixe sua sanidade o \nmais alta possível')
                break
        while dia == 3:
            print(
                "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
            relogio.avancaTempo(60)    
            print("São "+str(relogio)+" do Dia "+str(dia) +
                  f". {nome} tem que ir dormir às 22:00.")
            print(personagem)
            print("")
            print("Ações:")
            print("1 - Tomar banho e escovar os dentes")
            print("2 - Jantar")
            print("3 - Levar o cachorro para passear")
            print("4 - Escrever no diário")
            print("5 - Ver TV")
            print("6 - Dormir")
            print("0 - Sair do jogo")
            opcao = input("Escolha sua ação:")
            
            if opcao == '1':
                    print(
                        '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                    print(
                        '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                    print(
                        '┃                      ┃Banho e Escovar os Dentes...┃                  ┃')
                    print(
                        '┃         _            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
                    print(
                        '┃       _|___                _______  _______               _          ┃')
                    print(
                        '┃      |_/_\_|              |_o_|_o_||_o_|_o_|             |o|         ┃')
                    print(
                        '┃       || ||               |___o___||___o___|          ___| |         ┃')
                    print(
                        '┃       ||=||               |___o___||___o___|         (    .‘         ┃')
                    print(
                        '┃       || ||                ||   ||  ||   ||           )__(           ┃')
                    print(
                        '┃══════════════════════════════════════════════════════════════════════┃')
                    print(
                        '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                    print()

                    personagem.sujo = False
                    d4 = random.randint(1, 4)
                    if d4 == 1:
                        print(
                            'A resistencia do chuveiro queimou e você teve que arrumar, você permanece sujo!')
                        personagem.sujo = True
                        relogio.avancaTempo(15)
                        personagem.sanidade -= 5
                    elif d4 != 1:
                        relogio.avancaTempo(45)        
            elif opcao == '2':
                    print(
                        '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                    print(
                        '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                    print(
                        '┃                      ┃         Jantando..         ┃                  ┃')
                    print(
                        '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                  ┃')
                    print(
                        '┃                        ;)( ;                                         ┃')
                    print(
                        '┃                       :----:     o8Oo./                              ┃')
                    print(
                        '┃                      C|====| ._o8o8o8Oo_.                            ┃')
                    print(
                        '┃                       |    |  \========/                             ┃')
                    print(
                        '┃                       `----‘   ‘------‘                              ┃')
                    print(
                        '┃══════════════════════════════════════════════════════════════════════┃')
                    print(
                        '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
                    print()

                    personagem.fome = False
                    d4 = random.randint(1, 4)
                    if d4 == 1:
                        print('O arroz queimou e você ainda não saciou sua fome')
                        personagem.fome = True
                        relogio.avancaTempo(10)
                        personagem.sanidade -= 5
                    elif d4 != 1:
                        relogio.avancaTempo(45)
            elif opcao == '3':
                personagem.PassearCachorro = False
                relogio.avancaTempo(30)
            elif opcao == "4": 
                personagem.Escrever = False
                relogio.avancaTempo(45)    
            elif opcao == '5':
                print(
                    '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(
                    '┃                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                  ┃')
                print(
                    '┃                      ┃     Indo para o Trabalho...┃               ■■■┃')
                print(
                    '┃                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛             ■■■■■┃')
                print(                ##VAI NO COMEÇO "VOLTANDO DO TRABALHO"
                    '┃                                                               ■■■■■■■┃')
                print(
                    '┃                           ____________                     ╔═════════┃')
                print(
                    '┃      ◙     ©           _/_|[][][][][] |                    ║[ ]   [ ]┃')
                print(
                    '┃     /█\    ║          (      Onibus   |                    ║  ╔══╗   ┃')
                print(
                    '┃     / \    ║        =--OO-------OO--=dwb                   ║  ║• ║   ┃')
                print(
                    '┃═══╦════════╬═══════════════════════════════════════════════╠══╩══╩═══┃')
                print(
                    '┗━━━╨━━━━━━━━╨━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╨━━━━━━━━━┛')
                print()
            
                personagem.ATv == False
                personagem.cansado == False
                relogio.avancaTempo(60)

            elif opcao == "6":
                personagem.sono == False
                if personagem.fome == True:
                    personagem.sanidade -= 10
                if personagem.sujo == True:
                    personagem.sanidade -= 10
                if personagem.cansado== True:
                    personagem.sanidade -= 10
                if personagem.PassearCachorro == True:
                    personagem.sanidade -= 10
                if personagem.Escrever == True:
                    personagem.sanidade -= 10    
                if relogio.atrasado():
                    personagem.sanidade -= 15
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                print(f"{nome} foi dormir no seguinte estado: ")
                print(personagem)
                print(
                    "-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|-=-|")
                if 0 < personagem.sanidade < 80:
                    print(f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem.sanidade,
                          '%, cuidado! você não pode zerar sua sanidade!')
                if 80 <= personagem.sanidade < 90:
                    print(
                        f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem.sanidade, '%')
                if personagem.sanidade >= 90:
                    print(f'{nome} terminou o primeiro estagio do jogo com o sanidade em ', personagem.sanidade,
                          '%'' muito bem! continue assim, deixe sua sanidade o \nmais alta possível')
                break
            elif(opcao == "0"):
                print(
                    '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                print(
                    '                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                      ')
                print(
                    '                      ┃      Obrigado Por Jogar    ┃                      ')
                print(
                    '                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                      ')
                print(
                    '                                                                          ')
                break
            else:
                print("Opção inválida!")
                relogio.avancaTempo(5)
        if(opcao == "0"):
            break
        if dia == 5:
            print(
                '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
            print(
                '                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                      ')
            print(
                '                      ┃      Obrigado Por Jogar    ┃                      ')
            print(
                '                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                      ')
            print(
                '                                                                          ')
        personagem.sujo = True
        personagem.fome = True
        personagem.exercicio = True
        personagem.comida_thor = True
        
