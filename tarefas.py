tarefas=[]

def adicionar_tarefa():
    descricao = input("digite a descricao da tarefa: ").strip()

    tarefa = ({
        "descricao": descricao,
        "concluida": False
    })

    tarefas.append(tarefa)
    print("tarefa adicionada com sucesso!")
    
def listar_tarefas():
    if len(tarefas) == 0:
        print("nenhuma tarefa cadastrada")
        return
    
    
        print ("\n======== Tarefas =========")
    
    for indice, tarefa in enumerate(tarefas):
        if tarefa["concluida"]:
            status = "X"
        else: 
            status = " "
            
    print (
        f"{indice + 1} -  [{status}] {tarefa['descricao']}"
    )