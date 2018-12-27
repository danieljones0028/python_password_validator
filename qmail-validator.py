#!/home/daniel/anaconda3/bin/python

import re
from datetime import datetime

def logando(mensagem, e, logfile="validator.log"):
    data_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open('validator.log','a') as log:
        texto = "%s \t %s \t %s \n" % (data_atual, mensagem, str(e))
        log.write(texto)

while True:
    try:

        senha = str(input("Senha: "))

        numeros = 2
        caixaalta = 2
        caixabaixa = 2
        simbolos = 2
        tamanho = 10

        if len(senha or ()) < tamanho:
            raise ValueError('Senha tem que ter no mínimo '+str(tamanho)+' caracteres')
        
        if len(re.findall(r"[(+*!@#/)]", senha)) < simbolos:
            raise ValueError('Senha tem que ter no mínimo '+str(simbolos)+' caracteres especiais')

        if len(re.findall(r"[A-Z]", senha)) < caixaalta:
            raise ValueError('Senha tem que ter no mínimo '+str(caixaalta)+' letras maiusculas')

        if len(re.findall(r"[a-z]", senha)) < caixabaixa:
            raise ValueError('Senha tem que ter no mínimo '+str(caixabaixa)+' letras minusculas')

        if len(re.findall(r"[0-9]", senha)) < numeros:
            raise ValueError('Senha tem que ter no mínimo '+str(numeros)+' numeros')

    except ValueError as e:
        logando("Error", e)
    else:
        break

print(senha)