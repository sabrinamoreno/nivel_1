## Entrega do primeiro desafio da trilha de Back end com python, do Programa Trilhas Inova Maranhão ##
# Desafio 1 : entrega de um ponto de venda que aplica descontos, de acordo com os requisitos. #



historico = []

while True:

    print("\n===== SISTEMA DE PDV DO TRILHAS =====")

    valor = float(input("Digite o valor da compra (0 para encerrar): R$ "))

    if valor == 0:
        break

    if valor < 0:
        print("Valor inválido! Digite um valor positivo.")
        continue

    idade = int(input("Digite a idade do cliente: "))

    if idade < 0:
        print("Idade inválida! Digite uma idade positiva.")
        continue

    valor_original = valor

    desconto = 0

    if idade >= 65:
        valor = valor * 0.80

    if valor > 100:
        valor = valor * 0.90

    desconto = valor_original - valor

    historico.append([valor_original, desconto, valor])

    print("\n===== RESULTADO DA COMPRA =====")
    print(f"Valor original: R$ {valor_original:.2f}")
    print(f"Desconto concedido: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor:.2f}")


print("\n===== RESUMO DO DIA =====")

quantidade_compras = len(historico)
total_bruto = 0
total_descontos = 0
total_final = 0

for compra in historico:
    total_bruto += compra[0]
    total_descontos += compra[1]
    total_final += compra[2]

print(f"Quantidade de compras: {quantidade_compras}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")

print("\nSistema encerrado. Obrigado!")
