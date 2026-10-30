<p align="center">
  <img src="https://img.shields.io/badge/Desenvolvedora-Sabrina%20Moreno-ff69b4?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/From-São%20Luís%2C%20MA-purple?style=for-the-badge&logo=googlemaps&logoColor=white" />
</p>

# Desafio Nível 1 (Python)

## 1. O que o código faz?

O projeto consiste no desenvolvimento de um sistema de Ponto de Venda (PDV) utilizando a linguagem Python. O programa recebe o valor de uma compra e a idade do cliente, calcula descontos de acordo com regras estabelecidas e apresenta o valor final a pagar. Além disso, permite registrar várias compras, armazenar os dados em uma lista e gerar um resumo ao final do dia, contendo a quantidade de compras, o total bruto, os descontos concedidos e o total final das vendas.

## 2. Como o código funciona?

O funcionamento do programa acontece por meio das seguintes etapas:

1. Primeiro, é criada uma lista vazia chamada `historico`, responsável por armazenar os dados das compras realizadas.
2. O programa utiliza uma estrutura de repetição `while` para permitir que várias compras sejam registradas.
3. São solicitados ao usuário o valor da compra e a idade do cliente.
4. O sistema verifica se os valores informados são negativos. Caso sejam, apresenta uma mensagem de aviso e solicita uma nova entrada.
5. Se o cliente possuir 65 anos ou mais, recebe um desconto de 20% sobre o valor da compra.
6. Em seguida, o programa verifica se o valor após o desconto por idade é superior a R$ 100,00. Caso seja, aplica mais 10% de desconto.
7. Os dados de cada compra são armazenados na lista `historico` utilizando o método `.append()`.
8. O valor original, o desconto concedido e o valor final são apresentados na tela.
9. Quando o usuário digita `0` no valor da compra, o sistema encerra o loop.
10. Por fim, uma estrutura `for` percorre a lista de compras e calcula o resumo do dia, apresentando a quantidade de compras, o total bruto, o total de descontos e o total final.

## 3. Como executar o programa?

É necessário ter o Python instalado no computador.

Abra o terminal na pasta `nivel_1` e execute o seguinte comando:

```bash
python pdv.py
```

Para encerrar o programa e visualizar o resumo do dia, digite `0` quando for solicitado o valor de uma nova compra.

## 4. Conceitos de Python utilizados

Durante o desenvolvimento do projeto, foram utilizados os seguintes conceitos:

- **Variáveis:** armazenamento dos valores das compras, idades e resultados dos cálculos.
- **Input():** recebimento de dados informados pelo usuário.
- **If/Else:** estruturas condicionais para verificar as regras de desconto e validar os dados.
- **While:** estrutura de repetição para permitir várias compras.
- **Break:** encerramento do loop quando o usuário digita zero.
- **Continue:** retorno ao início do loop quando uma entrada inválida é identificada.
- **Listas:** armazenamento do histórico das compras.
- **Append():** inserção de novos registros na lista.
- **For:** percorrer o histórico e calcular os totais.
- **Len():** contagem da quantidade de compras registradas.
- **Operadores matemáticos:** realização dos cálculos dos descontos e totais.
- **F-strings:** formatação dos valores monetários com duas casas decimais.

## 5. Tabela de exemplos e casos de teste

| Caso | Valor da compra | Idade | Valor final esperado |
| ---- | --------------: | ----: | -------------------: |
| 1    |        R$ 50,00 |    30 |             R$ 50,00 |
| 2    |       R$ 150,00 |    30 |            R$ 135,00 |
| 3    |        R$ 80,00 |    70 |             R$ 64,00 |
| 4    |       R$ 200,00 |    70 |            R$ 144,00 |
| 5    |       R$ 125,00 |    70 |            R$ 100,00 |
| 6    |       R$ 100,00 |    65 |             R$ 80,00 |
| 7    |       R$ 101,00 |    30 |             R$ 90,90 |
| 8    |       R$ 300,00 |    65 |            R$ 216,00 |
| 9    |        R$ 90,00 |    64 |             R$ 90,00 |
| 10   |       R$ 200,00 |    64 |            R$ 180,00 |

## 6. Estrutura de entrega

A pasta do projeto está organizada da seguinte maneira:

```text
nivel_1/
├── pdv.py
└── README.md
```

O arquivo `pdv.py` contém o código-fonte do sistema de Ponto de Venda, enquanto o arquivo `README.md` apresenta a documentação, explicando seu funcionamento, os conceitos utilizados e os casos de teste.

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Concluído-2ea44f?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Nível-Iniciante-ffb6c1?style=for-the-badge" />

</p>
