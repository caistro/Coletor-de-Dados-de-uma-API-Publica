import requests
from modelos.repositorio import Repository

# token = ''
# headers = {
#     'Authorization': '{token}'
# }

class GitHubClient:    
    def get_repos(self, username: str) -> list[dict]:
        url = f'https://api.github.com/users/{username}/repos'
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return [Repository.from_api(repo) for repo in response.json()]

        except requests.exceptions.HTTPError as e:
            status = e.response.status_code
            if status == 403:
                raise ValueError('Limite de requisições atingido ou acesso proibido')
            elif status == 404:
                raise ValueError(f'Usuário {username} não encontrado')
            else:
                raise
        
        except requests.exceptions.Timeout:
            raise TimeoutError('A requisição demorou muito para responder')
        
        except requests.exceptions.RequestException as e:
            raise Exception(f'Erro: {e}')
                    
            
            
