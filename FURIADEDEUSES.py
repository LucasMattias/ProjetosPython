from time import sleep
import random
hist = ' '
pers = ''
esc = ''
perd = 'lorem ipsum'
res = ''
perdao = ['S', 'N']
armas = ('MACHADO', 'ESPADA', 'CAJADO')
escmaq = random.choice(armas)
print('\033[1:31m|-|'*30)
print(f'\033[1:36m{"FURIA DE DEUSES":-^90}')
print('\033[1:31m|-|\033[m'*30)
sleep(2)
print('\n\033[1:34mA 3 mil anos atrás, ao norte do deserto de shurima acontecia uma batalha de irmãos jamais vista pela humanidade...\n')
sleep(5)
print('De um lado estava dessa batalha se encontrava o impulsivo e sanguinario deus \033[1:33mRenekton\033[1:34m.\n')
sleep(4)
print('Um crocodilo ambicioso e impetuoso, que na busca por poder, acabou assassinando seu próprio pai com apenas um golpe.\n')
sleep(3)
print('...')
sleep(2)
print('...')
sleep(2)
print('...')
print('Do outro lado estava o sábio e pacato deus \033[1:32mNasus\033[1:34m, um chacal que apesar de amar seu irmão mais novo \033[1:33mRenekton\033[1:34m.\n')
sleep(3)
print('Foi obrigado a prende-lo em uma prisão dimensional, a fim de parar a ira de seu irmão.\n')
sleep(3)
while pers != 'NASUS' and pers !='RENEKTON':
    pers= str(input('Escolha um personagem: [ \033[1:32mNasus\033[1:34m | \033[1:33mRenekton\033[1:34m ]')).upper().strip()
    if pers not in 'NASUS''RENEKTON':
        print('Não entendi sua resposta, por favor ', end='')
