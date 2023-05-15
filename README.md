Busca Processos nos Tribunais de Justiça dos estados do AL e CE
__author__ = "Daniel Baptista"
__contact__ = "danielbpta@gmail.com"
__date__ = "2021/05/12"
__version__ = "1.0"
===============================================================

Este é um projeto para fins de teste.
O desafio é fazer uma API que busque dados de um processo em todos os graus dos Tribunais de Justiça
de Alagoas (TJAL) e do Ceará (TJCE). Geralmente o processo começa no primeiro grau e pode subir para o segundo. 
Você deve buscar o processo em todos os graus e retornar suas informações.
Será necessário desenvolver crawlers para coletar esses dados no tribunal e uma API para fazer input e buscar o resultado depois.

=================================================================================================================================
Guia de instalação:
- Você precisa ter instalado Python 3.x na sua máquina.
- Crie um diretório em um local de sua escolha.
- Faça download do projeto dentro deste diretório.
- Se o projeto estiver compactado, descompacte-o neste diretório.
- Criar um ambiente virtual dentro do diretório:
    - Digite no terminal linux: python -m venv venv
    Obs: Você precisa ter o python-venv instalado ou vai gerar erro.
- Ative o ambiente virtual:
    - Digite no terminal linux: source venv/bin/activate
- Instalar as bibliotecas que estão no requirements.txt
    - Digite no terminal linux: cd consulta_processos para entrar no diretório
    - Digite no terminal linux: pip install -r requirements.txt
- Iniciar o servidor do FastApi:
- Digite o comando no terminal linux: uvicorn main:app --reload (irá iniciar o servidor do FastApi)
- Abra o browser de sua preferência e cole a seguinte url - http://127.0.0.1:8000/docs
- Expandir a aba default e inserir os dados abaixo.

Input:
Dados que devem ser enviados:
Número do processo e sigla do estado referente a consulta.
Para enviar os dados você deve acessar o link http://127.0.0.1:8000/docs
Ex: nu_processo = 0710802-55.2018.8.02.0001
    estado = al
    nu_processo = 0070337-91.2008.8.06.0001
    estado = ce

- Clique em executar, a Api deve retornar o json com as informações do processo.
===============================================================================================
Output:
A Api retornará os dados em formato json.
=========================================================================
- Campos extraídos do site:
* Classe
* Área
* Assunto
* Data distribuição
* Juiz
* Valor da ação
* Partes do Processo
* Lista das Movimentações
=========================================================================