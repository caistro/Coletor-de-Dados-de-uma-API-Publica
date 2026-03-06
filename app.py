import argparse
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
    chamada = GitHubClient.get_repos(param.username)
    iter(chamada)
except Exception as e:
    exit()


repositorios = [Repository.from_api(repo) for repo in chamada]
relatorio = ReportService().relatorio(repositorios)
salvar_repositorio = FileStorage.salvar_repos(repositorios, param.username, param.output)
salvar_relatorio = FileStorage.salvar_report(relatorio, param.username, param.output)


''' Testar a instância de cada classe'''
# print(chamada) 
# print(repositorios)
# print(relatorio)





