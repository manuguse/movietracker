class Usuario:

    def __init__(self, nome, nomeUser, idade, sexo, tipo):
        self.nome = nome
        self.nomeUser = nomeUser
        self.idade = idade
        self.sexo = sexo
        self.tipo = tipo

    def mensagemBoasVindas(self):
        if self.sexo == 'F':
            mensagem = (f'\nBem vinda, {(self.nome).title()}')
        else:
            mensagem = (f'\nBem vindo, {(self.nome).title()}')
        return mensagem


class UsuarioAdm(Usuario):

    def __init__(self, nome, nomeUser, idade, sexo, tipo):
        super().__init__(nome, nomeUser, idade, sexo, tipo) 


class UsuarioPadrao(Usuario):
    def __init__(self, nome, nomeUser, idade, sexo, tipo, creditoInicial):
        super().__init__(nome, nomeUser, idade, sexo, tipo)
        self.credito = creditoInicial
        self.filmesParaAssistir = {}
        self.filmesAssistidos = {}
        self.assistindoFilme = {}

    def adicionaCredito(self):
        valor = int(input('Quanto deseja inserir? '))
        self.credito += valor
        print(f'Crédito total: {self.credito}')


    def removeLista(self, filme, titulo):
        self.filmesParaAssistir.pop[titulo]
        print('filme removido da lista')

    def adicionaLista(self, filme, titulo):
        limiteLista = 20
        if len(self.filmesParaAssistir)+1 <= limiteLista: 
            self.filmesParaAssistir[titulo] = filme
            print('filme adicionado à lista')
            print(f'capacidade da lista: {len(self.filmesParaAssistir)}/{limiteLista}')
        else:
            print('a lista está em seu limite, esvazie para adicionar')
    
    def terminaFilme(self, filme, titulo, valor):
        self.filmesAssistidos[titulo] = filme
        self.assistindoFilme.pop(titulo)
        self.credito += valor/2
        print(f'filme terminado, crédito total: {self.credito:.2f}')
    
    def comecaFilme(self, filme, titulo, valor):
        limiteFilme = 5
        if self.credito - valor > 0:
            if len(self.assistindoFilme) > limiteFilme:
                print(f'você já chegou no limite de filmes assistidos de uma vez')
            else:
                self.credito -= valor
                self.assistindoFilme[titulo] = filme
                print(f'tenha um bom filme!\ncrédito total: {self.credito:.2f}')
        else:
            print(f'saldo insuficiente, crédito total: {self.credito:.2f}')


class UsuarioPVIP(UsuarioPadrao):
    def __init__(self, nome, nomeUser, idade, sexo, tipo, filmesParaAssistir, assistindoFilme, filmesAssistidos, creditoInicial):
        super().__init__(nome, nomeUser, idade, sexo, tipo, creditoInicial)
        self.credito = creditoInicial
        self.filmesParaAssistir = filmesParaAssistir
        self.assistindoFilme = assistindoFilme
        self.filmesAssistidos = filmesAssistidos

    def adicionaLista(self, filme, titulo):
        self.filmesAssistidos[titulo] = filme
        print('filme adicionado à lista')
    
    def comecaFilme(self, filme, titulo, valor):
        if self.credito - valor > 0:
            self.credito -= valor
            self.assistindoFilme[titulo] = filme
            print(f'tenha um bom filme!\ncrédito total: {self.credito:.2f}')
        else:
            print(f'saldo insuficiente, crédito total: {self.credito:.2f}')
