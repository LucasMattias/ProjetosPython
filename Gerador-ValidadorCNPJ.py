import re
from random import randint

def cnpjParaInt(num):
    num = re.sub(r'[^0-9]', '', num)
    numInt = num[0:12]
    return numInt


def validPriNum(c):
    cnpjValida = cnpjParaInt(c)
    acumulanum = 0
    cont = 5
    for i in cnpjValida:
        numTemporario = int(i) * cont
        acumulanum += numTemporario
        cont -= 1
        if cont < 2:
            cont = 9
    primDigito = 11 - (acumulanum % 11)
    if primDigito > 9:
        primDigito = 0
    cnpjProv = cnpjValida + str(primDigito)
    return cnpjProv


def validSegNum(n):
    cnpjProgresso = validPriNum(n)
    acumulanum = 0
    cont = 6
    for n in cnpjProgresso:
        somaNum = int(n) * cont
        acumulanum += somaNum
        cont -= 1
        if cont < 2:
            cont = 9
    segDigito = 11 - (acumulanum % 11)
    if segDigito > 9 :
        segDigito = 0
    cnpjFinal = cnpjProgresso + str(segDigito)
    return cnpjFinal


def validaCnpj(valida):
    cnpjOriginal = re.sub(r'[^0-9]','', valida)
    cnpjValidador = validSegNum(valida)
    if cnpjValidador == cnpjOriginal:
        return 'Esse CNPJ é valido'
    else:
        return 'Infelizmente esse CNPJ não é valido'


def geraCnpj():
    cnpj = ''
    for i in range(0,8):
        cnpj += str(randint(0, 9))
        if i == 1 or i == 4:
            cnpj += '.'
    cnpj += '/0001'
    cnpjGera = validSegNum(cnpj)
    cnpjGeraFinal = ''
    for n , v in enumerate(cnpjGera):
        cnpjGeraFinal += v
        if n == 1 or n == 4:
            cnpjGeraFinal += '.'
        if n == 7:
            cnpjGeraFinal += '/'
        if n == 11:
            cnpjGeraFinal += '-'
    return cnpjGeraFinal


print(validaCnpj('11.177.739/0001-90'))

print(geraCnpj())