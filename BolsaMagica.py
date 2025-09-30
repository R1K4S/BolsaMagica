import json
import customtkinter as ctk

ARQUIVO = "itens.json"

def carregar_json():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
def salvar_itens(itens):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(itens,f,indent=4,ensure_ascii=False)
#Interface
app = ctk.CTk()
app.title("Bolsa Mágica")
app.geometry("400x400")
app.mainloop()
#Funcoes
#Create
def criar_item():
    itens = carregar_json()
    nome = input("Digite o nome do Item Mágico: ")
    tipo = input("Digite o tipo do Item Mágico: ")
    novo_id = 1 if not itens else itens [-1]["id"]+1
    novo_item = {"id": novo_id,"nome": nome,"tipo": tipo}
    itens.append(novo_item)
    salvar_itens(itens)
    print(f"Item '{nome}' Item colocado com sucesso na bolsa")
#Read
def ler_item():
    itens = carregar_json()
    if not itens:
        print("Não existes itens na Bolsa")
    else:
        print("--Bolsa Mágica--")
        for item in itens:
            print(f"{item['id']}. | {item['nome']} | {item['tipo']}")
#Delete
def deletar_item():
    itens = carregar_json()
    itemSelect = int(input("Qual item desejar retirar: "))
    itemFound = None
    for item in itens:
        if item["id"]== itemSelect:
            itens.remove(item)
            salvar_itens(itens)
            print("Item retirado com sucesso da bolsa")
            itemFound = True
            break
    if not itemFound:
            print("Item na bolsa não existe")            
#Menu
def menu():
    while True:
        print("Bem vindo Invocador a Bolsa Mágica!")
        print("Como posso te servir hoje?")
        print("1.Colocar um item na Bolsa Mágica")
        print("2.Ver que itens tem na Bolsa Mágica")
        print("3.Retirar um item da Bolsa Mágica")
        print("4.Guardar a Bolsa Mágica")

        escolha = input("Invocador: ")

        if escolha == "1":
            criar_item()
        elif escolha == "2":
            ler_item()
        elif escolha == "3":
            deletar_item()
        elif escolha == "4":
            print("Fechando a Bolsa Mágica, Boa sorte na sua aventura Invocador!!!")
            return
        else:
            print("Não entendi seu pedido Invocador,poderia falar o numero novamente")
#Main
menu()
    