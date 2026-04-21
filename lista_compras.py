print('-' * 10)
print('Bem vindo ao To Do on Supermarket')
print('Aqui você pode organizar sua lista de compras como desejar')
print('-' * 10)

lista = {}
produtos_nao_comprados = []

while True:
    print("=" * 30)
    print("   🛒 LISTA DE COMPRAS")
    print("=" * 30)
    print("1 - Adicionar itens")
    print("2 - Remover itens")
    print("3 - Ver lista de compras")
    print("4 - Sair")
    print("=" * 30)

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print("Você escolheu Adicionar itens")
            item = input("Digite o item a ser adicionado: ")
            categoria = input("Digite a categoria do item: ")

            if categoria not in lista:
                lista[categoria] = []  # cria a categoria automaticamente

            lista[categoria].append(item)
            print(f"✅ '{item}' adicionado na categoria '{categoria}' com sucesso!")

        case "2":
            print("Você escolheu Remover itens")
            print('Aqui você pode conferir os itens que já adicionou no carrinho ou não')

            if not lista:
                print("⚠️ A lista está vazia!")
            else:
                remover_categoria = input("Informe a categoria do item: ")
                remover_item = input("Informe o item que deseja remover: ")

                if remover_categoria in lista:
                    if remover_item in lista[remover_categoria]:
                        lista[remover_categoria].remove(remover_item)
                        produtos_nao_comprados.append(remover_item)
                        print(f"✅ '{remover_item}' removido com sucesso!")

                        # Remove a categoria se ficar vazia
                        if not lista[remover_categoria]:
                            del lista[remover_categoria]
                            print(f"📦 Categoria '{remover_categoria}' removida pois ficou vazia.")
                    else:
                        print("❌ Item não encontrado, tente novamente.")
                else:
                    print("❌ Categoria não encontrada, verifique novamente.")

        case "3":
            print("Você escolheu Ver lista de compras")

            if not lista:
                print("⚠️ A lista está vazia!")
            else:
                for categoria in sorted(lista):           # ordena categorias
                    print(f"\n📦 {categoria}:")
                    for item in sorted(lista[categoria]):  # ordena itens
                        print(f"  - {item}")
            
                # Exibe produtos removidos
            print("\n" + "=" * 30)
            if produtos_nao_comprados:
                print("🗑️ Produtos removidos da lista:")
                for produto in produtos_nao_comprados:
                    print(f"  - {produto}")
            else:
                print("✅ Nenhum produto foi removido ainda.")

        case "4":
            print("Até logo! 🛒")
            break

        case _:
            print("❌ Opção inválida! Escolha entre 1 e 4.")