from time import sleep
from src.Colors import Color
import random

hist = ' '
pers = ''
esc = ''
perd = 'lorem ipsum'
res = ''
perdao = ['S', 'N']
armas = ('MACHADO', 'ESPADA', 'CAJADO')
escmaq = random.choice(armas)
try:
    print(f'{Color.RED}|-|'*30)
    print(f'{Color.CYAN}{"FURIA DE DEUSES":-^90}')
    print(f'{Color.RED}|-|'*30)
    sleep(2)
    print(f'\n{Color.BLUE}A 3 mil anos atrás, ao norte do deserto de shurima acontecia uma batalha de irmãos jamais vista pela humanidade...\n')
    sleep(5)
    print(f'De um lado estava dessa batalha se encontrava o impulsivo e sanguinário deus {Color.YELLOW}Renekton{Color.BLUE}.\n')
    sleep(4)
    print('Um crocodilo ambicioso e impetuoso, que na busca por poder, acabou assassinando seu próprio pai com apenas um golpe.\n')
    sleep(3)
    print('...')
    sleep(2)
    print('...')
    sleep(2)
    print('...')
    print(f'Do outro lado estava o sábio e pacato deus {Color.GREEN}Nasus{Color.BLUE}, um chacal que apesar de amar seu irmão mais novo {Color.YELLOW}Renekton{Color.BLUE}.\n')
    sleep(3)
    print('Foi obrigado a prende-lo em uma prisão dimensional, a fim de parar a ira de seu irmão.\n')
    sleep(3)
    while pers != 'NASUS' and pers !='RENEKTON':
        pers= str(input(f'{Color.RESET}Escolha um personagem: [ {Color.GREEN}Nasus{Color.BLUE}{Color.RESET} | {Color.YELLOW}Renekton{Color.BLUE}{Color.RESET} ]')).upper().strip()
        if pers not in 'NASUS''RENEKTON':
            print('Não entendi sua resposta, por favor ', end='')
    print(f'\n{Color.RESET}{"2 DIAS ATRÁS":-^60}\n')
    if pers == 'RENEKTON':
        print(f'{Color.YELLOW}GRRRRRRRRRR... Não aguento mais esse lugar escuro...\n')
        sleep(3)
        print(f'{Color.RESET}[ Por consequência do tempo, a prisão se enfraqueceu e {Color.YELLOW}Renekton conseguiu se libertar]\n')
        sleep(4)
        print(f'{Color.YELLOW}Agora que saí daqui, preciso encontrar e matar meu irmão mais velho...\n')
        sleep(3)
        print(f'...ele me traiu e me prendeu para roubar meu império!\n')
        sleep(4)
        print(f'Assim que encontra-lo, irei cortar sua cabeça fora e devorar seu corpo...\n')
        sleep(2)
        print(f'{Color.RESET}[{Color.YELLOW}Renekton{Color.RESET} corre em direção a Shurima, ao chegar encontra seu irmão dentro do saguão principal]\n')
        sleep(3)
        print(f'{Color.YELLOW}Olá irmãozinho... Estava morrendo de saudades de você, seu cachorrão...(contém ironias!)\n')
        sleep(4)
        print(f'{Color.RESET}[{Color.YELLOW}Renekton{Color.RESET} olha para a parede e avista três armas]\n')
        sleep(2)
        while esc != 'MACHADO' and esc != 'ESPADA' and esc != 'CAJADO':
            esc = str(input(f'Escolha uma arma: [ {Color.RED}Machado{Color.BLUE} | {Color.RED}Espada{Color.BLUE} | {Color.RED}Cajado{Color.BLUE} ]')).strip().upper()
            if esc != 'MACHADO' and esc != 'ESPADA' and esc != 'CAJADO':
                print(f'{Color.RED}{esc}{Color.BLUE} não estava na parede, por favor, escolha entre {Color.RED}Machado{Color.BLUE} | {Color.RED}Espada{Color.BLUE} | {Color.RED}Cajado{Color.BLUE}.\n')
    #Apenas para definir o artigo da arma do usuário.
        if esc == 'ESPADA':
            art = 'a'
            ssua = 'sua'
        else:
            art = 'o'
            ssua = 'seu'
    #Apenas para definir o artigo da arma da maquina.
        if escmaq == 'ESPADA':
            artmaq = 'a'
        else:
            artmaq = 'o'
        forcusu = random.randint(1, 10)
        forcmaq = random.randint(1, 10)
        print(f'{Color.YELLOW}Renekton{Color.BLUE} pega {art} {Color.RED}{esc.lower()}{Color.BLUE}, e {Color.GREEN}Nasus{Color.BLUE} pegou {artmaq} {Color.RED}{escmaq.lower()}{Color.BLUE}.\n')
        sleep(3)
        print(f'{Color.YELLOW}Renekton{Color.BLUE} pula e golpeia seu irmão com toda a força...\n')
        sleep(3)
        if forcusu > forcmaq:
            print(f'Pela força esmagadora d{art} {ssua} {Color.RED}{esc.lower()}{Color.BLUE}, {Color.YELLOW}Renekton{Color.BLUE} parte {artmaq} {Color.RED}{escmaq.lower()}{Color.BLUE} de seu irmão ao meio e acerta o ombro de seu irmão em cheio\n')
            sleep(5)
            print(f'Ao atingir seu irmão, {Color.GREEN}Nasus{Color.BLUE} cai no chão e pede clemencia, pedindo um tempo para se explicar.\n')
            sleep(3)
            print(f'{Color.YELLOW}Renekton{Color.BLUE}, segurando {ssua} {Color.RED}{esc.lower()}{Color.BLUE}, escuta seu irmão.\n')
            sleep(3)
            print(f'[...{Color.GREEN}Nasus{Color.BLUE} conta que so o prendeu para conter a loucura de seu irmão, e que mesmo fazendo isso sempre o amou...]')
            res = 'GA'
        elif forcusu < forcmaq:
            print(f'Infelizmente seu irmão passou todo esse tempo treinando no templo Shurimane,\n'
                f'e se defende do ataque d{art} {Color.RED}{esc.lower()}{Color.BLUE} de seu irmão, e o derruba no chão.\n')
            sleep(5)
            print(f'Após ter seu irmão no chão, {Color.GREEN}Nasus{Color.BLUE} diz que não deseja mata-lo, e que só o prendeu para poder parar sua loucura.\n')
            res = 'PE'
        elif forcusu == forcmaq:
            print(f'Ao acertar seu irmão, as armas se enroscam e travam uma na outra, aproximando os dois...\n')
            sleep(4)
            print(f'Depois de ter seu irmão sob controle, {Color.GREEN}Nasus{Color.BLUE} conta que so o prendeu para\n'
                'conter a loucura de seu irmão, e que mesmo fazendo isso sempre o amou...\n')
            res = 'EM'
        while perd[0] not in 'S''N':
            perd = str(input(f'{Color.RESET}Depois de escutar {Color.GREEN}Nasus{Color.BLUE}, você escolhe perdoa-lo? {Color.RESET}[ {Color.GREEN}Sim {Color.RESET}| {Color.RED}Não{Color.RESET} ]\n')).upper().strip()
            if perd[0] not in 'S''N':
                print(f'É para responder apenas sim ou não, por favor, tente novamente!')
                sleep(3)
        if perd[0] == 'S':
            print(f'Após perdoar seu irmão, os dois se uniram para reerguer shurima, que foi severamente destruida após muitas guerras por poder!\n')
        elif perd[0] == 'N':
            if res == 'GA':
                print(f'{Color.YELLOW}Renekton{Color.BLUE} resolve não perdoar seu irmão, e atravessa sua face com {art} {Color.RED}{esc.lower()}{Color.BLUE} dele, o matando instantaneamente.\n')
                sleep(4)
                print(f'Após matar seu irmão, {Color.YELLOW}Renekton{Color.BLUE} assume seu império Shurimane, formando um exército imbativel para tomar mais e mais poder!')
                sleep(4)
            elif res == 'PE':
                print(f'Após ver que seu irmão não o perdoaria, {Color.GREEN}Nasus{Color.BLUE} golpeia seu irmão com {artmaq} {Color.RED}{escmaq.lower()}{Color.BLUE}, matando-o instantaneamente.\n')
                sleep(4)
                print(f'Após matar seu irmão, {Color.GREEN}Nasus{Color.BLUE} reuniu os conselheiros e trabalhou incessantemente para reerguer a nação Shurimane.')
                sleep(4)
            elif res == 'EM':
                print(f'Após escutar seu irmão, {Color.YELLOW}Renekton{Color.BLUE} se enfurece mais, soltando de de seu irmão e o atacando novamente.\n')
                sleep(4)
                forcusu = random.randint(1, 10)
                forcmaq = random.randint(1, 10)
                if forcusu > forcmaq:
                    print(f'{Color.YELLOW}Renekton{Color.BLUE} acerta {Color.GREEN}Nasus{Color.BLUE} com {ssua} {Color.RED}{esc.lower()}{Color.BLUE} na barriga, matando seu irmão.')
                    sleep(4)
                    print(f'Após matar seu irmão, {Color.YELLOW}Renekton{Color.BLUE} assume seu império Shurimane, formando um exército imbativel para tomar mais e mais poder!')
                    sleep(4)
                elif forcusu <= forcmaq:
                    print(f'Após ser atacado novamente, {Color.GREEN}Nasus{Color.BLUE} se defende e em seguida, golpeia seu irmão com {ssua} {Color.RED}{escmaq.lower()}{Color.BLUE}, levando {Color.YELLOW}Renekton{Color.BLUE} a morte')
                    sleep(4)
                    print(f'Após matar seu irmão, Nasus reuniu os conselheiros e trabalhou incessantemente para reerguer a nação Shurimane.')
                    sleep(4)
    if pers == 'NASUS':
        print(f'{Color.BLUE}Shurima esta sofrendo com todas essas guerras, precisamos de plano para cessá-las!\n')
        sleep(3)
        print(f'{Color.BLUE}[Por consequência do tempo, a prisão se enfraqueceu e {Color.YELLOW}Renekton{Color.BLUE} conseguiu se libertar]\n')
        sleep(4)
        print(f'{Color.BLUE}Soube que {Color.YELLOW}Renekton{Color.BLUE} escapou da prisão a qual eu o coloquei...\n')
        sleep(3)
        print(f'...acredito que ele virá atrás de mim!\n')
        sleep(3)
        print(f'Preciso me preparar para uma batalha!\n')
        sleep(3)
        print(f'{Color.BLUE}[{Color.YELLOW}Renekton{Color.BLUE} corre em direção a Shurima, ao chegar encontra seu irmão dentro do saguão principal]\n')
        sleep(3)
        print(f'{Color.BLUE}Olá irmão... A que devo essa ilustre visita?\n')
        sleep(4)
        print(f'{Color.BLUE}[{Color.GREEN}Nasus{Color.BLUE} olha para a parede e avista 3 armas]\n')
        sleep(2)
        while esc != 'MACHADO' and esc != 'ESPADA' and esc != 'CAJADO':
            esc = str(input(f'{Color.RESET}Escolha uma arma: [ {Color.RED}Machado{Color.RESET} | {Color.RED}Espada{Color.RESET} | {Color.RED}Cajado{Color.RESET} ]')).strip().upper()
            if esc != 'MACHADO' and esc != 'ESPADA' and esc != 'CAJADO':
                print(f'{Color.RED}{esc.lower()}{Color.BLUE} não estava na parede, por favor, escolha entre Machado | Espada | Cajado.\n')
        #Apenas para definir o artigo da arma do usuário.
        if esc == 'ESPADA':
            art = 'a'
            ssua = 'sua'
        else:
            art = 'o'
            ssua = 'seu'
        #Apenas para definir o artigo da arma da maquina.
        if escmaq == 'ESPADA':
            artmaq = 'a'
            ssuam = 'sua'
        else:
            artmaq = 'o'
            ssuam = 'seu'
        forcusu = random.randint(1, 10)
        forcmaq = random.randint(1, 10)
        print(f'{Color.GREEN}Nasus{Color.BLUE} pega {art} {Color.RED}{esc.lower()}{Color.BLUE}, e {Color.YELLOW}Renekton{Color.BLUE} pegou {artmaq} {Color.RED}{escmaq.lower()}{Color.BLUE}.\n')
        sleep(3)
        print(f'{Color.YELLOW}Renekton{Color.BLUE} pula e golpeia seu irmão com toda a força...\n')
        sleep(3)
        if forcusu < forcmaq:
            print(f'Pela força esmagadora d{artmaq} {ssuam} {Color.RED}{escmaq.lower()}{Color.BLUE}, {Color.YELLOW}Renekton{Color.BLUE} parte {artmaq} {Color.RED}{esc.lower()}{Color.BLUE} de seu irmão ao meio e acerta o ombro de seu irmão em cheio\n')
            sleep(5)
        elif forcusu > forcmaq:
            print(f'Felizmente {Color.GREEN}Nasus{Color.BLUE} passou todo esse tempo treinando no templo Shurimane,\n'
                f'e se defende do ataque d{art} {Color.RED}{escmaq.lower()}{Color.BLUE} de seu irmão, e o derruba no chão.\n')
            sleep(5)
        elif forcusu == forcmaq:
            print(f'Ao acertar {Color.GREEN}Nasus{Color.BLUE}, as armas se enroscam e travam uma na outra, aproximando os dois...\n')
            sleep(4)
        while hist[0] not in 'S''N':
            hist = str(input(f'{Color.RESET}Após ser atacado, você deseja buscar o perdão de seu irmão? [ {Color.GREEN}Sim {Color.RESET}| {Color.RED}Não {Color.RESET}]')).upper().strip()
            print(f'')
            if hist[0] not in 'S''N':
                print(f'É para responder apenas sim ou não, por favor, tente novamente!')
                sleep(3)
        if hist[0] == 'S' and forcusu < forcmaq:
            print(f'{Color.BLUE}Após ser atingido por seu irmão, {Color.GREEN}Nasus{Color.BLUE} cai no chão e pede clemencia, pedindo um tempo para se explicar.\n')
            sleep(3)
            print(f'{Color.YELLOW}Renekton{Color.BLUE}, segurando {ssuam} {Color.RED}{esc.lower()}{Color.BLUE}, escuta seu irmão.\n')
            sleep(3)
            print(f'[...{Color.GREEN}Nasus{Color.BLUE} conta que so o prendeu para conter a loucura de seu irmão, e que mesmo fazendo isso sempre o amou...]\n')
            sleep(3)
            perdre = random.choice(perdao)
            if perdre == 'S':
                print(f'Após ouvir seu irmão, {Color.YELLOW}Renekton{Color.BLUE} entende suas motivações e o perdoa.\n')
                sleep(3)
                print(f'Os dois se uniram para reerguer shurima, que foi severamente destruida após muitas guerras por poder!\n')
            elif perdre == 'N':
                print(f'{Color.YELLOW}Renekton{Color.BLUE} resolve não perdoar seu irmão, e atravessa sua face com {artmaq} {Color.RED}{escmaq.lower()}{Color.BLUE} dele, o matando instantaneamente.\n')
                sleep(4)
                print(f'Após matar seu irmão, {Color.YELLOW}Renekton{Color.BLUE} assume seu império Shurimane, formando um exército imbativel para tomar mais e mais poder!')
                sleep(4)
        elif hist[0] == 'S' and forcusu > forcmaq:
            print(f'Após ter seu irmão no chão, {Color.GREEN}Nasus{Color.BLUE} diz que não deseja mata-lo, e que só o prendeu para poder parar sua loucura.\n')
            sleep(4)
            perdre = random.choice(perdao)
            if perdre == 'S':
                print(f'Após ouvir seu irmão, {Color.YELLOW}Renekton{Color.BLUE} entende suas motivações e o perdoa.\n')
                sleep(3)
                print(f'Os dois se uniram para reerguer shurima, que foi severamente destruida após muitas guerras por poder!\n')
            elif perdre == 'N':
                print(f'Depois de não ser perdoado por seu irmão, {Color.GREEN}Nasus{Color.BLUE} atravessa {ssua} {Color.RED}{esc.lower()}{Color.BLUE} na cabeça dele, dando fim a ameaça que {Color.YELLOW}Renekton{Color.BLUE} representava...\n')
                sleep(3)
                print(f'Após derrotar seu irmão, Nasus se reuniu com conselheiros para estabelecer um plano para reerguer Shurima.')
        elif hist[0] == 'S' and forcusu == forcmaq:
            print(f'Depois de ter seu irmão sob controle, Nasus conta que so o prendeu para\n'
                'conter a loucura de seu irmão, e que mesmo fazendo isso sempre o amou...\n')
            perdre = random.choice(perdao)
            if perdre == 'S':
                print(f'Após ouvir seu irmão, {Color.YELLOW}Renekton{Color.BLUE} entende suas motivações e o perdoa.\n')
                sleep(3)
                print(f'Os dois se uniram para reerguer shurima, que foi severamente destruida após muitas guerras por poder!\n')
                sleep(4)
            elif perdre == 'N':
                sleep(3)
                print('Após escutar seu irmão, \033[1:33mRenekton\033[1:34m prefere morrer que perdoá-lo...')
                sleep(3)
                print('...')
                sleep(3)
                print(f'Depois de não ser perdoado por seu irmão, {Color.GREEN}Nasus{Color.BLUE} atravessa {ssua} {Color.RED}{esc.lower()}{Color.BLUE} na cabeça dele, dando fim a ameaça que {Color.YELLOW}Renekton{Color.BLUE} representava...\n')
                sleep(3)
                print(
                    'Após derrotar seu {Color.YELLOW}Renekton{Color.BLUE}, Nasus se reuniu com conselheiros para estabelecer um plano para reerguer Shurima.')
        elif hist[0] == 'N' and forcusu < forcmaq:
            print(f'{Color.YELLOW}Renekton{Color.BLUE} aproveita seu irmão no chão e o finaliza com um golpe de {Color.RED}{esc.lower()}{Color.BLUE} na cabeça.\n')
            sleep(3)
            print(f'Após derrotar seu irmão, {Color.YELLOW}Renekton{Color.BLUE} assumiu o império shurimane, usando o que restou de seu exército para travar mais guerras...')
        elif hist[0] == 'N' and forcusu > forcmaq:
            print(f'Após derrubar {Color.YELLOW}Renekton{Color.BLUE}, {Color.GREEN}Nasus{Color.BLUE} atravessa {ssua} {Color.RED}{esc.lower()}{Color.BLUE} na cabeça de seu irmão, dando fim a ameaça que {Color.YELLOW}Renekton{Color.BLUE} representava...\n')
            sleep(3)
            print(f'Após derrotar seu irmão, {Color.GREEN}Nasus{Color.BLUE} se reuniu com conselheiros para estabelecer um plano para reerguer Shurima.')
        elif hist[0] == 'N' and forcusu == forcmaq:
            print(f'{Color.YELLOW}Renekton{Color.BLUE} se enfurece mais, soltando de de seu irmão e o atacando novamente.\n')
            sleep(4)
            forcusu = random.randint(1, 10)
            forcmaq = random.randint(1, 10)
            if forcusu <= forcmaq:
                print(f'{Color.YELLOW}Renekton{Color.BLUE} acerta {Color.GREEN}Nasus{Color.BLUE} com {ssuam} {Color.RED}{escmaq.lower()}{Color.BLUE} na barriga, matando seu irmão.\n')
                sleep(4)
                print(f'Após matar seu irmão, {Color.YELLOW}Renekton{Color.BLUE} assume seu império Shurimane, formando um exército imbativel para tomar mais e mais poder!')
                sleep(4)
            elif forcusu > forcmaq:
                print(f'Após ser atacado novamente, {Color.GREEN}Nasus{Color.BLUE} se defende e em seguida, golpeia seu irmão com {ssuam} {Color.RED}{escmaq.lower()}{Color.BLUE}, levando {Color.YELLOW}Renekton{Color.BLUE} a morte\n')
                sleep(4)
                print(f'Após matar seu irmão, {Color.GREEN}Nasus{Color.BLUE} reuniu os conselheiros e trabalhou incessantemente para reerguer a nação Shurimane.')
                sleep(4)
    print(f'\n{Color.CYAN}{"FIM":=^60}')
except KeyboardInterrupt: print(f"{Color.RESET}\nA fúria dos deuses foi interrompida :(")
except Exception as err: print(f"{Color.RESET}\nErro: {Color.RED}{err}")
