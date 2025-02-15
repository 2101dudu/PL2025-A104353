# TPC2

![foto perfil](../foto_perfil.jpg)

- **Data**: 15/02/2025
- **Nome**: Eduardo de Oliveira Sousa Faria
- **Número**: a104353

## Resumo

Para cada alínea, é lida cada linha proveniente do _stdin_ e aplicada uma expressão regular.
Dada a natureza do documento de input, certas expressões possuem _safety measures_ que asseguram que algumas inconcistências são efetivamente salvaguardadas.

#### 1.

Nesta pergunta, é pedido uma lista ordenada dos compositores musicais. Começei por filtrar o nome dos mesmos utilizando a seguinte expressão: `\d\d\d\d;[^;]*;([^;]*);`
- `\d\d\d\d;`: encontra o padrão de 4 dígitos seguidos, útil para o ano associado a cada entrada. ex.: ...;`1914;`...
- `[^;]*;`: encontra qualquer caracter que não seja `;`. deste modo, seleciona-se o atributo período. ex.: ...;`Medieval;`... ou ...;`Século XX;`...
- `([^;]*)`: seleciona o padrão associado ao atributo do nome do compositor

Deste modo, é possível extrair o grupo resultado de `re.search(...)` para obter o nome do compositor. Juntando os nomes de todos os compositores numa listaq, e dando _sort_ da mesma, obtemos o resultado pretendido.

#### 2.

A segunda pergunta pretende um resultado que demonstre o número de obras por período. Novamente, fiz uso da expressão regular `\d\d\d\d;([^;]*);[^;]*;` para filtrar as linhas do _stdin_ pelo atributo.
Esta expressão é parecida com a usada anteriormente, alterando apenas o conjunto selecionado pelo uso dos parênteses para favorecer o atributo do período.
Restou apenas registar quantas vezes cada período aparecia para obter o resultado esperado.

#### 3.

A última pergunta esperava por um _output_ representativo de uma categorização dos vários nomes das obras de um período, ordenadas por ordem alfabética.
Para isso, após algumas iterações, fiz uso da expressão regular `(((\d\d\d\d;)([^;]*);.*$)|^([^;\n]*);[^ \w])`.
- `(...|...)`: permite à expressão funcionar de dois modos — encontrar o nome da obra ou o período da mesma
- `((\d\d\d\d;)([^;]*);.*$)`: procura pelo atributo período a partir do fim da linha
- `^([^;\n]*);[^ \w])`: procura pelo atributo do nome da obra

Esta expressão regular é bastante robusta e é capaz de lidar com diversos cenários, como a inclusão de um `;` no texto descritivo. Restou apenas registar os vários períodos e associar, a cada um, obras da sua época.

## Resultados

Invocando as funções associadas a cada pergunta, respetivamente, obtêm-se os seguintes resultados:

#### 1.

