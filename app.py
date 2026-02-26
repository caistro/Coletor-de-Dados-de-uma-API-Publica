import argparse
from modelos.chamada_api import GitHubClient
from modelos.repositorio import Repository
from modelos.relatorio import ReportService
from modelos.arquivo import FileStorage

parser = argparse.ArgumentParser(description='Coletor de dados da API do GitHub')
parser.add_argument('--username', type=str, help='Nome do usuário no GitHub')
parser.add_argument('--out', type=str, help='Diretório de salvamento dos arquivos')
args = parser.parse_args()
username = args.username
output = args.out

if username == None:
    username = input(str('Digite o nome do usuário do GitHub: '))

if output == None:
    output = './output/'

chamada = GitHubClient().get_repos(username)
repositorios = Repository.factory(chamada)
# relatorio = ReportService().relatorio(repositorios)
# salvar_repositorio = FileStorage.salvar_repos(repositorios, username, output)
# salvar_relatorio = FileStorage.salvar_report(relatorio, username, output)


''' Testar a instância de cada classe'''
#print(chamada)
#print(repositorios)

#print(relatorio)




