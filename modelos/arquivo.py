from pathlib import Path
import json
import csv

class FileStorage:    
    def salvar_repos(repos: list[dict], username: str, output: str) -> json:
        pasta_saida = Path(output)
        pasta_saida.mkdir(exist_ok=True, parents=True)
        nome_do_arquivo = f'{pasta_saida}/repos_{username}.json'
        arq_repos = list()

        for repo in repos:
            arq_repos.append(vars(repo))
        with open(nome_do_arquivo, 'w') as repositorios:
            json.dump(arq_repos, repositorios, indent=4)
        print(f'Arquivo de respositórios salvo em: /{pasta_saida}...')

    def salvar_report(report: dict, username: str, output: str) -> csv:
        pasta_saida = Path(output)
        pasta_saida.mkdir(exist_ok=True, parents=True)
        nome_do_arquivo = f'{pasta_saida}/report_{username}.csv'
        
        with open(nome_do_arquivo, 'w', newline='', encoding='utf-8') as relatorio:
            writer = csv.writer(relatorio)
            writer.writerows(report.items())
        print(f'Arquivo de relatórios salvo em: /{pasta_saida}...')
