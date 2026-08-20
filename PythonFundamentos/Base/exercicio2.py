pedidos = [    {"id": 1, "produto": "Notebook", "quantidade": 1, "preco": 2500},
    {"id": 2, "produto": "Mouse", "quantidade": 2, "preco": 50},
    {"id": 3, "produto": "Teclado", "quantidade": 1, "preco": 120},
    {"id": 0, "produto": "Outros", "quantidade": 0, "preco": 0},  # Remover
    {"id": 4, "produto": "Monitor", "quantidade": 1, "preco": 800},
    {"id": 0, "produto": "Outros", "quantidade": 0, "preco": 0},  # Remover
    {"id": 5, "produto": "Webcam", "quantidade": 3, "preco": 150}
]

print("=" * 10)
print("INFORMAÇÕES DE PEDIDOS")
print("=" * 10)

pedidos.pop(-4)
pedidos.pop(-2)
print(pedidos)

pedidos_index = int(input("Informe o index do pedido que deseja obter informações"))
pedido = pedidos[pedidos_index]

print(f"Pedido index {pedidos_index}: {pedido['produto']} - {pedido['quantidade']}x - R${pedido['preço']} - Total: R${pedido['quantidade'] * pedido['preço']}* ")