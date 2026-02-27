class ReportService:
    dados_calculados = dict()

    def relatorio(self, repos: list[dict]) -> dict:
        self.total_repos(repos)
        self.total_estrelas(repos)
        self.top_5_repos_por_estrela(repos)
        self.linguagem(repos)
        return self.dados_calculados
    
    def total_repos(self, repos: list[dict]) -> dict:
        self.dados_calculados.update({f'total_repos': len(repos)})
        print(f'Coletados {len(repos)} repositórios')
        return self.dados_calculados
    
    def total_estrelas(self, repos: list[dict]) -> dict:
        total = int()
        for repo in repos:
            total += repo.stargazers_count
        self.dados_calculados.update({f'total_estrelas': total})
        print(f'Relatório gerado com total de {total} estrelas')
        return self.dados_calculados
    
    def top_5_repos_por_estrela(self, repos: list[dict]) -> dict:
        top_repos = dict()

        for repo in repos:
            top_repos.update({repo.name: repo.stargazers_count})
        ordenado = sorted(top_repos.items(), key=lambda x: x[1], reverse=True)

        for item in ordenado[:5]:
            self.dados_calculados.update({item[0]:item[1]})
        
        return self.dados_calculados
    
    def linguagem(self, repos: list[dict]) -> dict:
        linguagens_total = dict()
        
        for repo in repos:
            if repo.language not in linguagens_total:
                linguagens_total.update({repo.language: 1})
            else:
                linguagens_total[repo.language] += 1
        for item in linguagens_total.items():
            if item[0] == None:
                self.dados_calculados.update({'Desconhecido': item[1]})
            else:
                self.dados_calculados.update({item[0]: item[1]})
        return self.dados_calculados
            
