__author__ = 'Daniel Baptista'
__contact__ = 'danielbpta@gmail.com'
__date__ = '2023/05/14'
__version__ = '1.0'
from fastapi import FastAPI
from crawlers.scraper import Scraper

app = FastAPI()

processos = Scraper()

@app.get('/{nu_processo}')
async def consulta_processo(nu_processo): # , estado
    # TODO: Criar um modulo para enviar essa lógica e deixar o código mais limpo
    # estado = estado.upper()
    if len(nu_processo) < 25:
        nu_processo = '{}-{}.{}.{}.{}.{}'.format(nu_processo[:7], nu_processo[7:9], nu_processo[9:13],\
                                                  nu_processo[13:14], nu_processo[14:16], nu_processo[16:20])
    if nu_processo[16:20] == '8.06':
        estado = 'CE'
    if nu_processo[16:20] == '8.02':
        estado = 'AL'

    if estado == 'AL':
        url_grau_1 = 'https://www2.tjal.jus.br/cpopg/search.do?'
        url_grau_2 = 'https://www2.tjal.jus.br/cposg5/search.do'
        return processos.consulta_processo(nu_processo, url_grau_1, url_grau_2)
    if estado == 'CE':
        url_grau_1 = 'https://esaj.tjce.jus.br/cpopg/search.do?'
        url_grau_2 = 'https://esaj.tjce.jus.br/cposg5/search.do'
        return processos.consulta_processo(nu_processo, url_grau_1, url_grau_2)
    