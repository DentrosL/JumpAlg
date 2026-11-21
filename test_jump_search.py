import unittest

from jump_search import jump_search
from sorting_algorithms import insertion_sort, merge_sort, selection_sort

class JumpSearchTests(unittest.TestCase):
    def test_exemplo_da_imagem(self):
        self.assertEqual(jump_search([1, 2, 5, 9, 17, 26, 53, 78, 107], 78), 7)

    def test_lista_vazia_e_alvo_ausente(self):
        self.assertEqual(jump_search([], 1), -1)
        self.assertEqual(jump_search([2, 4, 6], 5), -1)
        self.assertEqual(jump_search([2, 4, 6], 8), -1)

    def test_limites_e_tamanhos_pequenos(self):
        self.assertEqual(jump_search([4], 4), 0)
        self.assertEqual(jump_search([1, 3, 5], 1), 0)
        self.assertEqual(jump_search([1, 3, 5], 5), 2)

    def test_saltos_fixos_e_salto_maior_que_lista(self):
        values = list(range(1, 21))
        for step in (1, 2, 5, 20, 30):
            self.assertEqual(jump_search(values, 17, step), 16)
            self.assertEqual(jump_search(values, 21, step), -1)

    def test_duplicatas(self):
        index = jump_search([1, 2, 2, 2, 4], 2)
        self.assertIn(index, (1, 2, 3))

    def test_tamanho_de_salto_invalido(self):
        with self.assertRaises(ValueError):
            jump_search([1, 2, 3], 2, 0)

class SortingTests(unittest.TestCase):
    def test_todos_ordenam_copia_sem_alterar_entrada(self):
        values = [8, -2, 5, 5, 0, 1]
        expected = [-2, 0, 1, 5, 5, 8]
        for algorithm in (insertion_sort, selection_sort, merge_sort):
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm(values), expected)
                self.assertEqual(values, [8, -2, 5, 5, 0, 1])

    def test_ordenacoes_com_lista_vazia_e_unitaria(self):
        for algorithm in (insertion_sort, selection_sort, merge_sort):
            with self.subTest(algorithm=algorithm.__name__):
                self.assertEqual(algorithm([]), [])
                self.assertEqual(algorithm([4]), [4])

if __name__ == "__main__":
    unittest.main()
