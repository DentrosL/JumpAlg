"""Busca em salto para sequências ordenadas em ordem crescente."""

from math import isqrt
from typing import Sequence, TypeVar

T = TypeVar("T")

def jump_search(values: Sequence[T], target: T, jump_size: int | None = None) -> int:
    """Retorna o índice de ``target`` ou -1 se não estiver em ``values``.

    A sequência deve estar ordenada em ordem crescente. Por padrão, usa um
    salto de tamanho floor(sqrt(n)); ``jump_size`` permite experimentar
    tamanhos fixos no benchmark. Em caso de duplicatas, retorna uma ocorrência.
    """
    n = len(values)
    if n == 0:
        return -1
    if jump_size is None:
        jump_size = max(1, isqrt(n))
    elif jump_size <= 0:
        raise ValueError("jump_size deve ser maior que zero")

    start = 0
    end = min(jump_size, n)

    # Avança por blocos até encontrar o bloco que pode conter o alvo.
    while values[end - 1] < target:
        start = end
        if start >= n:
            return -1
        end = min(end + jump_size, n)

    # Procura sequencialmente apenas dentro do bloco candidato.
    for index in range(start, end):
        if values[index] == target:
            return index
        if values[index] > target:
            return -1
    return -1

if __name__ == "__main__":
    exemplo = [1, 2, 5, 9, 17, 26, 53, 78, 107]
    procurado = 78
    print(f"Índice de {procurado}: {jump_search(exemplo, procurado)}")
