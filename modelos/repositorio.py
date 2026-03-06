class Repository:

    def __init__(self, name, full_name, html_url, language, stargazers_count, forks_count, updated_at):
        self.name = name
        self.full_name = full_name
        self.html_url = html_url
        self.language = language
        self.stargazers_count = stargazers_count
        self.forks_count = forks_count
        self.updated_at = updated_at
    
    def __str__(self):
        return (
            f'name: {self.name}\n'
            f'full_name: {self.full_name}\n'
            f'html_url: {self.html_url}\n'
            f'language: {self.language}\n'
            f'stargazers_count: {self.stargazers_count}\n'
            f'forks_count: {self.forks_count}\n'
            f'updated_at: {self.updated_at}')
    
    def __repr__(self):
        return f'Repositorio: {self.name}'

    @classmethod
    def from_api(cls, repo: dict):
        return cls(
            name = repo.get('name'),
            full_name = repo.get('full_name'),
            html_url = repo.get('html_url'),
            language = repo.get('language'),
            stargazers_count = repo.get('stargazers_count'),
            forks_count = repo.get('forks_count'),
            updated_at = repo.get('updated_at')
        )
    


