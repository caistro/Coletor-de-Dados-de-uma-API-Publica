from modelos.args_cli import ArgumentosCLI
from modelos.chamada_api import GitHubClient
from modelos.repositorio import Repository
from modelos.relatorio import ReportService
from modelos.arquivo import FileStorage

'''
Usernames de teste
Torvalds: padrão
ç: Não existe
kakaka: Não tem repositorios 
'''
param = ArgumentosCLI()

try:
    repos_api = GitHubClient.get_repos(param.username)
    iter(repos_api)
except Exception as e:
    exit()

repos_filtrados = [Repository.from_api(repo) for repo in repos_api]
relatorio = ReportService().relatorio(repos_filtrados)
salvar_repositorio = FileStorage.salvar_repos(repos_filtrados, param.username, param.output)
salvar_relatorio = FileStorage.salvar_report(relatorio, param.username, param.output)


''' Testar a instância de cada classe'''
# print(chamada) 
# print(repositorios)
# print(relatorio)





