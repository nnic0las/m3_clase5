import sys
import os

#fijar ruta directa a la logica del negocio (negocio.py y __init__.py)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

#importamos el archivo .py y sus funciones 
from negocio import VendedorBase, VendedorPremium

import pytest

def test_calcyular_comicion_base():
    vendedor = VendedorBase("pedro", 1000)
    assert VendedorBase.clacular_comision() == 100.0

def test_calcular_comicion_premium():
    vendedor = VendedorPremium("maria", 2000)
    assert VendedorPremium.clacular_comision() == 300.0

