from dataclasses import dataclass
from enum import Enum

# print(enum.list())
class EnumExt(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.name, cls))


class TipoRoupaOmbro(EnumExt):
    BLAZER = 0

class TipoRoupaBusto(EnumExt):
    TOP = 0
    BLUSA = 1
    CAMISA = 2
    MACACAO = 3
    TUBINHO = 4

class TipoRoupaQuadril(EnumExt):
    SHORT = 0
    CALCA = 1
    SAIA = 2

@dataclass
class Medida:
    busto: float
    cintura: float
    quadril: float

@dataclass
class MedidaOmbro:
    ombro: float


class PadraoMedidaBR:
    def __init__(self):
        self.limites = {
            'PP36': (36, Medida(79, 61, 85)),
            'P38': (38, Medida(82, 64, 88)),
            'P40': (40, Medida(86, 68, 92)),
            'M42': (42, Medida(90, 72, 96)),
            'M44': (44, Medida(94, 76, 100)),
            'M46': (46, Medida(98, 80, 104)),
            'M48': (48, Medida(104, 86, 110)),
            'GG50': (50, Medida(110, 92, 116)),
            'GG52': (52, Medida(116, 98, 122)),
            'XGG54': (54, Medida(122, 104, 128)),
            'XGG56': (56, Medida(128, 110, 134)),
        }
        self.ombros = {
            'PP38': (38, MedidaOmbro(40.4)),
            'P40': (40, MedidaOmbro(42.4)),
            'M42': (42, MedidaOmbro(44.4)),
            'G44': (44, MedidaOmbro(46.4)),
            'GG46': (46, MedidaOmbro(48.4)),
        }

    def buscaMedidasCorpo(self, tipo:int, medida:Medida):
        res = ''
        manequim = 56
        for padrao in list(self.limites):
            limites = self.limites[padrao][1]
            if(tipo == 0):
                if medida.busto <= limites.busto:
                    res = padrao
                    break
            if(tipo == 1):
                if medida.quadril <= limites.quadril:
                    res = padrao
                    break
        if not res == '':
            manequim = self.limites[res][0]
        return manequim

    def buscaMedidasOmbro(self, medida:MedidaOmbro):
        res = ''
        manequim = 46
        for padrao in list(self.ombros):
            limites = self.ombros[padrao][1]
            if medida.ombro <= limites.ombro:
                res = padrao
                break
        if not res == '':
            manequim = self.ombros[res][0]
        return manequim

