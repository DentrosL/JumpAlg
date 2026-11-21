# Experimento: ordenações e busca em salto

Projeto em Python para comparar Insertion Sort, Selection Sort e Merge Sort nos mesmos dados e, em seguida, executar Jump Search nas listas ordenadas.

## Dados

As entradas estão em arquivos separados, com um inteiro por linha:

- `listas/lista_10k.txt` — 10.000 elementos
- `listas/lista_50k.txt` — 50.000 elementos
- `listas/lista_100k.txt` — 100.000 elementos

Cada algoritmo recebe a lista original e ordena sua própria cópia. O programa confere o resultado antes de medir Jump Search. Para cada ordenação, Jump Search procura o mesmo alvo 100 vezes e registra a média.

## Executar

Rode tudo na ordem 10k, 50k e 100k:

```bash
python benchmark.py
```

Para filmar uma etapa por vez:

```bash
python benchmark.py --lista 10k
python benchmark.py --lista 50k
python benchmark.py --lista 100k
```

A execução completa cria ou substitui `resultados.txt`. Ao executar com `--lista`, o programa acrescenta aquela etapa ao relatório existente, para que você possa filmar e rodar as listas em sequência sem perder os resultados anteriores.

## Testes

```bash
python -m unittest -v
```

Os testes cobrem a busca em salto e verificam se cada ordenação retorna a sequência ordenada correta.

## Interpretação

Jump Search exige uma lista crescente. O tamanho de salto padrão é `⌊√N⌋`; nesse caso, sua complexidade de tempo é `O(√N)` e o espaço adicional é `O(1)`. Insertion Sort e Selection Sort têm tempo `O(N²)` no caso médio/pior, enquanto Merge Sort tem tempo `O(N log N)` e usa espaço adicional `O(N)`. Em especial, as listas de 50 mil e 100 mil elementos podem levar bastante tempo nos algoritmos quadráticos.
