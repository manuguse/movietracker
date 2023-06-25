from filme import Filme
class Usuario:

    def __init__(self, nome, nomeUser, idade, sexo, tipo):
        self.nome = nome
        self.nomeUser = nomeUser
        self.idade = idade
        self.sexo = sexo
        self.tipo = tipo

    def mensagemBoasVindas(self):
        if self.sexo == 'F':
            mensagem = (f'\nBem vinda, {(self.nome).title()}!')
        else:
            mensagem = (f'\nBem vindo, {(self.nome).title()}!')
        return mensagem


class UsuarioAdm(Usuario):

    def __init__(self, nome, nomeUser, idade, sexo, tipo):
        super().__init__(nome, nomeUser, idade, sexo, tipo) 


class UsuarioPadrao(Usuario):
    def __init__(self, nome, nomeUser, idade, sexo, tipo, filmesAssistidos = {}, filmesParaAssistir = {}, assistindoFilme = {}):
        super().__init__(nome, nomeUser, idade, sexo, tipo)
        self.credito = 30
        self.filmesParaAssistir = filmesParaAssistir
        self.filmesAssistidos = filmesAssistidos
        self.assistindoFilme = assistindoFilme

    def adicionaCredito(self):
        print(f'\nCrédito atual: R${self.credito:.2f}')
        while True:
            valor = float(input('Quanto deseja inserir? '))
            if valor >= 0:
                break
            else:
                print('O valor deve ser positivo')
        self.credito += valor
        print(f'Crédito total: R${self.credito:.2f}')

    def removeLista(self, filme, titulo):
        self.filmesParaAssistir.pop(titulo)
        print('Filme removido da lista com sucesso')

    def adicionaLista(self, filme, titulo):
        limiteLista = 20
        if len(self.filmesParaAssistir)+1 <= limiteLista: 
            self.filmesParaAssistir[titulo] = filme
            print('\nFilme adicionado à lista com sucesso')
            print(f'Capacidade da lista: {len(self.filmesParaAssistir)}/{limiteLista}')
        else:
            print('A lista está em seu limite, esvazie para adicionar')
    
    def terminaFilme(self, filme, titulo, valor):
        self.filmesAssistidos[titulo] = filme
        self.assistindoFilme.pop(titulo)
        self.credito += valor*0.25
        print(f'Filme terminado, crédito total: R${self.credito:.2f}')
    
    def comecaFilme(self, filme, titulo, valor):
        limiteFilme = 5
        if self.credito - valor > 0:
            if len(self.assistindoFilme) > limiteFilme:
                print(f'Você já chegou no limite de filmes assistidos de uma vez')
            else:
                self.credito -= valor
                self.assistindoFilme[titulo] = filme
                print(f'Tenha um bom filme!\ncrédito total: R${self.credito:.2f}')
        else:
            print(f'Saldo insuficiente, crédito total: R${self.credito:.2f}')
            opcao = int(input('Deseja adicionar crédito?\n1 - sim\n2 - não '))
            while opcao != 1 and opcao != 2:
                opcao = int(input('Opção inválida, digite novamente'))
            if opcao == 1:
                self.adicionaCredito()
                opcao = int(input('Deseja começar o filme?\n1 - sim\n2 - não '))
                while opcao != 1 and opcao != 2:
                    opcao = int(input('Opção inválida, digite novamente'))
                if opcao == 1:
                    self.comecaFilme(filme, titulo, valor)

    def mostraFilmesAssistir(self):
        print('\nFilmes para assistir:')
        if len(self.filmesParaAssistir) == 0:    
            print('Lista vazia')
            return False
        else:
            cont = 1
            for i in self.filmesParaAssistir:
                print(f'{cont} - {i}')
                cont += 1
            return True
    
    def mostraFilmesAssistidos(self):
        print('\nFilmes assistidos:')
        if len(self.filmesAssistidos) == 0:
            print('Lista vazia')
            return False
        else:
            cont = 1
            for i in self.filmesAssistidos:
                print(f'{cont} - {i}')
                cont += 1
            return True
            
    def mostraFilmesAssistindo(self):
        print('\nFilmes que está assistindo:')
        if len(self.assistindoFilme) == 0:
            print('Lista vazia')
            return False
        else:
            cont = 1
            for i in self.assistindoFilme:
                print(f"{cont} - {i}")
                cont += 1
            return True

    def opcoesBuscaMostra(self, filme, titulo, valor): 
        statusTrue = '✔'
        statusFalse = '✖'
        if titulo in self.filmesAssistidos:
            assistido = statusTrue
        else:
            assistido = statusFalse

        if titulo in self.filmesParaAssistir:
            lista = statusTrue
            opcoesLista = 'remover filme da lista'
            acaoLista = self.removeLista
        else:
            lista = statusFalse
            opcoesLista = 'adicionar filme à lista'
            acaoLista = self.adicionaLista

        if titulo in self.assistindoFilme:
            asistindo = statusTrue
            opcoesFilme = 'terminar filme'
            acaoFilme = self.terminaFilme
        else:
            asistindo = statusFalse
            opcoesFilme = 'comecar filme'
            acaoFilme = self.comecaFilme

        print()
        print(f'assistindo: {asistindo}')
        print(f'assistidos: {assistido}')
        print(f'minha lista: {lista}')

        while True:
            opcao = int(input(f'\nO que deseja fazer?\n1 - {opcoesFilme}\n2 - {opcoesLista}\n0 - voltar '))
            if 0 <= opcao <= 2:
                break
            else:
                print('Opção inválida')
        if opcao == 0:
            return False
        if opcao == 1:
            acaoFilme(filme, titulo, valor)
        elif opcao == 2:
            acaoLista(filme, titulo)

class UsuarioPVIP(UsuarioPadrao):
    def __init__(self, nome, nomeUser, idade, sexo, tipo):
        super().__init__(nome, nomeUser, idade, sexo, tipo, filmesAssistidos = {}, filmesParaAssistir = {}, assistindoFilme = {})
        self.credito = 50

    def adicionaLista(self, filme, titulo):
        self.filmesParaAssistir[titulo] = filme
        print('\nFilme adicionado à lista com sucesso')
    
    def comecaFilme(self, filme, titulo, valor):
        if self.credito - valor > 0:
            self.credito -= valor
            self.assistindoFilme[titulo] = filme
            print(f'Tenha um bom filme!\ncrédito total: R${self.credito:.2f}')

        else:
            print(f'Saldo insuficiente, crédito total: R${self.credito:.2f}')
            
    def terminaFilme(self, filme, titulo, valor):
        self.filmesAssistidos[titulo] = filme
        self.assistindoFilme.pop(titulo)
        self.credito += valor*0.50
        print(f'Filme terminado, crédito total: R${self.credito:.2f}')