print(f'\n{"2 DIAS ATRÁS":-^60}\n')
if pers == 'RENEKTON':
    print('\033[1:33mGRRRRRRRRRR... Não aguento mais esse lugar escuro...\n')
    sleep(3)
    print('\033[1:34m[Por consequência do tempo, a prisão se enfraqueceu e Renekton conseguiu se libertar]\n')
    sleep(4)
    print('\033[1:33mAgora que saí daqui, preciso encontrar e matar meu irmão mais velho...\n')
    sleep(3)
    print('...ele me traiu e me prendeu para roubar meu império!\n')
    sleep(4)
    print('Assim que encontra-lo, irei cortar sua cabeça fora e devorar seu corpo...\n')
    sleep(2)
    print('\033[1:34m[\033[1:33mRenekton\033[1:34m corre em direção a Shurima, ao chegar encontra seu irmão dentro do saguão principal]\n')
    sleep(3)
    print('\033[1:33mOlá irmãozinho... Estava morrendo de saudades de você, seu cachorrão...(contém ironias!)\n')
    sleep(4)
    print('\033[1:34m[Renekton olha para a parede e avista três armas]\n')
    sleep(2)
    while esc != 'MACHADO' and esc != 'ESPADA' and esc != 'CAJADO':
        esc = str(input('Escolha uma arma: [ \033[1:31mMachado\033[1:34m | \033[1:31mEspada\033[1:34m | \033[1:31mCajado\033[1:34m ]')).strip().upper()
        if esc != 'MACHADO' and esc != 'ESPADA' and esc != 'CAJADO':
            print(f'\033[1:31m{esc}\033[1:34m não estava na parede, por favor, escolha entre \033[1:31mMachado\033[1:34m | \033[1:31mEspada\033[1:34m | \033[1:31mCajado\033[1:34m.\n')
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
    print(f'\033[1:33mRenekton\033[1:34m pega {art} \033[1:31m{esc.lower()}\033[1:34m, e \033[1:32mNasus\033[1:34m pegou {artmaq} \033[1:31m{escmaq.lower()}\033[1:34m.\n')
    sleep(3)
    print('\033[1:33mRenekton\033[1:34m pula e golpeia seu irmão com toda a força...\n')
    sleep(3)
    if forcusu > forcmaq:
        print(f'Pela força esmagadora d{art} {ssua} \033[1:31m{esc.lower()}\033[1:34m, \033[1:33mRenekton\033[1:34m parte {artmaq} \033[1:31m{escmaq.lower()}\033[1:34m de seu irmão ao meio e acerta o ombro de seu irmão em cheio\n')
        sleep(5)
        print('Ao atingir seu irmão, \033[1:32mNasus\033[1:34m cai no chão e pede clemencia, pedindo um tempo para se explicar.\n')
        sleep(3)
        print(f'\033[1:33mRenekton\033[1:34m, segurando {ssua} \033[1:31m{esc.lower()}\033[1:34m, escuta seu irmão.\n')
        sleep(3)
        print('[...\033[1:32mNasus\033[1:34m conta que so o prendeu para conter a loucura de seu irmão, e que mesmo fazendo isso sempre o amou...]')
        res = 'GA'
    elif forcusu < forcmaq:
        print(f'Infelizmente seu irmão passou todo esse tempo treinando no templo Shurimane,\n'
              f'e se defende do ataque d{art} \033[1:31m{esc.lower()}\033[1:34m de seu irmão, e o derruba no chão.\n')
        sleep(5)
        print('Após ter seu irmão no chão, \033[1:32mNasus\033[1:34m diz que não deseja mata-lo, e que só o prendeu para poder parar sua loucura.\n')
        res = 'PE'
    elif forcusu == forcmaq:
        print('Ao acertar seu irmão, as armas se enroscam e travam uma na outra, aproximando os dois...\n')
        sleep(4)
        print('Depois de ter seu irmão sob controle, \033[1:32mNasus\033[1:34m conta que so o prendeu para\n'
              'conter a loucura de seu irmão, e que mesmo fazendo isso sempre o amou...\n')
        res = 'EM'
    while perd[0] not in 'S''N':
        perd = str(input('Depois de escutar \033[1:32mNasus\033[1:34m, você escolhe perdoa-lo? [ Sim | Não ]\n')).upper().strip()
        if perd[0] not in 'S''N':
            print('É para responder apenas sim ou não, por favor, tente novamente!')
            sleep(3)
    if perd[0] == 'S':
        print('Após perdoar seu irmão, os dois se uniram para reerguer shurima, que foi severamente destruida após muitas guerras por poder!\n')
    elif perd[0] == 'N':
        if res == 'GA':
            print(f'\033[1:33mRenekton\033[1:34m resolve não perdoar seu irmão, e atravessa sua face com {art} \033[1:31m{esc.lower()}\033[1:34m dele, o matando instantaneamente.\n')
            sleep(4)
            print('Após matar seu irmão, \033[1:33mRenekton\033[1:34m assume seu império Shurimane, formando um exército imbativel para tomar mais e mais poder!')
            sleep(4)
        elif res == 'PE':
            print(f'Após ver que seu irmão não o perdoaria, \033[1:32mNasus\033[1:34m golpeia seu irmão com {artmaq} \033[1:31m{escmaq.lower()}\033[1:34m, matando-o instantaneamente.\n')
            sleep(4)
            print('Após matar seu irmão, \033[1:32mNasus\033[1:34m reuniu os conselheiros e trabalhou incessantemente para reerguer a nação Shurimane.')
            sleep(4)
        elif res == 'EM':
            print(f'Após escutar seu irmão, \033[1:33mRenekton\033[1:34m se enfurece mais, soltando de de seu irmão e o atacando novamente.\n')
            sleep(4)
            forcusu = random.randint(1, 10)
            forcmaq = random.randint(1, 10)
            if forcusu > forcmaq:
                print(f'\033[1:33mRenekton\033[1:34m acerta \033[1:32mNasus\033[1:34m com {ssua} \033[1:31m{esc.lower()}\033[1:34m na barriga, matando seu irmão.')
                sleep(4)
                print('Após matar seu irmão, \033[1:33mRenekton\033[1:34m assume seu império Shurimane, formando um exército imbativel para tomar mais e mais poder!')
                sleep(4)
            elif forcusu <= forcmaq:
                print(f'Após ser atacado novamente, \033[1:32mNasus\033[1:34m se defende e em seguida, golpeia seu irmão com {ssua} \033[1:31m{escmaq.lower()}\033[1:34m, levando \033[1:33mRenekton\033[1:34m a morte')
                sleep(4)
                print('Após matar seu irmão, Nasus reuniu os conselheiros e trabalhou incessantemente para reerguer a nação Shurimane.')
                sleep(4)
