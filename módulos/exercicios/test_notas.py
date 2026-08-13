import unittest

from módulos.exercicios.ex3 import calcular_media, verificar_aprovacao


class TestSistemaNotas(unittest.TestCase):
    def test_aprovacao_e_reprovacao_casos_normais(self):
        media_aprovado = calcular_media([8.0, 7.0, 9.0])
        media_reprovado = calcular_media([4.0, 5.0, 6.0])

        self.assertEqual(verificar_aprovacao(media_aprovado), "Aprovado")
        self.assertEqual(verificar_aprovacao(media_reprovado), "Reprovado")

    def test_calcular_media_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])

    def test_aprovacao_com_media_minima_zero(self):
        media = calcular_media([0.0, 0.0, 0.0])
        self.assertEqual(verificar_aprovacao(media, media_minima=0), "Aprovado")


if __name__ == "__main__":
    unittest.main()
