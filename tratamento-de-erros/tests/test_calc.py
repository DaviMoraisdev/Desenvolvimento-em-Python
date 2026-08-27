import sys
from pathlib import Path

PASTA_DO_MODULO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PASTA_DO_MODULO))

from testes import dobro, raiz_quadrada


def test_dobro():
    assert dobro(5) == 10
    assert dobro(0) == 0
    assert dobro(-3) == -6


def test_raiz_quadrada():
    assert raiz_quadrada(16) == 4
    assert raiz_quadrada(1) == 1
