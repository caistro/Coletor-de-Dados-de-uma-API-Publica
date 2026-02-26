class Repository:

    def __init__(self, name, full_name, html_url, language, stargazers_count, forks_count, updated_at):
        self.name = name
        self.full_name = full_name
        self.html_url = html_url
        self.language = language
        self.stargazers_count = stargazers_count
        self.forks_count = forks_count
        self.updated_at = updated_at


    @classmethod
    def factory(cls, response: dict):
        for i in response:
            name = i['name']
            print(name)

        return cls(
            name = response[1].get('name'),
            full_name = response[1].get('full_name'),
            html_url = response[1].get('html_url'),
            language = response[1].get('language'),
            stargazers_count = response[1].get('stargazers_count'),
            forks_count = response[1].get('forks_count'),
            updated_at = response[1].get('updated_at')
        )
    
    def from_api():
        pass
    

