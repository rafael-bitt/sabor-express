import os

restaurantes = [{'nome':'Six', 'categoria': 'Lanche', 'ativo': False},
                {'nome':'Atacado', 'categoria': 'Pizza', 'ativo': True},
                {'nome':'Piadina', 'categoria': 'Italiano', 'ativo': False}]

def exibir_nome_do_programa():
    ''' Essa função é responsável por exibir o nome do programa de forma estilizada'''
    print("""
𝙎𝙖𝙗𝙤𝙧 𝙀𝙭𝙥𝙧𝙚𝙨𝙨
""")

def exibir_opcoes():
    ''' Essa função é responsável por exibir as opções '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Essa função é responsável por finalizar o app '''
    exbir_subtitulos('App finalizado')

def voltar_menu_principal():
    ''' Essa função é responsável por  solicitar uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal

    '''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    ''' Essa função é responsável por mostrar uma opção como inválida e volta ao menu principal
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção inválida!\n')
    voltar_menu_principal()

def exbir_subtitulos(texto):
    ''' Essa função é responsável por exibir os subtítulos estilizados
    
    inputs:
    - Texto: str - O texto do subtítulo
    
    '''
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs: 
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exbir_subtitulos('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastar: ')
    categoria = input(f'Digite o nome da categoria do restauratne {nome_do_restaurante}: ')
    dados_restautante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restautante)
    print(f'O nome do restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu_principal()

def listar_restaurantes():
    ''' Essa função é responsável por listar os restaurantes
    
    Outputs:
    - Exibe a lista de restaurantes na tela

    '''
    exbir_subtitulos('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante ['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_menu_principal()

def alternar_estado_restaurante():
    ''' Essa função é responsável por alternar o estado de um restaurante entre ativo/desativado
    
    Outputs:
    - Exibe mensagem de sucesso na operação
    
    '''
    exbir_subtitulos('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'\nO restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'\nO restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('\nO restaurante não foi encontrado')


    voltar_menu_principal()

def escolher_opcao():
    ''' Essa função é responsável por definir a escolha de uma opção 
    
    Outputs:
    - Executa a opção escolhida pelo usuário

    '''
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

# opcao_escolhida = int(input('Escolha uma opção: '))
# match opcao_escolhida:
#     case 1:
#         print('Adicionar restaurante')
#     case 2:
#         print('Listar restaurantes')
#     case 3:
#         print('Ativar restaurante')
#     case 4:
#         print('Finalizar app')
#     case _:
#         print('Opção inválida!')

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()