# morgana.github.io
from manequim import *

def getNome():
    print('Olá EMPODERADA!')
    nome = input('Qual o seu nome? ')
    print('É um grande prazer conhecê-la %s!' % nome)

def getMedidas():
    ombro, busto, cintura, quadril = 0, 0,0,0

    ombro = float(input('Qual o tamanho do seu ombro, em cm? '))
    busto = float(input('E o seu busto? '))
    cintura = float(input('Sua cintura? '))
    quadril = float(input('Seu quadril? '))

    print('Legal, deixa ver se eu entendi!')
    print(f'%.1fcm de ombro, %.1fcm de busto, %.1fcm de cintura, %.1fcm de quadril.' % (ombro, busto, cintura, quadril))

    return (ombro, busto, cintura, quadril)

def getMedidaOmbro(obj, medida=MedidaOmbro):
    manequim = obj.buscaMedidasOmbro(medida)
    return manequim

def getMedidaBusto(obj, medida:Medida):
    manequim = obj.buscaMedidasCorpo(0, medida)
    return manequim

def getMedidaQuadril(obj, medida:Medida):
    manequim = obj.buscaMedidasCorpo(1, medida)
    return manequim


medidaBR = PadraoMedidaBR()
blazers = TipoRoupaOmbro.list()
blusas = TipoRoupaBusto.list()
calcas = TipoRoupaQuadril.list()
tipo = 0
tipos = [1,2,3]
msgTipos = [
    'Digite:',
    f'  [ 1 ] para: %s' % ', '.join(blazers),
    f'  [ 2 ] para: %s' % ', '.join(blusas),
    f'  [ 3 ] para %s' % ', '.join(calcas)
]

getNome()

while tipo not in tipos:
    print("\n".join(msgTipos), "\n")
    tipo = input('Tipo de roupa: ')
    if not tipo.isnumeric():
        tipo = 0
    else:
        tipo = int(tipo)

ombro, busto, cintura, quadril = getMedidas()
ok = input('Correto? ')


if tipo == 1:
    m = MedidaOmbro(ombro=ombro)
    manequim = getMedidaOmbro(medidaBR, m)
else:
    m = Medida(busto=busto, cintura=cintura, quadril=quadril)
    if tipo == 2:
        manequim = getMedidaBusto(medidaBR, m)
    elif tipo == 3:
        manequim = getMedidaQuadril(medidaBR, m)

print(f'Seu manequim é: %d' % manequim)
