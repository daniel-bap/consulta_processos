import unittest
from bs4 import BeautifulSoup


class TesteParser(unittest.TestCase):
    # Teste parser da primeira parte do html do processo (1º grau TJCE)
	def test_parser_tjce(self):
		with open('tjce.html', 'r') as f:
			soup = BeautifulSoup(f, 'html.parser')
			
		classe = soup.find('span',{'id':'classeProcesso'})
		self.assertEqual(classe.get_text(), 'Ação Penal - Procedimento Ordinário')
		area = soup.find('div',{'id': 'areaProcesso'})
		self.assertEqual(area.get_text().strip(), 'Criminal')
		assunto = soup.find('span', {'id': 'assuntoProcesso'})
		self.assertEqual(assunto.get_text().strip(), 'Crimes de Trânsito')
		dt_distribuicao = soup.find('div', {'id': 'dataHoraDistribuicaoProcesso'})
		self.assertEqual(dt_distribuicao.get_text().strip(), '02/05/2018 às 09:13 - Sorteio')
		nm_juiz = soup.find('span', {'id': 'juizProcesso'})
		if nm_juiz:
			self.assertEqual(nm_juiz.get_text().strip(), 'José Cícero Alves da Silva')
		vl_acao = soup.find('div', {'id': 'valorAcaoProcesso'})
		if vl_acao:
			self.assertEqual(vl_acao.get_text().strip(), 'R$         281.178,42')

	# Teste parser da primeira parte do html do processo (1º grau TJAL)
	def test_parser_tjal(self):
		with open('tjal.html', 'r') as f:
			soup = BeautifulSoup(f, 'html.parser')
			
		classe = soup.find('span',{'id':'classeProcesso'})
		self.assertEqual(classe.get_text(), 'Procedimento Comum Cível')
		area = soup.find('div',{'id': 'areaProcesso'})
		self.assertEqual(area.get_text().strip(), 'Cível')
		assunto = soup.find('span', {'id': 'assuntoProcesso'})
		self.assertEqual(assunto.get_text().strip(), 'Dano Material')
		dt_distribuicao = soup.find('div', {'id': 'dataHoraDistribuicaoProcesso'})
		self.assertEqual(dt_distribuicao.get_text().strip(), '02/05/2018 às 19:01 - Sorteio')
		nm_juiz = soup.find('span', {'id': 'juizProcesso'})
		if nm_juiz:
			self.assertEqual(nm_juiz.get_text().strip(), 'José Cícero Alves da Silva')
		vl_acao = soup.find('div', {'id': 'valorAcaoProcesso'})
		if vl_acao:
			self.assertEqual(vl_acao.get_text().strip().replace(' ',''), 'R$281.178,42')
			
	def test_upper(self):
		self.assertEqual('al'.upper(), 'AL')

	# Trata o numero do processo se o usuário inserir somente os números.
	def test_input(self):
		nu_processo = '07108025520188020001'
		if len(nu_processo) < 25:
			nu_processo = '{}-{}.{}.{}.{}.{}'.format(nu_processo[:7], nu_processo[7:9],\
					     nu_processo[9:13], nu_processo[13:14], nu_processo[14:16], nu_processo[16:20])
		#print(nu_processo)
		self.assertEqual(nu_processo, '0710802-55.2018.8.02.0001')

	"""
		Eu criei este bloco de código sob a hipótese de que uma parte do número do processo
		corresponde ao estado do AL ou do CE então fiz esta verificação para adicionar o estado 
		automaticamente na busca do processo. Se estiver errado então deve-se retornar para a 
		inserção do estado do TJ na consulta.
	"""
	def test_estado_tj(self):
		nu_processo = '0710802-55.2018.8.02.0001'
		if nu_processo[16:20] == '8.06':
			estado = 'CE'
			self.assertEqual(estado, 'CE')
		if nu_processo[16:20] == '8.02':
			estado = 'AL'
			self.assertEqual(estado, 'AL')


if __name__ == '__main__':
	unittest.main()