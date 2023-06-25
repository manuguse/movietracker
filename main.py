from usuario import Usuario, UsuarioAdm, UsuarioPadrao, UsuarioPVIP
from filme import Filme

### funções gerais ###

def confereOpcao(texto, y, z):
    while True:
        x = int(input(texto))
        if (y <= x <= z):
            break
        else:
            print(f"A opcão deve estar entre {y} e {z} ")
    return x

def desejaVerInfo(filmesProcura, cont):
    opcao = confereOpcao('\nDeseja ver as informações de algum filme?\n1 - sim\n0 - não ', 0, 1)
    if opcao == 1:
        filmeNum = confereOpcao('\nDigite o número do filme: ', 1, cont)
        procuraFilmesPadTitulo(filmesProcura[filmeNum-1].titulo)

def desejaVerInfoDic(filmesProcura, cont):
    opcao = confereOpcao('\nDeseja ver as informações de algum filme?\n1 - sim\n0 - não ', 0, 1)
    if opcao == 1:
        listaFilmes = list(filmesProcura.keys())
        filmeNum = confereOpcao('\nDigite o número do filme: ', 1, cont)
        procuraFilmesPadTitulo(listaFilmes[filmeNum-1])

### pagina inicial ###

def fazLogin():
    flag = False
    user = input('\nNome de usuario ')
    for i in range(len(usuarios)):
        if usuarios[i].nomeUser == user:
            flag = True
            return usuarios[i]
    if flag == False:
        print('\nUsuario nao cadastrado, o que deseja fazer? ')
        return None

def criaConta():
    print('\nCRIANDO CONTA\n')
    nome = input("Insira o nome: ").title()
    nomeUser = input("Insira o nome de usuario: ")
    idade = int(input("Insira a idade: "))
    while True:
        sexo = input("Insira o gênero (F/M): ").upper()
        if sexo == 'F' or sexo == 'M':
            break
        else:
            print('Opção indisponível')
    tipo = confereOpcao(
        f"Insira o tipo de usuario:\n1 - padrão\n2 - adm ", 1, 2)
    if tipo == 2:
        user = UsuarioAdm(nome, nomeUser, idade, sexo, tipo)
    else:
        vip = confereOpcao('Insira o tipo de usuário padrão:\n1 - padrão\n2 - vip ', 1, 2)
        if vip == 1: 
            user = UsuarioPadrao(nome, nomeUser, idade, sexo, tipo)
        else:
            user = UsuarioPVIP(nome, nomeUser, idade, sexo, tipo)
    usuarios.append(user)
    return user

### pagina 2 ###

def pagina2():
    while True:
        if usuarioAtivo.tipo == 2:  # adm
            opcao = confereOpcao(
                (f'\nO que deseja fazer?\n1 - editar filme(s)\n2 - procurar filme(s)\n0 - voltar '), 0, 2)
            if opcao == 0:
                return False
            elif opcao == 1:
                confere = editaFilmes()
                if confere == False:
                    continue
            elif opcao == 2:
                procuraFilmesAdm()
                
        else:  # padrao
            opcao = confereOpcao(
                ('\nO que deseja fazer?\n1 - procurar filme(s)\n2 - adicionar credito\n3 - ver listas\n0 - voltar '), 0, 3)
            if opcao == 0:
                return False
            elif opcao == 1:
                confere = procuraFilmesPad()
                if confere == False:
                    continue
            elif opcao == 2:
                usuarioAtivo.adicionaCredito()
            elif opcao == 3: # ver listas
                while True:
                    opcao2 = confereOpcao('\nO que deseja acessar?\n1 - filmes para assistir\n2 - filmes assistidos\n3 - filmes que está assistindo\n0 - voltar ', 0, 3)
                    if opcao2 == 0:
                        break
                    if opcao2 == 1:
                        confere = usuarioAtivo.mostraFilmesAssistir()
                        if confere == True:
                            desejaVerInfoDic(usuarioAtivo.filmesParaAssistir, len(usuarioAtivo.filmesParaAssistir))
                    elif opcao2 == 2:
                        confere = usuarioAtivo.mostraFilmesAssistidos()
                        if confere == True:
                            desejaVerInfoDic(usuarioAtivo.filmesAssistidos, len(usuarioAtivo.filmesAssistidos))
                    elif opcao2 == 3:
                        confere = usuarioAtivo.mostraFilmesAssistindo()
                        if confere == True:
                            desejaVerInfoDic(usuarioAtivo.assistindoFilme, len(usuarioAtivo.assistindoFilme))
# edita filme

