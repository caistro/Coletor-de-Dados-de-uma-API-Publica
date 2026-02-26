class ReportService:
    dados_calculados = dict()

    def relatorio(self, repos: dict) -> dict:
        self.total_repos(repos)
        self.total_estrelas(repos)
        self.top_5_repos_por_estrela(repos)
        self.linguagem(repos)
        return self.dados_calculados
    
    def total_repos(self, repos: dict) -> dict:
        self.dados_calculados.update({f'total_repos': len(repos)})
        print(f'Coletados {len(repos)} repositórios')
        return self.dados_calculados
    
    def total_estrelas(self, repos: dict) -> dict:
        total = int()
        for i in repos:
            total += repos[i]['stargazers_count']
        self.dados_calculados.update({f'total_estrelas': total})
        print(f'Relatório gerado com total de {total} estrelas')
        return self.dados_calculados
    
    def top_5_repos_por_estrela(self, repos: dict) -> dict:
        top_estrelas = list()
        top_repos = dict()  
        
        # lista em ordem decrecente os repos por estrela
        for item in repos:
            top_estrelas.append(repos[item]['stargazers_count'])
            top_estrelas.sort(reverse=True)          

        # atribui o nome do repo como chave do dicionario, mantendo a ordem decrecente
        for item in repos:
            top_repos.update({repos[item]['name']: top_estrelas[item]})
            if len(top_repos) == 5:
                break

        self.dados_calculados.update({f'top_5_repos_por_estrela': top_repos})
        return self.dados_calculados
    
    def linguagem(self, repos: dict) -> dict:
        linguagens = list()
        linguagens_total = dict()
        
        #filtra as linguagens utilizadas
        for item in repos:
            #print(repos[item]['language'])
            linguagens.append(repos[item]['language'])
            
        #conta as linguagens utilizadas mantendo o nome da linguagem como chave
        for item in linguagens:
            linguagens_total.update({item: linguagens.count(item)})
        
        self.dados_calculados.update({f'linguagem': linguagens_total})
        return self.dados_calculados

