from usuario import Usuario, UsuarioAdm, UsuarioPadrao, UsuarioPVIP
from filme import Filme
import json

def confereOpcao(texto, y, z):
    while True:
        x = int(input(texto))
        if (y <= x <= z):
            break
        else:
            print(f"a opcão deve estar entre {y} e {z} ")
    return x

### pagina inicial ###

def fazLogin():
    user = input('nome de usuario ')
    if user not in usuarios:
        print('\nusuario nao cadastrado, o que deseja fazer? ')
        return None
    else:
        return usuarios[user]

def criaConta():
    nome = input("insira o nome ").title()
    nomeUser = input("insira o nome de usuario ")
    idade = int(input("insira a idade "))
    while True:
        sexo = input("insira o gênero (F/M) ").upper()
        if sexo == 'F' or sexo == 'M':
            break
        else:
            print('Opção indisponível')
    tipo = confereOpcao(
        f"insira o tipo de usuario:\n1 - padrão\n2 - adm ", 1, 2)
    if tipo == 2:
        user = UsuarioAdm(nome, nomeUser, idade, sexo, tipo)
    else:
        vip = confereOpcao('insira o tipo de usuário padrão:\n1 - padrão\n2 - vip ', 1, 2)
        if vip == 1: 
            user = UsuarioPadrao(nome, nomeUser, idade, sexo, tipo, 200)
        else:
            user = UsuarioPVIP(nome, nomeUser, idade, sexo, tipo, 100)
    usuarios[user.nomeUser] = user
    return user

### pagina 2 ###

def pagina2():
    while True:
        if usuarioAtivo.tipo == 2:  # adm
            opcao = confereOpcao(
                (f'\no que deseja fazer?\n1 - editar filme(s)\n2 - procurar filme(s)\n0 - voltar '), 0, 2)
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
                ('\no que deseja fazer?\n1 - procurar filme(s)\n2 - adicionar credito\n3 - ver listas\n0 - voltar '), 0, 3)
            if opcao == 0:
                return False
            elif opcao == 1:
                confere = procuraFilmesPad()
                if confere == False:
                    continue
            elif opcao == 2:
                usuarioAtivo.adicionaCredito()
            elif opcao == 3:
                usuarioAtivo.verListas()

# edita filme

def editaFilmes():
    while True:
        opcao = confereOpcao(
            (f'\no que deseja fazer?\n1 - editar filmes do catálogo\n2 - adicionar filmes no catálogo\n3 - remover filmes do catálogo\n0 - voltar '), 0, 3)
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
    filme = (input('\nqual filme deseja remover? ')).title()
    for i in range(len(filmes)):
        if filme == filmes[i].titulo:
            filmes.remove(filmes[i])
            return True
    else:
        print('o filme não está contido na base de dados')
        return False

def editaFilmesCat():
    filme = input('\ninsira o nome do filme: ').title()
    for i in range(len(filmes)):
        if filme == filmes[i].titulo:
            filme = filmes[i]
        else: 
            print('o filme não está contido na base de dados')
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
    return True

def adicionaFilmes():
    print('\nADICIONANDO FILME')
    titulo = input('título: ').title()
    anoLancamento = int(input('ano de lançamento: '))
    diretor = input('diretor: ').title()
    while True: # duracao
        duracao = int(input('duração: '))
        if duracao > 0:
            break
        else:
            print('a duração deve ser maior que 0')
    while True: # valor
        valor = float(input('valor: '))
        if valor > 0:
            break
        else:
            print('o valor deve ser maior que 0')
    atores = []
    while True: # atores
        ator = input('ator: ').title()
        atores.append(ator)
        while True:
            opcao = input('deseja continuar adicionando atores? (S/N) ').upper()
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
                print('numero invalido')
                print('gênero:', end = ' ')
                continue
            elif 1 <= genero <= numGeneros and generosDisponiveis[genero-1] not in generos:
                generos.append(generosDisponiveis[genero-1])
                break
            elif generosDisponiveis[genero-1] in generos:
                print('genero já adicionado')
                print('gênero:', end = ' ')
                
        while True:
            opcao = input('deseja continuar adicionando gêneros? (S/N) ').upper()
            if opcao == 'N' or opcao == 'S':
                break
        if opcao == 'N':
            break
        else:
            print('gênero:', end = ' ')

    filme = (Filme(titulo, anoLancamento, diretor, atores, duracao, generos, valor))
    filmes.append(filme)
    print('filme adicionado com sucesso')
    return False