def editaFilmes():
    while True:
        opcao = confereOpcao(
            (f'\nO que deseja fazer?\n1 - editar filmes do catálogo\n2 - adicionar filmes no catálogo\n3 - remover filmes do catálogo\n0 - voltar '), 0, 3)
        if opcao == 0:
            return False
        elif opcao == 1:
            confere = editaFilmesCat()
            if confere == False:
                continue
        elif opcao == 2:
            adicionaFilmes()
        elif opcao == 3:
            confere = removeFilmes()
            if confere == False:
                continue

def removeFilmes():
    flag = False
    filme = (input('\nQual filme deseja remover? ')).title()
    for i in range(len(filmes)):
        if filme == filmes[i].titulo:
            filmes.remove(filmes[i])
            for user in usuarios:
                if user.tipo == 1:
                    if filme in user.filmesParaAssistir:
                        user.filmesParaAssistir.pop(filme)
                    if filme in user.filmesAssistidos:
                        user.filmesAssistidos.pop(filme)
                    if filme in user.assistindoFilme:
                        user.assistindoFilme.pop(filme)
            flag = True
            print('Filme removido com sucesso')
            return True
    if flag == False:
        print('Filme não contido na base de dados')
        return False

def editaFilmesCat():
    flag = False
    filme = input('\nInsira o nome do filme: ').title().strip()
    for i in range(len(filmes)):
        if filme == filmes[i].titulo:
            filme = filmes[i]
            flag =True
    if flag == False: 
        print('Filme não contido na base de dados')
        return False

    while True:
        mudar = confereOpcao(
            (f'Que dado deseja alterar?\n1 - título\n2 - ano de lançamento\n3 - diretor\n4 - genero\n5 - atores\n6 - duração\n7 - valor\n0 - encerrar ediçao '), 0, 7)
        if mudar == 0:
            return False
        else:
            if mudar == 1:
                filme.editaTitulo()  # feito
            elif mudar == 2:
                filme.editaAno()  # feito
            elif mudar == 3:
                filme.editaDiretor()  # feito
            elif mudar == 4:
                filme.editaGenero()  # feito
            elif mudar == 5:
                filme.editaAtores()  # feito
            elif mudar == 6:
                filme.editaDuracao()  # feito
            elif mudar == 7:
                filme.editaValor()  # feito

def adicionaFilmes():
    print('\nADICIONANDO FILME')
    titulo = input('Título: ').title().strip()
    anoLancamento = int(input('Ano de lançamento: '))
    diretor = input('Diretor: ').title()
    while True: # duracao
        duracao = int(input('Duração: '))
        if duracao > 0:
            break
        else:
            print('A duração deve ser maior que 0')
    while True: # valor
        valor = float(input('Valor: '))
        if valor > 0:
            break
        else:
            print('O valor deve ser maior que 0')
    atores = []
    while True: # atores
        ator = input('Ator: ').title()
        atores.append(ator)
        while True:
            opcao = input('Deseja continuar adicionando atores? (S/N) ').upper()
            if opcao == 'N' or opcao == 'S':
                break
        if opcao == 'N':
            break
    generos = []
    numGeneros = 9
    generosDisponiveis = ["Romance","Musical", "Documentário", "Ação", "Animação", "Drama", "Terror", "Fantasia", "Comédia"]
    print('gênero: ')
    for i in range(numGeneros):
        if i == numGeneros-1:
            print(f'{i+1} - {generosDisponiveis[i]}', end=' ')
        else:
            print(f'{i+1} - {generosDisponiveis[i]}')
    while True:
        while True:
            genero = int(input())
            if genero >= numGeneros+1 or genero < 1:
                print('Numero invalido')
                print('Gênero:', end = ' ')
                continue
            elif 1 <= genero <= numGeneros and generosDisponiveis[genero-1] not in generos:
                generos.append(generosDisponiveis[genero-1])
                break
            elif generosDisponiveis[genero-1] in generos:
                print('Gênero já adicionado')
                print('Gênero:', end = ' ')
                
        while True:
            opcao = input('Deseja continuar adicionando gêneros? (S/N) ').upper()
            if opcao == 'N' or opcao == 'S':
                break
        if opcao == 'N':
            break
        else:
            print('Gênero:', end = ' ')

    filme = (Filme(titulo, anoLancamento, diretor, atores, duracao, generos, valor))
    filmes.append(filme)
    print('Filme adicionado com sucesso')
    return False

# procura filme

def procuraFilmesAdm():
    filme = input('\nDigite o título do filme de busca: ').title().strip()
    flag = False
    for i in range(len(filmes)):
        if filme == filmes[i].titulo:
            filme = filmes[i]
            flag = True
            break
    if flag == False: 
        print('Filme não contido na base de dados')
        return False
    filme.mostraInfos()
    return True

