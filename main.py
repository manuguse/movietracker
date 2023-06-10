from usuario import Usuario, UsuarioAdm, UsuarioPadrao
from filme import Filme


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
        user == UsuarioPadrao(nome, nomeUser, idade, sexo, tipo)
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
                ('\no que deseja fazer?\n1 - procurar filme(s)\n2 - adicionar credito\n0 - voltar '), 0, 2)
            if opcao == 0:
                paginaInicial()
            elif opcao == 1:
                procuraFilmesPad()
            elif opcao == 2:
                usuarioAtivo.adicionaCredito()

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
    filme = int(input('\nqual filme deseja remover? '))
    if filmes in filmes:
        filmes.pop(filme)
        return True
    else:
        print('o filme não está contido na base de dados')
        return False


def editaFilmesCat():
    filme = input('\ninsira o nome do filme: ').title()
    if filme in filmes:
        print(filme)
        while True:
            mudar = confereOpcao(
                (f'Que dado deseja alterar?\n1 - título\n2 - ano de lançamento\n3 - diretor\n4 - genero\n5 - atores\n6 - duração\n7 - valor\n0 - encerrar ediçao '), 0, 7)
            if mudar == 0:
                return False
            else:
                if mudar == 1:
                    filmes[filme].editaTitulo()  # feito
                    tituloo = filmes[filme].titulo
                    filmes[tituloo] = filmes[filme]
                    filmes.pop(filme)
                    filme = tituloo
                elif mudar == 2:
                    filmes[filme].editaAno()  # feito
                elif mudar == 3:
                    filmes[filme].editaDiretor()  # feito
                elif mudar == 4:
                    filmes[filme].editaGenero()  # feito
                elif mudar == 5:
                    filmes[filme].editaAtores()  # feito
                elif mudar == 6:
                    filmes[filme].editaDuracao()  # feito
                elif mudar == 7:
                    filmes[filme].editaValor()  # feito
    else:
        print('o filme não está contido na base de dados')
    return True


# procura filme

def procuraFilmesAdm():
    while True:
        filme = input('digite o filme de busca: ').title()
        print(filme)
        if filme in filmes:
            break
        else:
            print('filme não encontrado')
            return False
    filmes[filme].mostraInfos()

### main ###


usuarios = {
    'mariahh': Usuario('maria', 'mariahh', 18, 'F', 2),
    'joaozinho': Usuario('joao', 'joaozinho', 23, 'M', 2)
}
filmes = {
    'Clueless': Filme('Clueless', 1995, 'Amy Heckerling', ['Paul Rudd', 'Alicia Silverstone'], 97, ['Comédia'], 20),
    'Orgulho E Preconceito': Filme('Orgulho e Preconceito', 2006, 'Joe Wright', ['Keira Knightley', 'Matthew Macfadyen'], 127, ['Romance'], 15)
}

print("MOVIE TRACKER, o que deseja fazer?")
flag = True
while flag == True:
    while True:
        opcao = confereOpcao(
            "1 - fazer login com conta existente\n2 - criar uma nova conta\n0 - encerrar programa ", 0, 2)
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
