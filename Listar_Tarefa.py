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