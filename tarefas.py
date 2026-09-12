tarefas=[]
def adicionar_tarefa():
    descricao = input("digite a descricao da tarefa:").strip()

    tarefa = ({
        "descricao": descricao,
        "concluida": False
    })
    tarefas.append(tarefa)
    print("tarefa adicionada com sucesso!")

    
def remover_tarefa():
    if len(tarefas) == 0:
        print("Nenuma tarefa cadastrada.")
        return

    listar_tarefas()
        try:
            numero = int(
                input("Digite o número da tarefa que deseja remover: ")
            )

            indice = numero - 1

            if indice < 0 or indice >= len(tarefas):
                print("Tarefa inválido.")
                return

            tarefa_removida = tarefas.pop(indice)
            
            print(
                f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso."
                )

        except ValueError:
            print("Digite um número válido.")