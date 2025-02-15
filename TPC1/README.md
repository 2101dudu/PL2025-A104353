# TPC1

![foto perfil](../foto_perfil.jpg)

- **Data**: 31/01/2025
- **Nome**: Eduardo de Oliveira Sousa Faria
- **Número**: a104353

## Resumo

Somador on/off: criar o programa em Python

1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto
2. Sempre que encontrar a string "Off" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado
3. Sempre que encontrar a string "On" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado
4. Sempre que encontra o carater "=", o resultado da soma é colocado na saída

_exemplo_:

```
...45...
...2025-02-07...
...Off...
...789...43...
...on...2...
...5 = ...
```

_resultado_

```
ac = 45
+ 2025
+ 2
+ 7 (=2079)
+ 2
+ 5 -> print 2086
```

## Resultados

Executanto o programa com diferentes entradas de texto, obtem-se o seguinte resultado.

```bash
$ python3 tpc1.py < sample.txt
156
699
```

```bash
$ python3 tpc1.py < sample2.txt
3187
3257
3759
```

## Conclusões

O programa revela-se desnecessariamente complexto, mas fucnional.
