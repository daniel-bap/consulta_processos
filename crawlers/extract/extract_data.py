from bs4 import BeautifulSoup

# TODO: Melhorar alguns tratamentos, como excesso de espaços, criar algumas regex para tratar textos
# melhorar a extração dos dados recursivos. Teste somente os 2 inputs que me enviaram então
# podem ocorrer falhas de parser com outras consultas mas como teste está bom.

def extrair_processo_grau_1(body):
    soup = BeautifulSoup(body.content, 'html.parser')
    if u"O tipo de pesquisa informado é inválido." in soup.text:
        return {'Info': 'O tipo de pesquisa informado é inválido.'}
    if u"Não existem informações disponíveis para os parâmetros informados." in soup.prettify():
        return {'info': 'Não existem informações disponíveis para os parâmetros informados.'}
    else:
        dados_processo = {}
        classe = soup.find('span',{'id':'classeProcesso'})
        dados_processo['classe'] = check_data(classe)
        area = soup.find('div',{'id': 'areaProcesso'})
        dados_processo['area'] = check_data(area)
        assunto = soup.find('span', {'id': 'assuntoProcesso'})
        dados_processo['assunto'] = check_data(assunto)
        dt_distribuicao = soup.find('div', {'id': 'dataHoraDistribuicaoProcesso'})
        dados_processo['dt_distribuicao'] = check_data(dt_distribuicao)
        nm_juiz = soup.find('span', {'id': 'juizProcesso'})
        dados_processo['nm_juiz'] = check_data(nm_juiz)
        vl_acao = soup.find('div', {'id': 'valorAcaoProcesso'})
        dados_processo['vl_acao'] = check_data(vl_acao)
        
        lista_partes_processo = {}
        tp_pt = []
        nm_pt = []
        for item in soup.find_all('table', {'id': 'tablePartesPrincipais'}):
            for tp_participacao in item.find_all('span', {'class':'mensagemExibindo tipoDeParticipacao'}):
                tp_pt.append(check_data(tp_participacao))
            for nm_parte in item.find_all('td', {'class':'nomeParteEAdvogado'}):
                nm_pt.append(check_data(nm_parte))
            for i,j in zip(tp_pt,nm_pt):
                lista_partes_processo[i.replace('\n','').replace('\t','').replace('\xa0','')]\
                      = j.replace('\n','').replace('\t','').replace('\xa0','')
        dados_processo['lista_partes_processo'] = lista_partes_processo

        lista_movimentacoes_processo = {}
        tp_mv = []
        desc_mv = []
        for item in soup.find_all('tr', {'class': 'fundoClaro containerMovimentacao'}):
            for tp_movimentacao in item.find_all('td', {'class':'dataMovimentacao'}):
                tp_mv.append(check_data(tp_movimentacao))
            for desc_movimentacao in item.find_all('td', {'class':'descricaoMovimentacao'}):
                desc_mv.append(check_data(desc_movimentacao))
            for i,j in zip(tp_mv,desc_mv):
                lista_movimentacoes_processo[i.replace('\n','').replace('\t','').replace('\xa0','')]\
                      = j.replace('\n','').replace('\t','').replace('\xa0','')
        dados_processo['lista_movimentacoes_processo'] = lista_movimentacoes_processo
        return dados_processo
    
def extrair_processo_grau_2(body):
    soup = BeautifulSoup(body.content, 'html.parser')
    if u"O tipo de pesquisa informado é inválido." in soup.text:
        return {'Info': 'O tipo de pesquisa informado é inválido.'}
    if u"Não existem informações disponíveis para os parâmetros informados." in soup.prettify():
        return {'info': 'Não existem informações disponíveis para os parâmetros informados.'}
    else:
        dados_processo = {}
        classe = soup.find('div', {'id': 'classeProcesso'})
        dados_processo['classe'] = check_data(classe) 
        area = soup.find('div',{'id': 'areaProcesso'})
        dados_processo['area'] = check_data(area)
        assunto = soup.find('div', {'id': 'assuntoProcesso'})
        dados_processo['assunto'] = check_data(assunto)
        dt_distribuicao = soup.find('div', {'id': 'dataHoraDistribuicaoProcesso'})
        dados_processo['dt_distribuicao'] = check_data(dt_distribuicao)
        nm_juiz = soup.find('span', {'id': 'juizProcesso'})
        dados_processo['nm_juiz'] = check_data(nm_juiz)
        vl_acao = soup.find('div', {'id': 'valorAcaoProcesso'})
        dados_processo['vl_acao'] = check_data(vl_acao)
        
        lista_partes_processo = {}
        tp_pt = []
        nm_pt = []
        for item in soup.find_all('table', {'id': 'tablePartesPrincipais'}):
            for tp_participacao in item.find_all('span', {'class':'mensagemExibindo tipoDeParticipacao'}):
                tp_pt.append(check_data(tp_participacao))
            for nm_parte in item.find_all('td', {'class':'nomeParteEAdvogado'}):
                nm_pt.append(check_data(nm_parte))
            for i,j in zip(tp_pt,nm_pt):
                lista_partes_processo[i.replace('\n','').replace('\t','').replace('\xa0','')]\
                      = j.replace('\n','').replace('\t','').replace('\xa0','')
        dados_processo['lista_partes_processo'] = lista_partes_processo

        lista_movimentacoes_processo = {}
        tp_mv = []
        desc_mv = []
        for item in soup.find_all('tr', {'class': 'fundoClaro movimentacaoProcesso'}):
            for tp_movimentacao in item.find_all('td', {'class':'dataMovimentacaoProcesso'}):
                tp_mv.append(check_data(tp_movimentacao))
            for desc_movimentacao in item.find_all('td', {'class':'descricaoMovimentacaoProcesso'}):
                desc_mv.append(check_data(desc_movimentacao))
            for i,j in zip(tp_mv,desc_mv):
                lista_movimentacoes_processo[i.replace('\n','').replace('\t','').replace('\xa0','')]\
                      = j.replace('\n','').replace('\t','').replace('\xa0','')
        dados_processo['lista_movimentacoes_processo'] = lista_movimentacoes_processo
        return dados_processo

# Método evita erro de Nonetype se o find_all não encontrar a tag relaconada,
# também tiro excesso de espaços em branco do texto.
def check_data(data: BeautifulSoup):
    if data:
        return data.get_text().strip()
