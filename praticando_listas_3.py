lista_moto = [] #lista vazia

print('Vai ser feita 3 perguntas, responda cada pergunta com uma marca.')

moto1 = str(input('Digite uma marca de moto: '))
moto2 = str(input('Digite mais uma marca de moto: '))
moto3 = str(input('Digite outra marca de moto: '))

#adicionando a lista o que o usuario digitar, e usando .title para deixar em maiucula a primeira letra
lista_moto.append(moto1.title())
lista_moto.append(moto2.title())
lista_moto.append(moto2.title())

print(f'Essa é sua lista {lista_moto}')

while True: # while true para sempre repetir a pergunta de adicionar ou remover ate que digite sair para encerrar.
    print('Deseja adicionar mais alguma ou remover ou sair?')
    opcao = str(input('[adicionar]  | [remover] | [sair]: '))

    if opcao == 'adicionar' or opcao == 'Adicionar':
        moto4 = str(input('Digite a marca que quer adicionar: '))
        lista_moto.append(moto4.title())
        print(lista_moto)

    elif opcao == 'remover' or opcao == 'Remover':
        remover = str(input('Digite a marca que quer remover: '))

        if remover == moto1:
            moto_removida = lista_moto.pop(0)
            print(f'O item {moto_removida} foi removido da lista.')
            print(lista_moto)

        elif remover == moto2:
            moto_removida = lista_moto.pop(1)
            print(f'O item {moto_removida} foi removido da lista.')
            print(lista_moto)
            
        elif remover == moto3:
            moto_removida = lista_moto.pop(2)
            print(f'O item {moto_removida} foi removido da lista.')
            print(lista_moto)

        elif remover == moto4:
            moto_removida = lista_moto.pop(3)
            print(f'O item {moto_removida} foi removido da lista.')
            print(lista_moto)
            
    elif opcao == 'sair' or opcao == 'Sair':
        print('Ok. Tchau...')
        break

    else:
        print('Comando invalido. ERROR')