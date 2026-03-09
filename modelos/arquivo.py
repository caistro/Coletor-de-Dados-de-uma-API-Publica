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

        def flatten_dict(dicionario, parent_key='', sep='/'):
            """
            Transforma um dicionário aninhado em um dicionário de nível único,
            concatenando as chaves com o separador definido.
            """
            items = []
            for k, v in dicionario.items():
                new_key = f"{parent_key}{sep}{k}" if parent_key else k
                if isinstance(v, dict):
                    items.extend(flatten_dict(v, new_key, sep=sep).items())
                else:
                    items.append((new_key, v))
            return dict(items)
        data = flatten_dict(report)
                    
        with open(nome_do_arquivo, 'w', newline='', encoding='utf-8') as relatorio:
            writer = csv.DictWriter(relatorio, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)
        print(f'Arquivo de relatórios salvo em: /{pasta_saida}...')



