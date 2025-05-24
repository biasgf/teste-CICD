bebidas = []

for i in range(5):
    bebida1 = input('Digite o nome de uma bebida favorita')
    bebidas.append(bebida1)
bebidas= sorted(bebidas)

for bebida in bebidas:
    print(bebida)