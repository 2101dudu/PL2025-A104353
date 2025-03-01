# TPC4

![foto perfil](../foto_perfil.jpg)

- **Data**: 01/03/2025
- **Nome**: Eduardo de Oliveira Sousa Faria
- **Número**: a104353

## Resumo

Criar um analisador léxico capaz de detetar e _tokenizar_ a linguagem de _query_ proposta:
Este exercício foi resolvido com uso à biblioteca `ply.lex`.

## Procedimento

1. Verificar e especificar os _tokens_ a serem tratados.
2. Criar expressões regulares para obter grupos de captura.
3. Para casos mais específicos, acrescentar regras extra.

## Resultados

Utilizando o comando `python3 tpc4.py`, obtém-se o seguinte resultado:

```
COMMENT # DBPedia: obras de Chuck Berry 2 1
SELECT select 3 33
VAR ? 3 40
ID nome 3 41
VAR ? 3 46
ID desc 3 47
WHERE where 3 52
LBRA { 3 58
VAR ? 4 64
ID s 4 65
A a 4 67
PREFIX dbo 4 69
TERM :MusicalArtist 4 72
DOT . 4 86
VAR ? 5 92
ID s 5 93
PREFIX foaf 5 95
TERM :name 5 99
QUERY "Chuck Berry" 5 105
TAG @en 5 118
DOT . 5 122
VAR ? 6 128
ID w 6 129
PREFIX dbo 6 131
TERM :artist 6 134
VAR ? 6 142
ID s 6 143
DOT . 6 144
VAR ? 7 150
ID w 7 151
PREFIX foaf 7 153
TERM :name 7 157
VAR ? 7 163
ID nome 7 164
DOT . 7 168
VAR ? 8 174
ID w 8 175
PREFIX dbo 8 177
TERM :abstract 8 180
VAR ? 8 190
ID desc 8 191
RBRA } 9 196
ID LIMIT 9 198
NUM 1000 9 204
```
