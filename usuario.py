class Usuario:

    def __init__(self, nome, nomeUser, idade, sexo, tipo):
        creditoInicial = 100
        self.nome = nome
        self.nomeUser = nomeUser
        self.idade = idade
        self.sexo = sexo
        self.tipo = tipo
        self.filmesParaAssistir = []
        self.filmesAssistidos = []
        self.credito = creditoInicial

    def mensagemBoasVindas(self):
        if self.sexo == 'F':
            mensagem = (f'\nbem vinda, {self.nome}')
        else:
            mensagem = (f'\nbem vindo, {self.nome}')
        return mensagem
    
    def adicionaCredito(self):
        valor = int(input('quanto deseja inserir? '))
        self.credito += valor

    def removeCredito(self, valor):
        self.credito -= valor

class UsuarioAdm(Usuario):

    def __init__(self, nome, nomeUser, idade, sexo, tipo):
        super().__init__(nome, nomeUser, idade, sexo, tipo) 
        
class UsuarioPadrao(Usuario):
    def __init__(self, nome, nomeUser, idade, sexo, tipo):
        super().__init__(nome, nomeUser, idade, sexo, tipo)