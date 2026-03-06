import argparse

class ArgumentosCLI:
    '''Verifica os argumentos passados via CLI, se não houver o username é inserido via input e o output é setado em ./output/'''

    def __init__(self):
        self.parametros_cli = argparse.ArgumentParser(description='Coletor de dados da API do GitHub')
        self.parametros_cli.add_argument('--username', type=str, help='Nome do usuário no GitHub')
        self.parametros_cli.add_argument('--out', type=str, help='Diretório de salvamento dos arquivos')
        self.args = self.parametros_cli.parse_args()
        self.username = self._get_username()
        self.output = self._get_output()

    
    def _get_username(self):
        user = self.args.username
        if user == None:
            user = input(str('Digite o nome do usuário do GitHub: '))
        return user
    
    def _get_output(self):
        if self.args.out == None:
            return './output/' 
        return self.args.out 
    



