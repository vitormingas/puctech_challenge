# sistema_estoque_farmacia.py

# Sistema de estoque para uma farmacia
# vitormingas - 2025

# Estoque inicial (pode ser vazio)
estoque = {}

# Exemplo de funções:
def adicionar_medicamento():
    nome = input("Digite o nome do medicamento: ")
    try:
        quantidade = int(input("Digite a quantidade inicial: "))
    except ValueError:
        print("❌ Quantidade inválida.")
        return
    if nome in estoque:
        print(f"❌ {nome} já existe no estoque, utilize a função de atualizar.")
    else:
        estoque[nome] = quantidade
        print(f"✅ {nome} adicionado ao estoque com {quantidade} unidades iniciais com sucesso!")

def atualizar_estoque():
    nome = input("Digite o nome do medicamento que deseja atualizar: ")
    try:
        nova_qtd = int(input("Digite a quantidade a ser adicionada: "))
    except ValueError:
        print("❌ Quantidade inválida.")
        return
    if nome in estoque:
        estoque[nome] += nova_qtd
        print(f"✅ {nome} atualizado. Agora existem {estoque[nome]} unidades no estoque.")
    else:
        print(f"❌ Não foi possível localizar {nome} no estoque.")

def listar_estoque():
    if not estoque:
        print("❌ Estoque vazio.")
        return
    print("\n📋 Estoque atual:")
    for nome, qtd in estoque.items():
        status = "🔴 Esgotado" if qtd == 0 else "🟡 Crítico" if qtd <= 5 else "🟢 OK"
        print(f"{nome:<20} | Quantidade: {qtd} | Status: {status}")

def deletar_medicamento():
    nome = input("Digite o nome do medicamento a ser removido: ")
    if nome in estoque:
        del estoque[nome]
        print(f"✅ {nome} foi removido com sucesso do estoque.")
    else:
        print(f"❌ Não foi possível localizar {nome} no estoque.")

def processar_pedidos():
    entrada = input("Digite os medicamentos pedidos separados por vírgula: ")
    pedidos = [x.strip() for x in entrada.split(",")]
    for nome in pedidos:
        if nome in estoque and estoque[nome] > 0:
            estoque[nome] -= 1
            print(f"⚙️  Pedido de {nome} processado. Restam {estoque[nome]} unidades.")
        elif nome in estoque:
            print(f"❌ {nome} está esgotado.")
        else:
            print(f"❌ {nome} não está cadastrado no estoque.")

def exibir_resumo():
    print("\n📦 Resumo final do estoque:")
    listar_estoque()

# Menu interativo
def menu():
    while True:
        print("\n=== Menu do Sistema de Estoque ===")
        print("1. Adicionar medicamento")
        print("2. Atualizar estoque")
        print("3. Listar estoque")
        print("4. Remover medicamento")
        print("5. Processar pedidos")
        print("6. Exibir resumo")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_medicamento()
        elif escolha == "2":
            atualizar_estoque()
        elif escolha == "3":
            listar_estoque()
        elif escolha == "4":
            deletar_medicamento()
        elif escolha == "5":
            processar_pedidos()
        elif escolha == "6":
            exibir_resumo()
        elif escolha == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("❌ Opção inválida.")

# Inicia o programa
menu()