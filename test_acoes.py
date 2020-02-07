import unittest
from acoes import lucro_acao

class AcoesTest(unittest.TestCase):
    def test_retorna_o_valor_correto_com_valores_apos_o_minimo(self):
        resultado = lucro_acao([7,1,5,3,6,4])
        self.assertEqual(5, resultado)

    def test_retorna_0_quando_nao_existe_valores_apos_o_minimo(self):
        resultado = lucro_acao([7,6,4,3,1])
        self.assertEqual(0, resultado)
        