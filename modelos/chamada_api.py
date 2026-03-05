import requests

# token = ''
# headers = {
#     'Authorization': '{token}'
# }

class GitHubClient:  
    base_url = f'https://api.github.com/users/'

    @classmethod
    def get_repos(cls, username: str) -> list[dict]:
        try:
            response = requests.get(f'{cls.base_url}{username}/repos', timeout=10)
            response.raise_for_status()
            # return [Repository.from_api(repo) for repo in response.json()]
            return response.json()

        except requests.exceptions.HTTPError as e:
            status = e.response.status_code
            if status == 404:
                return (f'Usuário {username} não encontrado')
            elif status == 403:
                return ('Limite de requisições atingido ou acesso proibido')
            else:
                return (f'Erro: {e}')
            
        except requests.exceptions.Timeout as e:
            return ('A requisição demorou muito para responder')
        
        except requests.ConnectionError as e:
            return (f'Erro de conexão: {e}') 
            
        except requests.exceptions.RequestException as e:
            return (f'Erro: {e}')
                    
            
            
