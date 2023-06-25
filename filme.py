class Filme:

    def __init__(self, titulo, anoLancamento, diretor, atores, duracao, genero, valor):
        self.titulo = titulo
        self.anoLancamento = anoLancamento
        self.diretor = diretor
        self.genero = genero
        self.atores = atores
        self.duracao = duracao
        self.valor = valor

    def editaTitulo(self):
        self.titulo = input('Insira o novo título: ').title()
        return self.titulo
        
    def editaAno(self):
        self.anoLancamento = int(input('Insira o novo ano de lançamento: '))
        
    def editaDiretor(self):
        self.diretor = input('Insira o novo diretor: ').title()
        
    def editaDuracao(self):
        while True:
            duracao = int(input('Insira a nova duração (min): '))
            if duracao > 0:
                break
            else:
                print('A duração deve ser maior que 0')
        self.duracao = duracao
        
    def editaValor(self):
        while True:
            valor = float(input('Insira o novo valor: '))
            if valor >= 0:
                break
            else:
                print('O valor deve ser maior que 0')
        self.valor = valor
        
    def editaAtores(self):
        print('ATORES CADASTRADOS:')
        for i in range(len(self.atores)):
            print(f'{i+1} - {self.atores[i]}')
        while True:
            opcao = int(input('O que deseja fazer?\n1 - Adicionar ator\n2 - Remover ator '))
            if opcao == 1 or opcao == 2:
                break
            else:
                print('A opção deve estar na faixa disponível')
        if opcao == 1:
            self.atores.append(input('Digite o nome do ator: ').title())
        else:
            while True:
                ator = int(input('Selecione o ator '))
                if 1 <= ator <= len(self.atores):
                    break
                else:
                    print('Selecione dentro da faixa indicada')
            self.atores.remove(self.atores[ator-1])

    def editaGenero(self):
        generosDisponiveis = ["Romance","Musical", "Documentário", "Ação", "Animação", "Drama", "Terror", "Fantasia", "Comédia"]
        print('GENEROS CADASTRADOS:')
        for i in range(len(self.genero)):
            print(f'{i+1} - {self.genero[i]}')
        while True:
            opcao = int(input('O que deseja fazer?\n1 - Adicionar gênero\n2 - Remover gênero '))
            if opcao == 1 or opcao == 2:
                break
            else:
                print('A opção deve estar na faixa disponível')
        if opcao == 1:
            print('Gêneros disponíveis:')
            for i in range(len(generosDisponiveis)):
                print(f'{i+1} - {generosDisponiveis[i]}')
            while True:   
                gen = int(input('Selecione o gênero a adicionar: '))
                if 1 <= gen <= len(generosDisponiveis) or generosDisponiveis[gen-1] not in self.genero:
                    break
                else:
                    if generosDisponiveis[gen-1] in self.genero:
                        print('Gênero já acionado')
                    else:
                        print('O gênero não está na faixa permitida')
            self.genero.append(generosDisponiveis[gen-1])
        else:
            while True:
                gen = int(input('Selecione o gênero a remover: '))
                if 1 <= gen <= len(self.genero):
                    break
                else:
                    print('O gênero deve estar na faixa permitida')
            self.atores.remove(self.genero[gen-1])
            
    def mostraInfos(self):
        print(f'\n======= INFORMAÇÕES: =======')
        print(f'TÍTULO: {self.titulo}')
        print(f'ANO DE LANÇAMENTO: {self.anoLancamento}')
        print(f'DURAÇÃO: {self.duracao} minutos')
        print(f'GÊNERO(S):', end = ' ')
        for i in range(len(self.genero)):
            print(self.genero[i], end = '')
            if i != len(self.genero) - 1:
                print(', ', end = '')
            else:
                print()
        print(f'ATOR(ES):', end = ' ')
        for i in range(len(self.atores)):
            print(self.atores[i], end = '')
            if i != len(self.atores) - 1:
                print(', ', end = '')
            else:
                print()
        print(f'DIRETOR: {self.diretor}')
        print(f'VALOR: R${self.valor:.2f}')