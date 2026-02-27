import argparse
from modelos.chamada_api import GitHubClient
from modelos.repositorio import Repository
from modelos.relatorio import ReportService
from modelos.arquivo import FileStorage

'''Verifica os argumentos passados via CLI, se não houver o username é inserido via input e o output é setado em ./output/'''
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

repos = GitHubClient().get_repos(username)
# repositorios = Repository.from_api(repos)
relatorio = ReportService().relatorio(repos)
salvar_repositorio = FileStorage.salvar_repos(repos, username, output)
salvar_relatorio = FileStorage.salvar_report(relatorio, username, output)


''' Testar a instância de cada classe''' 
#print(repos)
# print(repositorios)
#print(relatorio)




