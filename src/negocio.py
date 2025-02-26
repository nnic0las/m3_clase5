from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Vendedor(ABC):
    nombre: str
    ventas: float

    @abstractmethod
    def clacular_comision(self) -> float:
        pass

@dataclass
class VendedorBase(Vendedor):

    def clacular_comision(self)-> float:
        return self.ventas * 0.10
    
@dataclass
class VendedorPremium(Vendedor):

    def clacular_comision(self) -> float:
        return self.ventas * 0.15


