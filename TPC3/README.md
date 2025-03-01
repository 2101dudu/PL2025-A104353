# TPC3

![foto perfil](../foto_perfil.jpg)

- **Data**: 22/02/2025
- **Nome**: Eduardo de Oliveira Sousa Faria
- **Número**: a104353

## Resumo

Criar um programa em Python que receba um ficheiro _markdown_ e converta os principais elementos textuais em HTML.

## Procedimento

- **Headers**: in: `## Exemplo`; out: `<h2>Exemplo</h2>`
- **Bold**: in: `**Exemplo**`; out: `<b>Exemplo</b>`
- **Itálico**: in: `*Exemplo*`; out: `<i>Exemplo</i>`
- **Lista Numerada**:
  in:
  ```
      1. Item1
      2. Item2
      3. Item3
  ```
  out:
  ```html
  <ol>
    <li>Item1</li>
    <li>Item2</li>
    <li>Item3</li>
  </ol>
  ```
- **Link**: in: `[Regex](https://regex101.com/)`; out: `<a href="https://regex101.com/">Regex</a>`
- **Imagem**: in: `![Foto](foto.png)`; out: `<img src="foto.png" alt="Foto"/>`

## Resultados

Utilizando o comando `python3 tpc3.py < sample.md >> index.html`, obtém-se o resultado visível em `index.html`.