if pers == 'NASUS':
    print('\033[1:32mShurima esta sofrendo com todas essas guerras, precisamos de plano para cessá-las!\n')
    sleep(3)
    print('\033[1:34m[Por consequência do tempo, a prisão se enfraqueceu e \033[1:33mRenekton\033[1:34m conseguiu se libertar]\n')
    sleep(4)
    print('\033[1:32mSoube que \033[1:33mRenekton\033[1:32m escapou da prisão a qual eu o coloquei...\n')
    sleep(3)
    print('...acredito que ele virá atrás de mim!\n')
    sleep(3)
    print('Preciso me preparar para uma batalha!\n')
    sleep(3)
    print('\033[1:34m[\033[1:33mRenekton\033[1:34m corre em direção a Shurima, ao chegar encontra seu irmão dentro do saguão principal]\n')
    sleep(3)
    print('\033[1:32mOlá irmão... A que devo essa ilustre visita?\n')
    sleep(4)
    print('\033[1:34m[\033[1:32mNasus\033[1:34m olha para a parede e avista 3 armas]\n')
    sleep(2)
    while esc != 'MACHADO' and esc != 'ESPADA' and esc != 'CAJADO':
        esc = str(input('Escolha uma arma: [ \033[1:31mMachado\033[1:34m | \033[1:31mEspada\033[1:34m | \033[1:31mCajado\033[1:34m ]')).strip().upper()
        if esc != 'MACHADO' and esc != 'ESPADA' and esc != 'CAJADO':
            print(f'\033[1:31m{esc.lower()}\033[1:34m não estava na parede, por favor, escolha entre Machado | Espada | Cajado.\n')
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
    print(f'\033[1:32mNasus\033[1:34m pega {art} \033[1:31m{esc.lower()}\033[1:34m, e \033[1:33mRenekton\033[1:34m pegou {artmaq} \033[1:31m{escmaq.lower()}\033[1:34m.\n')
    sleep(3)
    print('\033[1:33mRenekton\033[1:34m pula e golpeia seu irmão com toda a força...\n')
    sleep(3)
    if forcusu < forcmaq:
        print(f'Pela força esmagadora d{artmaq} {ssuam} \033[1:31m{escmaq.lower()}\033[1:34m, \033[1:33mRenekton\033[1:34m parte {artmaq} \033[1:31m{esc.lower()}\033[1:34m de seu irmão ao meio e acerta o ombro de seu irmão em cheio\n')
        sleep(5)
    elif forcusu > forcmaq:
        print(f'Felizmente \033[1:32mNasus\033[1:34m passou todo esse tempo treinando no templo Shurimane,\n'
              f'e se defende do ataque d{art} \033[1:31m{escmaq.lower()}\033[1:34m de seu irmão, e o derruba no chão.\n')
        sleep(5)
    elif forcusu == forcmaq:
        print('Ao acertar \033[1:32mNasus\033[1:34m, as armas se enroscam e travam uma na outra, aproximando os dois...\n')
        sleep(4)
    while hist[0] not in 'S''N':
        hist = str(input('Após ser atacado, você deseja buscar o perdão de seu irmão? [ Sim | Não ]')).upper().strip()
        print('')
        if hist[0] not in 'S''N':
            print('É para responder apenas sim ou não, por favor, tente novamente!')
            sleep(3)
    if hist[0] == 'S' and forcusu < forcmaq:
        print('Após ser atingido por seu irmão, \033[1:32mNasus\033[1:34m cai no chão e pede clemencia, pedindo um tempo para se explicar.\n')
        sleep(3)
        print(f'\033[1:33mRenekton\033[1:34m, segurando {ssuam} \033[1:31m{esc.lower()}\033[1:34m, escuta seu irmão.\n')
        sleep(3)
        print('[...\033[1:32mNasus\033[1:34m conta que so o prendeu para conter a loucura de seu irmão, e que mesmo fazendo isso sempre o amou...]\n')
        sleep(3)
        perdre = random.choice(perdao)
        if perdre == 'S':
            print('Após ouvir seu irmão, \033[1:33mRenekton\033[1:34m entende suas motivações e o perdoa.\n')
            sleep(3)
            print('Os dois se uniram para reerguer shurima, que foi severamente destruida após muitas guerras por poder!\n')
        elif perdre == 'N':
            print(f'\033[1:33mRenekton\033[1:34m resolve não perdoar seu irmão, e atravessa sua face com {artmaq} \033[1:31m{escmaq.lower()}\033[1:34m dele, o matando instantaneamente.\n')
            sleep(4)
            print('Após matar seu irmão, \033[1:33mRenekton\033[1:34m assume seu império Shurimane, formando um exército imbativel para tomar mais e mais poder!')
            sleep(4)
    elif hist[0] == 'S' and forcusu > forcmaq:
        print('Após ter seu irmão no chão, \033[1:32mNasus\033[1:34m diz que não deseja mata-lo, e que só o prendeu para poder parar sua loucura.\n')
        sleep(4)
        perdre = random.choice(perdao)
        if perdre == 'S':
            print('Após ouvir seu irmão, \033[1:33mRenekton\033[1:34m entende suas motivações e o perdoa.\n')
            sleep(3)
            print('Os dois se uniram para reerguer shurima, que foi severamente destruida após muitas guerras por poder!\n')
        elif perdre == 'N':
            print(f'Depois de não ser perdoado por seu irmão, \033[1:32mNasus\033[1:34m atravessa {ssua} \033[1:31m{esc.lower()}\033[1:34m na cabeça dele, dando fim a ameaça que \033[1:33mRenekton\033[1:34m representava...\n')
            sleep(3)
            print('Após derrotar seu irmão, Nasus se reuniu com conselheiros para estabelecer um plano para reerguer Shurima.')
    elif hist[0] == 'S' and forcusu == forcmaq:
        print('Depois de ter seu irmão sob controle, Nasus conta que so o prendeu para\n'
              'conter a loucura de seu irmão, e que mesmo fazendo isso sempre o amou...\n')
        perdre = random.choice(perdao)
        if perdre == 'S':
            print('Após ouvir seu irmão, \033[1:33mRenekton\033[1:34m entende suas motivações e o perdoa.\n')
            sleep(3)
            print('Os dois se uniram para reerguer shurima, que foi severamente destruida após muitas guerras por poder!\n')
            sleep(4)
        elif perdre == 'N':
            print(f'Depois de não ser perdoado por seu irmão, \033[1:32mNasus\033[1:34m atravessa {ssua} \033[1:31m{esc.lower()}\033[1:34m na cabeça dele, dando fim a ameaça que \033[1:33mRenekton\033[1:34m representava...\n')
            sleep(3)
            print(
                'Após derrotar seu \033[1:33mRenekton\033[1:34m, Nasus se reuniu com conselheiros para estabelecer um plano para reerguer Shurima.')
    elif hist[0] == 'N' and forcusu < forcmaq:
        print(f'\033[1:33mRenekton\033[1:34m aproveita seu irmão no chão e o finaliza com um golpe de \033[1:31m{esc.lower()}\033[1:34m na cabeça.\n')
        sleep(3)
        print('Após derrotar seu irmão, \033[1:33mRenekton\033[1:34m assumiu o império shurimane, usando o que restou de seu exército para travar mais guerras...')
    elif hist[0] == 'N' and forcusu > forcmaq:
        print(f'Após derrubar \033[1:33mRenekton\033[1:34m, \033[1:32mNasus\033[1:34m atravessa {ssua} \033[1:31m{esc.lower()}\033[1:34m na cabeça de seu irmão, dando fim a ameaça que \033[1:33mRenekton\033[1:34m representava...\n')
        sleep(3)
        print('Após derrotar seu irmão, \033[1:32mNasus\033[1:34m se reuniu com conselheiros para estabelecer um plano para reerguer Shurima.')
    elif hist[0] == 'N' and forcusu == forcmaq:
        print(f'\033[1:33mRenekton\033[1:34m se enfurece mais, soltando de de seu irmão e o atacando novamente.\n')
        sleep(4)
        forcusu = random.randint(1, 10)
        forcmaq = random.randint(1, 10)
        if forcusu <= forcmaq:
            print(f'\033[1:33mRenekton\033[1:34m acerta \033[1:32mNasus\033[1:34m com {ssuam} \033[1:31m{escmaq.lower()}\033[1:34m na barriga, matando seu irmão.\n')
            sleep(4)
            print('Após matar seu irmão, \033[1:33mRenekton\033[1:34m assume seu império Shurimane, formando um exército imbativel para tomar mais e mais poder!')
            sleep(4)
        elif forcusu > forcmaq:
            print(f'Após ser atacado novamente, \033[1:32mNasus\033[1:34m se defende e em seguida, golpeia seu irmão com {ssuam} \033[1:31m{escmaq.lower()}\033[1:34m, levando \033[1:33mRenekton\033[1:34m a morte\n')
            sleep(4)
            print('Após matar seu irmão, \033[1:32mNasus\033[1:34m reuniu os conselheiros e trabalhou incessantemente para reerguer a nação Shurimane.')
            sleep(4)
print(f'\n\033[1:36m{"FIM":=^60}')