```bash
$ python3 tpc2.py < Document.csv                                                                                                                                                                                                      ─╯
['Alessandro Stradella', 'Antonio Maria Abbatini', 'Bach, Johann Christoph', 'Bach, Johann Michael', 'Bach, Johann Michael', 'Bach, Wilhelm Friedemann', 'Bach, Wilhelm Friedemann', 'Bach, Wilhelm Friedemann', 'Balbastre, Claude', 'Balbastre, Claude', 'Baldassare Galuppi', 'Barbara of Portugal', 'Barbara of Portugal', 'Benda, Franz', 'Benda, Franz', 'Benda, Franz', 'Bernardo Pasquini', 'Biber, Heinrich Ignaz Franz', 'Bononcini, Giovanni Battista', 'Boyvin, Jacques', 'Bull, John', 'Cabanilles, Juan Bautista', 'Cabanilles, Juan Bautista', 'Caldara, Antonio', 'Caldara, Antonio', 'Caldara, Antonio', 'Caldara, Antonio', 'Carissimi, Giacomo', 'Carissimi, Giacomo', 'Carissimi, Giacomo', 'Cavalli, Francesco', 'Cristofaro Caresana', 'David Perez', 'Dieterich Buxtehude', 'Domenico Scarlatti', 'Duarte Lobo', 'Duarte Lôbo', 'Durante, Francesco', 'Durante, Francesco', 'Elisabeth Sophie of Mecklenburg', "Emanuele d'Astorga", "Emanuele d'Astorga", 'Estevao de Brito', 'Estevao de Brito', 'Fernandes, Gaspar', 'Filipe De Magalhaes', 'Friederike Sophie Wilhelmine', 'Friederike Sophie Wilhelmine', 'Friederike Sophie Wilhelmine', 'Froberger, Johann Jakob', 'Georg Bohm', 'Georg Muffat', 'Gibbons, Orlando', 'Gibbons, Orlando', 'Gibbs, Joseph', 'Gibbs, Joseph', 'Giovanni Battista Bassani', 'Giovanni Battista Bassani', 'Giovanni Gabrieli', 'Giovanni Gabrieli', 'Giovanni Legrenzi', 'Giuseppe Tartini', 'Gregor Aichinger', 'Gregor Aichinger', 'Gregorio Allegri', 'Handel, George Frideric', 'Hans Leo Haßler', 'Hasse, Johann Adolph', 'Hasse, Johann Adolph', 'Haym, Nicola Francesco', 'Haym, Nicola Francesco', 'Heinrich Scheidemann', 'Henri Desmarets', 'Jan Pieterszoon Sweelinck', 'Jan Pieterszoon Sweelinck', 'Jean-Joseph Mouret', 'Jean-Joseph Mouret', 'Jean-Joseph Mouret', 'Jean-Marie Leclair', 'Jean-Marie Leclair', 'Jeremiah Clarke', 'Johann Christoph(er) Pepusch', 'Johann David Heinichen', 'Johann Ernst Eberlin', 'Johann Ernst Eberlin', 'Johann Hermann Schein', 'Johann Joachim Quantz', 'Johann Joachim Quantz', 'Johann Krieger', 'Johann Nicolaus Bach', 'John Blow', 'John Blow', 'John Blow', 'John Dowland', 'John Dowland', 'John Dowland', 'John Eccles', 'John IV', 'John IV', 'John IV', 'Krebs, Johann Ludwig', 'Krebs, Johann Ludwig', 'Krebs, Johann Ludwig', 'Leopold I', 'Louis Couperin', 'Lully, Jean-Baptiste', 'Lôbo, Duarte', 'Machado, Manuel', 'Madre De Deus, Filpe Da', 'Manuel Cardoso', 'Manuel Correia', 'Manuel Correia', 'Manuel Correia', 'Manuel Correia', 'Manuel Rodriguez Coelho', 'Manuel Rodriguez Coelho', 'Marais, Marin', 'Marc-Antoine Charpentier', 'Martini, Giovanni Battista', 'Martini, Giovanni Battista', 'Mattheson, Johann', 'Melchior Schildt', 'Michael Praetorius', 'Mondonville, Jean-Joseph', 'Monsieur de Sainte-Colombe', 'Monsieur de Sainte-Colombe', 'Monteverdi, Claudio', 'Neander, Joachim', 'Neander, Joachim', 'Neander, Joachim', 'Nicolas Siret', 'Nicolaus Bruhns', 'Nicolaus Bruhns', 'Nivers, Guillaume-Gabriel', 'Paolo Agostino', 'Paolo Agostino', 'Pedro de Araujo', 'Pedro de Araujo', 'Pergolesi, Giovanni Battista', 'Pergolesi, Giovanni Battista', 'Peri, Jacopo', 'Peter Philips', 'Peter Philips', 'Peter Philips', 'Pierre Beauchamp', 'Pietro Della Valle', 'Rameau, Jean-Philippe', 'Reincken, Johann Adam', 'Reincken, Johann Adam', 'Reincken, Johann Adam', 'Robert Cambert', 'Robert Cambert', 'Robert Cambert', 'Rousseau, Jean-Jacques', 'Rousseau, Jean-Jacques', 'Sammartini, Giovanni Battista', 'Sammartini, Giuseppe', 'Samuel Scheidt', 'Samuel Scheidt', 'Sanz, Gaspar', 'Schenck, Johannes', 'Seixas, Carlos', 'Stefano Landi', 'Stefano Landi', 'Strozzi, Barbara', 'Titelouze, Jean', 'Titelouze, Jean', 'Tomaso Albinoni', 'Viadana, Lodovico Grossi da', 'Viadana, Lodovico Grossi da', 'Weldon, John', 'Weldon, John', 'Weldon, John', 'Wilhelmine of Prussia']
```

