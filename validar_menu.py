from tarefas import adicionar_tarefa

def menu():
    print('='*25)
    print('Tarefaspy'.center(25))
    print('='*25)
    print('''
1 - Adicionar tarefa
2 - Listar tarefa
3 - Concluir tarefa
4 - Remover tarefa
0 - Sair
''')

def validar_opção_menu():
    while True:
        tarefas = []

        try:
            menu()
            opção = int(input("Digite a opção: "))
            if opção not in (0, 1, 2, 3, 4):
                print("Opção inválida.")

            if opção == 1:
                adicionar = adicionar_tarefa()
                continue

            elif opção == 0:
                print('Encerrando Programa...')
                break
                
        except ValueError:
            print("Digite uma opção válida")

validar_opção_menu()