import requests
from bs4 import BeautifulSoup
from crawlers.extract.extract_data import extrair_processo_grau_1, extrair_processo_grau_2

class Scraper():
    
    def consulta_processo(self, nu_processo, url_grau_1, url_grau_2):
        try:
            lista_processo = {}
            url = url_grau_1
            nu_processo = nu_processo
            numeroDigitoAnoUnificado = nu_processo[:15]
            foroNumeroUnificado = nu_processo[-4:]
            req = requests.get(url,
                                params={
                                        'conversationId': '',
                                        'cbPesquisa': 'NUMPROC',
                                        'numeroDigitoAnoUnificado': numeroDigitoAnoUnificado,
                                        'foroNumeroUnificado': foroNumeroUnificado,
                                        'dadosConsulta.valorConsultaNuUnificado': [nu_processo,'UNIFICADO'],
                                        'dadosConsulta.valorConsulta': '',
                                        'dadosConsulta.tipoNuProcesso': 'UNIFICADO',
                                    },
                                )
            lista_processo['grau_1'] = extrair_processo_grau_1(req)

            url = url_grau_2
            nu_processo = nu_processo
            numeroDigitoAnoUnificado = nu_processo[:15]
            foroNumeroUnificado = nu_processo[-4:]
            req = requests.get(url,
                                params={
                                        'conversationId': '',
                                        'paginaConsulta': '0',
                                        'cbPesquisa': 'NUMPROC',
                                        'numeroDigitoAnoUnificado': numeroDigitoAnoUnificado,
                                        'foroNumeroUnificado': foroNumeroUnificado,
                                        'dePesquisaNuUnificado': [nu_processo,'UNIFICADO'],
                                        'dePesquisa': '',
                                        'tipoNuProcesso': 'UNIFICADO',
                                    },
                                )
            if u'Selecione o processo' in req.text:
                soup = BeautifulSoup(req.text, 'html.parser')
                cod_processo = soup.find('input',{'id': 'processoSelecionado'})
                req = requests.get(url[:-9] + "show.do?processo.codigo=" + cod_processo.get("value"))
                lista_processo['grau_2'] = extrair_processo_grau_2(req)
            return lista_processo
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