# procura filme

def procuraFilmesAdm():
    filme = input('digite o filme de busca: ').title()
    for i in range(len(filmes)):
        if filme == filmes[i].titulo:
            filme = filmes[i]
            break
        else: 
            print('o filme não está contido na base de dados')
            return False
    filme.mostraInfos()
    return True

def procuraFilmesPad():
    opcao = confereOpcao('\ndeseja procurar por que categoria?\n1 - título\n2 - ator\n3 - década\n4 - gênero\n0 - voltar ', 0, 4)
    if opcao == 1:
        procuraFilmesPadTitulo()

def procuraFilmesPadTitulo():
    statusTrue = '✔'
    statusFalse = '✖'
    filme = input('digite o filme de busca: ').title()
    for i in range(len(filmes)):
        if filme == filmes[i].titulo:
            filme = filmes[i]
            break
        else: 
            print('o filme não está contido na base de dados')
            return False
    filme.mostraInfos()

    if filme in usuarioAtivo.filmesAssistidos:
        assistido = statusTrue
    else:
        assistido = statusFalse

    if filme in usuarioAtivo.filmesParaAssistir:
        lista = statusTrue
        opcoesLista = 'remover filme da lista'
        acaoLista = usuarioAtivo.removeLista
    else:
        lista = statusFalse
        opcoesLista = 'adicionar filme à lista'
        acaoLista = usuarioAtivo.adicionaLista

    if filme in usuarioAtivo.assistindoFilme:
        asistindo = statusTrue
        opcoesFilme = 'terminar filme'
        acaoFilme = usuarioAtivo.terminaFilme
    else:
        asistindo = statusFalse
        opcoesFilme = 'comecar filme'
        acaoFilme = usuarioAtivo.comecaFilme

    print()
    print(f'assistindo: {asistindo}')
    print(f'assistidos: {assistido}')
    print(f'minha lista: {lista}')

    opcao = confereOpcao((f'o que deseja fazer?\n1 - {opcoesFilme}\n2 - {opcoesLista}\n0 - voltar '), 0, 2)
    if opcao == 0:
        return False
    if opcao == 1:
        valor = filme.valor
        acaoFilme(filme, filme.titulo, valor)
    elif opcao == 2:
        acaoLista(filme, filme.titulo)
    return True

### main ###

usuarios = {
    'mariahh': UsuarioAdm('maria', 'mariahh', 18, 'F', 2),
    'joaozinho': UsuarioPadrao('joao', 'joaozinho', 23, 'M', 1, 100),
    'manug': UsuarioPVIP('emanuelle', 'manug', 19, 'F', 1, 200)
}
filmes = (
    Filme('Clueless', 1995, 'Amy Heckerling', ['Paul Rudd', 'Alicia Silverstone'], 97, ['Comédia'], 20),
    Filme('Orgulho e Preconceito', 2006, 'Joe Wright', ['Keira Knightley', 'Matthew Macfadyen'], 127, ['Romance'], 15),
    Filme('Miss Americana', 2020, 'Lana Wilson', ['Taylor Swift'], 85, ['Documentário', 'Musical'], 17),
    Filme('Forest Gump', 1994, 'Robert Zemeckis', ['Tom Hanks', 'Robin Wright'], 142, ['Comédia', 'Drama'], 15)
)

print("MOVIE TRACKER, o que deseja fazer?")
flag = True
while flag == True:
    while True:
        opcao = confereOpcao(
            "\n1 - fazer login com conta existente\n2 - criar uma nova conta\n0 - encerrar programa ", 0, 2)
        if opcao == 0:
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