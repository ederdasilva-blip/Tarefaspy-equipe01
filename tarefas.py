tarefas=[]

def adicionar_tarefa():
    descricao = input("digite a descricao da tarefa: ").strip()

    tarefa = ({
        "descricao": descricao,
        "concluida": False
    })

    tarefas.append(tarefa)
    print("tarefa adicionada com sucesso!")