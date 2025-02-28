import sys
import os

#fijar ruta directa a la logica del negocio (negocio.py y __init__.py)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from negocio import VendedorBase, VendedorPremium 
import unittest

class TestVendedor(unittest.TestCase):
    def setUp(self):
        self.Vendedor_base = VendedorBase("luis", 1000) #comision = 100.0
        self.Vendedor_premium = VendedorPremium("carlos", 2000) #comision = 300.0

    def test_calcular_comision_base(self):
        self.assertEqual(self.Vendedor_base.clacular_comision(), 100.0)

    def test_calcular_comision_premium(self):
        self.assertEqual(self.Vendedor_premium.clacular_comision(), 300.0)

if __name__ == '__main__':
    unittest.main() 
