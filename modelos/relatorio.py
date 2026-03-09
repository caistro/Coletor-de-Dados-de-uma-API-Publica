class ReportService:

    def __init__(self):
        self.dados_calculados = dict()
        
    def relatorio(self, repos: list[dict]) -> dict:
        self.total_repos(repos)
        self.total_estrelas(repos)
        self.top_5_repos_por_estrela(repos)
        self.linguagem(repos)
        return self.dados_calculados
    
    def total_repos(self, repos: list[dict]) -> dict:
        self.dados_calculados.update({f'total_repos': len(repos)})
        return self.dados_calculados
    
    def total_estrelas(self, repos: list[dict]) -> dict:
        total = sum(repo.stargazers_count for repo in repos)
        self.dados_calculados.update({f'total_estrelas': total})
        print(f'Relatório gerado com total de {total} estrelas')
        return self.dados_calculados
    
    def top_5_repos_por_estrela(self, repos: list[dict]) -> dict:
        repos_estrela = dict()
        top_repos = dict()

        for repo in repos:
            repos_estrela.update({repo.name:repo.stargazers_count})

        ordenado = sorted(repos_estrela.items(), key=lambda x: x[1], reverse=True)[:5]

        for repo in ordenado:
            top_repos.update({repo[0]:repo[1]})
        
        self.dados_calculados.update({f'top_5_repos_por_estrela': top_repos})
        return self.dados_calculados
                
    def linguagem(self, repos: list[dict]) -> dict:
        linguagens_total = dict()
        
        for repo in repos:
            if repo.language not in linguagens_total:
                linguagens_total.update({repo.language: 1})
            else:
                linguagens_total[repo.language] += 1
        if None in linguagens_total.keys():
            linguagens_total['Desconhecido'] = linguagens_total.pop(None)

        self.dados_calculados.update({f'Linguagens': linguagens_total})
        return self.dados_calculados

        # print(linguagens_total)

        # for item in linguagens_total.items():
        #     if item[0] == None:
        #         self.dados_calculados.update({'Desconhecido': item[1]})
        #     else:
        #         self.dados_calculados.update({item[0]: item[1]})
        # return self.dados_calculados
            