def procuraFilmesPad():
    while True:
        opcao = confereOpcao('\nDeseja procurar por que categoria?\n1 - título\n2 - ator\n3 - década\n4 - gênero\n5 - todos os filmes\n0 - voltar ', 0, 5)
        if opcao == 0:
            return True
        if opcao == 1:
            confere = procuraFilmesPadTitulo(input('\nDigite o tĩtulo do filme de busca: ').title().strip())
            if confere == False:
                continue
        elif opcao == 2:
            confere = procuraFilmesPadAtor()
            if confere == False:
                continue
        elif opcao == 3:
            confere = procuraFilmesPadDecada()
            if confere == False:
                continue
        elif opcao == 4:
            confere = procuraFilmesPadGenero()
            if confere == False:
                continue
        elif opcao == 5:
            confere = procuraFilmesPadTodos()
            if confere == False:
                continue
        return False

def procuraFilmesPadTitulo(titulo):
    flag = False
    for movie in filmes:
        if titulo == movie.titulo:
            filme = movie
            flag = True
            break
    if flag == False:
        print('Filme não contido na base de dados')
        return False
    filme.mostraInfos()
    usuarioAtivo.opcoesBuscaMostra(filme, filme.titulo, filme.valor)
    return True

def procuraFilmesPadAtor():
    flag = False
    filmesProcura = []
    ator = input("\nDigite o nome do ator: ").title().strip()
    print(f'\nFILMES COM {ator.upper()}:')
    cont = 0
    for i in range (len(filmes)):
        if ator in filmes[i].atores:
            cont += 1
            print(f'{cont} - {filmes[i].titulo}')
            filmesProcura.append(filmes[i])
            flag = True
    if flag == False:
        print('Nenhum filme encontrado')
        return True
    desejaVerInfo(filmesProcura, cont)
    return True

def procuraFilmesPadDecada():
    filmesProcura = []
    flag = False
    decada = confereOpcao('\nDigite a década: ', 1900, 2020)
    decadaInput = (decada//10)*10
    print(f'\nFILME(S) DA DÉCADA DE {decada}:')
    cont = 0
    for i in range (len(filmes)):
        decadaFilme = (filmes[i].anoLancamento//10)*10
        if decadaInput == decadaFilme:
            cont += 1
            print(f'{cont} - {filmes[i].titulo}')
            filmesProcura.append(filmes[i])
            flag = True
    if flag == False:
        print('Nenhum filme encontrado')
        return False
    desejaVerInfo(filmesProcura, cont)
    return True

def procuraFilmesPadGenero():
    filmesProcura = []
    flag = False
    genero = input('\nDigite o gênero: ').title()
    print(f'\nFILMES DO GÊNERO {genero.upper()}:')
    cont = 0
    for filme in filmes:
        if genero in filme.genero:
            cont += 1
            print(f'{cont} - {filme.titulo}')
            filmesProcura.append(filme)
            flag = True
    if flag == False:
        print('Nenhum filme encontrado')
        return False
    desejaVerInfo(filmesProcura, cont)
    return True

def procuraFilmesPadTodos():
    print('\nTODOS OS FILMES:')
    cont = 0
    for filme in filmes:
        cont += 1
        print(f'{cont} - {filme.titulo}')
    desejaVerInfo(filmes, cont)

### main ###

usuarios = [
    UsuarioAdm('maria', 'mariahh', 18, 'F', 2),
    UsuarioPadrao('joao', 'joaozinho', 23, 'M', 1),
    UsuarioPVIP('emanuelle', 'manug', 19, 'F', 1)
]
filmes = [
    Filme('Clueless', 1995, 'Amy Heckerling', ['Paul Rudd', 'Alicia Silverstone'], 97, ['Comédia'], 20),
    Filme('Orgulho E Preconceito', 2006, 'Joe Wright', ['Keira Knightley', 'Matthew Macfadyen'], 127, ['Romance'], 15),
    Filme('Miss Americana', 2020, 'Lana Wilson', ['Taylor Swift'], 85, ['Documentário', 'Musical'], 17),
    Filme('Forest Gump', 1994, 'Robert Zemeckis', ['Tom Hanks', 'Robin Wright'], 142, ['Comédia', 'Drama'], 15)
]

print("Bem vindo ao movie tracker, o que deseja fazer?")
flag = True
while flag == True:
    while True:
        opcao = confereOpcao(
            "\n1 - fazer login com conta existente\n2 - criar uma nova conta\n0 - encerrar programa ", 0, 2)
        if opcao == 0:
            print("Até a proxima!")
            flag = False
            break
        if opcao == 1:
            user = fazLogin()
            if user != None:
                usuarioAtivo = user
                break
        else:
            user = criaConta()
            usuarioAtivo = user
            break
    if flag == False:
        break

    print(usuarioAtivo.mensagemBoasVindas())

    confere = pagina2()
    if confere == False:
        continue