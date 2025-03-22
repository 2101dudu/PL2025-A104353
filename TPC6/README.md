# TPC6

![foto perfil](../foto_perfil.jpg)

- **Data**: 22/03/2025
- **Nome**: Eduardo de Oliveira Sousa Faria
- **Número**: a104353

## Resumo

Este trabalho consiste na implementação de um parser LL(1) recursivo descendente.
O programa utiliza um analisador léxico (`exp_lex.py`) para interpretar e _tokenizar_ o _input_, e um analisador sintático (`exp_sin_val`) para calular o valor das expressões aritméticas a ele atribuídas.

_Produções_:

```
Exp -> Exp ADD Termo
     | Exp SUB Termo
     | Termo
Termo -> Termo MUL Fator
       | Fator
Fator -> NUM
       | PARA Exp PARF
```