#### 2.

```bash
$ python3 tpc2.py < Document.csv                                                                                                                                                                                                      ─╯
{'Barroco': 26, 'Clássico': 15, 'Medieval': 48, 'Renascimento': 41, 'Século XX': 18, 'Romântico': 19, 'Contemporâneo': 7}
```

#### 3.

```bash
$ python3 tpc2.py < Document.csv                                                                                                                                                                                                      ─╯
Barroco : 26 ; ['Ab Irato;"', 'Die Ideale, S.106;"', 'Fantasy No. 2;"', 'Hungarian Rhapsody No. 16;"', 'Hungarian Rhapsody No. 5;"', 'Hungarian Rhapsody No. 8;"', 'Impromptu Op.51;"', 'In the Steppes of Central Asia;"', 'Mazurkas, Op. 50;"', 'Military Band No. 1;"', 'Nocturne in C minor;"', 'Paganini Variations, Book I;"', 'Polonaise Op. 44;"', 'Polonaise-Fantasie;"', 'Polonaises Op.71;"', 'Preludes Op. 11;"', 'Preludes Op. 49;"', 'Prince Rostislav;"', 'Rage Over a Lost Penny;"', 'Rondo Op. 5;"', 'Shéhérazade, ouverture de féerie;"', 'Symphonies de Beethoven;"', 'The Rondo;"', 'Transcendental Études;"', 'Études Op. 25;"', 'Études Op.10;"']
Clássico : 15 ; ['Bamboula, Op. 2;"', 'Capriccio Italien;"', 'Czech Suite;"', 'French Overture;"', 'Hungarian Rhapsody No. 14;"', 'Hungarian Rhapsody No. 18;"', 'Händelgesellschaft volume 50;"', 'In Nature\'s Realm;"', 'Mass in C major;"', 'Scherzo No.3;"', 'Serenade for Strings in G minor;"', 'Serenata Notturna;"', 'Stabat Mater;"', 'Suite for Orchestra in B minor;"', 'Zärtliche Liebe;"']
Medieval : 48 ; ['Adagio in B minor;"', 'Ballade No.1;"', 'Ballades, Op. 10;"', 'Barcarole Op. 60;"', 'Coriolan Overture;"', 'Dixit Dominus;"', 'Eroica Variations;"', 'Fantasia and Fugue, BWV 542, G minor;"', 'Fantasia in D minor;"', 'Fantasy on Hungarian Folk Themes;"', 'Faust Overture;"', 'Gigue in G major, K. 574;"', 'Grande valse brillante;"', 'Hungarian Rhapsody No. 11;"', 'Hungarian Rhapsody No. 13;"', 'Hungarian Rhapsody No. 15;"', 'Hungarian Rhapsody No. 3;"', 'Hungarian Rhapsody No. 4;"', 'Hungarian Rhapsody No. 7;"', 'Impromptu Op.51;"', 'La Savane;"', 'Mass in C major;"', 'Mazurkas, Op. 63;"', 'Mazurkas, Op. 67;"', 'Mazurkas, Op. 68;"', 'Morceau de salon;"', 'Preludes Op. 11 No. 4;"', 'Preludes Op. 74;"', 'Première rhapsodie;"', 'Prélude, Choral et Fugue;"', 'Rhapsodie Espagnole;"', 'Romance in F major;"', 'Rondo for Piano No. 3;"', 'Schubert\'s Valses Nobles;"', 'Serenade for Wind Instruments;"', 'Suite No. 1 for two pianos;"', 'Suite No. 2 for two pianos;"', 'Suite in D minor, HWV 437;"', 'Tapiola;"', 'The Noon Witch;"', 'Three Pieces for Orchestra;"', 'Tragic Overture;"', 'Transcendental Études;"', 'Tönet, ihr Pauken! Erschallet, Trompeten!, BWV 214;"', 'Valses Sentimentales;"', 'Variations in F minor;"', 'Variations on a Theme of Corelli, Op. 42;"', 'Wedding day at Troldhaugen;"']
Renascimento : 41 ; ['Bagatelles, Opus 119;"', 'Bagatelles, Opus 33;"', 'Cantatas, BWV 141-150;"', 'Carnival Overture;"', 'Eroica Variations;"', 'Fantaisie brillante, Op. 22;"', 'Festklänge, S.101;"', 'Funeral March in Memory of Rikard Nordraak;"', 'Hamlet, S.104;"', 'Hungarian Rhapsody No. 10;"', 'Hungarian Rhapsody No. 12;"', 'Hungarian Rhapsody No.1;"', 'Komm, Jesu, komm!;"', 'L\'Art de varier;"', 'Le Mancenillier;"', 'Legends, Op.59;"', 'Liturgy of St. John Chrysostom;"', 'Marie-Magdeleine;"', 'Mazurkas, Op. 56;"', 'Morceaux de Salon, Op. 10;"', 'Nocturne in A-flat;"', 'Othello;"', 'Polonaises, Op.26;"', 'Preludes Op. 11;"', 'Preludes, Op. 32;"', 'Romance in G major;"', 'Rondo Op. 1;"', 'Scans of the Bach Gesellschaft edition of the Eight Short Preludes and Fugues;"', 'Scherzo No.4;"', 'Schubert\'s Valses Nobles;"', 'Shéhérazade;"', 'Six Pieces for Piano, Op. 118;"', 'St. Paul\'s Suite;"', 'Symphonic Dances, Op. 64;"', 'The Creatures of Prometheus;"', 'Transcendental Études;"', 'Transcendental Études;"', 'Valse romantique;"', 'Variation on a Waltz by Diabelli;"', 'Vers la flamme;"', 'Études Op. 25;"']
Século XX : 18 ; ['Berceuse;"', 'Eleven Chorale Preludes, Op. 122;"', 'Fürchte dich nicht;"', 'Hungarian Rhapsody No. 17;"', 'Hungarian Rhapsody No. 9;"', 'Nocturnes Op. Posth. 72;"', 'Papillons;"', 'Peer Gynt Suite Suite No. 1;"', 'Serenade for Strings;"', 'Sigurd Jorsalfar;"', 'Singet dem Herrn ein neues Lied;"', 'Sonatas and Partitas for Solo Violin;"', 'Sonatina in F major;"', 'Sonatina in G;"', 'Symphonic Poem No.1, Ce qu\'on entend sur la montagne;"', 'The Storm, Op.76;"', 'Variations on a Theme of Chopin, Op. 22;"', 'Études Op. 25;"']
Romântico : 19 ; ['Book II;"', 'Fantasy No. 4;"', 'Feu d\'artifice;"', 'Feuilles d\'Album;"', 'Grande Tarantelle;"', 'Jeux d\'enfants;"', 'Lobet den Herrn, alle Heiden;"', 'Moments musicaux;"', 'Overture, Scherzo and Finale;"', 'Preludes Op. 11;"', 'Preludes Op. 59;"', 'Präludium und Fuge über das Thema B-A-C-H;"', 'Psalm 42 , Op. 42;"', 'Salve Regina;"', 'Scherzo No. 2;"', 'Syrinx;"', 'Waltzes, Op. 34;"', 'Études Op. 25;"', 'Études Op.10;"']
Contemporâneo : 7 ; ['Impromptu Op.51;"', 'Les cinq doigts;"', 'Polonaises, Op.40;"', 'Preludes Opus 51;"', 'Rhapsodies, Op. 79;"', 'Sonnerie de Ste-Geneviève du Mont-de-Paris;"', 'Études Op. 25;"']
```
