import requests

token = ''
headers = {
    'Authorization': '{token}'
}

class GitHubClient:
    base_url = f'https://api.github.com/users/'

    @classmethod
    def get_repos(cls, username: str) -> list[dict]:
        try:
            response = requests.get(f'{cls.base_url}{username}/repos', timeout=10)
            response.raise_for_status()
            print(f'Status da requisição: {response.status_code}')
            print(f'Respositórios coletados: {len(response.json())}')
            if len(response.json()) == 0:
                return exit()
            return response.json()

        except requests.exceptions.HTTPError as e:
            status = e.response.status_code
            if status == 404:
                return print(f'Usuário "{username}" não encontrado')
            elif status == 403:
                return print('Limite de requisições atingido ou acesso proibido')
            elif status == 401:
                return print('Acesso não autorizado')
            else:
                return print(f'Erro: {e}')
            
        except requests.exceptions.Timeout as e:
            return print('A requisição demorou muito para responder')
        
        except requests.ConnectionError as e:
            return print(f'Erro de conexão: {e}') 
            
        except requests.exceptions.RequestException as e:
            return print(f'Erro: {e}')
        
        except Exception as e:
            return print(f'Erro: {e}')
                    
            
            
