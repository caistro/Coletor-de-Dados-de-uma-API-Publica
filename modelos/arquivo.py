from pathlib import Path
import json
import csv

class FileStorage:
    '''Output está setado direto para impedir que o usuário salve os arquivos em uma pasta inexistente. 
    Não conseguir tentar a persistencia de criação da pasta'''
    
    def salvar_repos(repos: dict, username: str, output: str) -> json:
        pasta_saida = Path(output)
        pasta_saida.mkdir(exist_ok=True, parents=True)
        nome_do_arquivo = f'{pasta_saida}/repos_{username}.json'
        with open(nome_do_arquivo, 'w') as repositorios:
            json.dump(repos, repositorios, indent=4)
        print(f'Arquivo de respositórios salvos em: /{pasta_saida}...')
    
    def salvar_report(report: dict, username: str, output: str) -> json:
        pasta_saida = Path(output)
        pasta_saida.mkdir(exist_ok=True, parents=True)
        nome_do_arquivo = f'{pasta_saida}/report_{username}.json'
        with open(nome_do_arquivo, 'w') as relatorio:
            json.dump(report, relatorio, indent=4)
        print(f'Arquivo de relatório salvos em: /{pasta_saida}...')

    
    '''Ao tentar implantar o relatorio com CSV ele sai quebrado. Creio que devido a forma como está o aninhamento do dicionário'''
    # def salvar_csv(report: dict, username: str, output: str) -> csv:
        #     pasta_saida = Path(output)
        #     pasta_saida.mkdir(exist_ok=True, parents=True)
        #     nome_do_arquivo = f'{pasta_saida}/report_{username}.csv'

        #     chave_principal = list()
        #     chave_aninhada = list()

        #     for i in report:
        #         chave_principal.append(i)
        #         if type(report.get(i,{})) == dict:    
        #             chave_aninhada += report.get(i,{}).keys()
        #     print(chave_principal)
        #     print(chave_aninhada)

        #     with open(nome_do_arquivo, 'w', newline='', encoding='utf-8') as relatorio:
        #         writer = csv.DictWriter(relatorio, fieldnames=cabecalho)
        #         writer.writeheader()
        #         writer.writerows(report.values())


                