"""Executa as ordenações e a busca em cada arquivo de dados, em sequência."""

import argparse
import statistics
import time
from pathlib import Path

from jump_search import jump_search
from sorting_algorithms import insertion_sort, merge_sort, selection_sort

ROOT = Path(__file__).parent
DATASETS = [ROOT / "listas" / "lista_10k.txt", ROOT / "listas" / "lista_50k.txt", ROOT / "listas" / "lista_100k.txt"]
SORTS = [
    ("Insertion Sort", insertion_sort),
    ("Selection Sort", selection_sort),
    ("Merge Sort", merge_sort),
]

def carregar_lista(path):
    with path.open(encoding="utf-8") as file:
        return [int(line) for line in file if line.strip()]

def formatar_tempo(seconds):
    if seconds < 1:
        return f"{seconds * 1000:,.3f} ms"
    return f"{seconds:,.3f} s"

def executar_dataset(path, report):
    values = carregar_lista(path)
    if not values:
        raise ValueError(f"A lista está vazia: {path}")
    target = values[len(values) // 2]
    lines = [
        "\n" + "=" * 64,
        f"  {path.name}  |  {len(values):,} elementos",
        "=" * 64,
    ]
    ordered_results = {}

    for name, algorithm in SORTS:
        print(f"  Executando {name}...", flush=True)
        start = time.perf_counter()
        ordered = algorithm(values)
        elapsed = time.perf_counter() - start
        if ordered != sorted(values):
            raise AssertionError(f"{name} produziu uma ordenação incorreta")
        ordered_results[name] = ordered
        lines.append(f"  {name:<18} {formatar_tempo(elapsed):>14}   lista ordenada: OK")

    lines.append(f"\n  Jump Search | alvo: {target:,} | salto: piso(raiz de N)")
    search_samples = []
    for name, ordered in ordered_results.items():
        samples = []
        for _ in range(100):
            start = time.perf_counter()
            found_index = jump_search(ordered, target)
            samples.append(time.perf_counter() - start)
            if found_index < 0 or ordered[found_index] != target:
                raise AssertionError(f"Jump Search falhou após {name}")
        average = statistics.mean(samples)
        search_samples.append(average)
        lines.append(f"  Após {name:<14} média de 100 buscas: {formatar_tempo(average)}")

    lines.extend([
        "\n  Checagem: as três ordenações e buscas foram concluídas.",
        "=" * 64,
    ])
    block = "\n".join(lines)
    print(block, flush=True)
    with report.open("a", encoding="utf-8") as file:
        file.write(block + "\n")
    return len(values)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lista", choices=("10k", "50k", "100k"), help="executa só uma lista")
    parser.add_argument("--saida", type=Path, default=ROOT / "resultados.txt", help="arquivo de relatório legível")
    args = parser.parse_args()

    selected = [path for path in DATASETS if args.lista is None or args.lista in path.name]
    missing = [path for path in selected if not path.exists()]
    if missing:
        parser.error("Arquivos de dados ausentes: " + ", ".join(str(path) for path in missing))

    if args.lista is None or not args.saida.exists():
        args.saida.write_text("RESULTADOS — ORDENACAO E JUMP SEARCH\n", encoding="utf-8")
    with args.saida.open("a", encoding="utf-8") as file:
        file.write("\nRodada: " + time.strftime("%d/%m/%Y %H:%M:%S") + "\n")
    print("\n  EXPERIMENTO DE ALGORITMOS", flush=True)
    print("  Insertion  |  Selection  |  Merge  |  Jump Search", flush=True)
    print(f"  Relatório: {args.saida}\n", flush=True)

    for path in selected:
        executar_dataset(path, args.saida)

    print(f"\n  Experimento concluído. Resultados em: {args.saida}\n", flush=True)

if __name__ == "__main__":
    main()
