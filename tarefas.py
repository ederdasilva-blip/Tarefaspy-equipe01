tarefas=[]
def adicionar_tarefa():
    descricao = input("digite a descricao da tarefa:").strip()

    tarefa = ({
        "descricao": descricao,
        "concluida": False
    })
    tarefas.append(tarefa)
    print("tarefa adicionada com sucesso!")

def concluir_tarefa():
    if len(tarefas) ==0:
        print("Nenhuma tarefa cadastrada.")
    return

listar_tarefas()

try:
    numero = int(
        input("Digite o número da tarefa que deseja concluir:")
    )
    

    indice = numero - 1

    if indice < 0 or indice >= len(tarefas):
    print("tarefa inválida.")
    return

    tarefas[indice]["concluida"] = True

    print("Tarefa concluída com sucesso!")

except valueError:
    print("Digite um número válido")