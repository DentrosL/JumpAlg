"""Implementações didáticas dos três algoritmos de ordenação do trabalho."""

def insertion_sort(values):
    result = values.copy()
    for index in range(1, len(result)):
        current = result[index]
        position = index - 1
        while position >= 0 and result[position] > current:
            result[position + 1] = result[position]
            position -= 1
        result[position + 1] = current
    return result

def selection_sort(values):
    result = values.copy()
    for index in range(len(result) - 1):
        smallest = index
        for candidate in range(index + 1, len(result)):
            if result[candidate] < result[smallest]:
                smallest = candidate
        result[index], result[smallest] = result[smallest], result[index]
    return result

def merge_sort(values):
    if len(values) < 2:
        return values.copy()
    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    merged = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged
