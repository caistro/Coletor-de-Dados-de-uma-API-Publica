import requests

class GitHubClient:    
    def get_repos(self, username: str) -> list[dict]:
        url = f'https://api.github.com/users/{username}/repos'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return print('Usuário não encontrado')
        else:
            return print(f'O erro foi: {response.status_code: {response}}')

