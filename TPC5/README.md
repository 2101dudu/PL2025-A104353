# TPC5

![foto perfil](../foto_perfil.jpg)

- **Data**: 14/03/2025
- **Nome**: Eduardo de Oliveira Sousa Faria
- **Número**: a104353

## Resumo

Este trabalho consiste na implementação de uma simulação de uma máquina de _vending_.
O programa utiliza a biblioteca `ply.lex` para análise léxica e processa comandos que permitem listar produtos, inserir moedas, selecionar produtos e terminar o programa.
O estado do stock é armazenado num ficheiro JSON (`stock.json`), que é carregado no arranque e atualizado com o término da execução.

## Procedimento

1. Leitura do stock a partir do ficheiro `stock.json`

2. Processar os comandos `LISTAR`, `MOEDA`, `SELECIONAR` e `SAIR` introduzidos pelo utilizador

3. Validação de situações como:

   - Produto inexistente
   - Stock vazio
   - Saldo insuficiente para a compra

## Resultados

Utilizando o comando `python3 tpc5.py`, obtém-se um possível exemplo :

```sh
maq: 2024-03-08, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR
maq:
cod    |  nome      |  quantidade  |  preço
---------------------------------
        A23        |        água 0.5L                              |      7        |      0.7
        B12        |        refrigerante cola 0.33L                |      5        |      1.2
        C34        |        sumo de laranja 0.25L                  |      6        |      1.0
        D45        |        pacote de batatas fritas               |      10       |      1.5
        E56        |        barra de chocolate                     |      7        |      1.3
        F67        |        pastilha elástica                      |      14       |      0.5
        G78        |        bolacha recheada                       |      9        |      1.1
        H89        |        café em lata                           |      4        |      1.8
        I90        |        chá gelado 0.33L                       |      6        |      1.2
        J01        |        barrita de cereais                     |      12       |      1.0
>> SELECIONAR A23
maq: Saldo insufuciente
maq: Saldo = 0e0c
maq: Produto = 0e70c
MOEDA 1e, 20c, 5c, 5c
maq: Saldo = 1e30c
>> SELECIONAR A23
maq: Produto comprado
maq: Saldo restante = 0e60c
>> LISTAR
maq:
cod    |  nome      |  quantidade  |  preço
---------------------------------
        A23        |        água 0.5L                              |      6        |      0.7
        B12        |        refrigerante cola 0.33L                |      5        |      1.2
        C34        |        sumo de laranja 0.25L                  |      6        |      1.0
        D45        |        pacote de batatas fritas               |      10       |      1.5
        E56        |        barra de chocolate                     |      7        |      1.3
        F67        |        pastilha elástica                      |      14       |      0.5
        G78        |        bolacha recheada                       |      9        |      1.1
        H89        |        café em lata                           |      4        |      1.8
        I90        |        chá gelado 0.33L                       |      6        |      1.2
        J01        |        barrita de cereais                     |      12       |      1.0
>> SAIR
maq: Troco = 1x 50c e 1x 10c
```
