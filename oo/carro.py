
"""
EXERCICIO

Voce deve criar uma classe de carro que vai possuir
dois atributos compostos por outras duas classes


1) Motor
2) Direção

o motor terá a responsabilodade de controlar a velocidade
ele oferece os seguintes atributos:
1)atributo de dado velocidade
2)metodo acelerar , que deverá incrementar a velocidade de uma unidade
3)metodo frear que devera decrementar a velocidade em duas unidades


a direçai terá a responsabilidade de controlar a direçao . ela oferece os seguintes atributos :
1)valor de direçao com valores possiveis :norte ,sul, leste ,oeste.
2)metodo girar_a_direita
3)métudo girar_a_esquerda
   N
O     L
   S

    Exemplo:
    >>> motor = motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar ()
    >>> motor.velocidade
    1
    >>> motor.acelerar ()
    >>> motor.velocidade
    2
    >>> motor.acelerar ()
    >>> motor.velocidade
    3
    >>> motor.frear ()
    >>> motor.velocidade
    1
    >>> motor.frear ()
    >>> motor.velocidade
    0
    >>> # Testando Dirção
    >>> direcao = Direcao
    >>> direcao.valor
    'NORTE'
     >>> direcao.girar_a_direita ()
     >>> direcao.valor
    'LESTE'
     >>> direcao.girar_a_direita ()
     >>> direcao.valor
     'SUL'
     >>> direcao.girar_a_direita ()
     >>> direcao.valor
     'OESTE'
     >>> direcao.girar_a_direita ()
     >>> direcao.valor
     'NORTE'
     >>> direcao.girar_a_esquerda ()
     >>> direcao.valor
     'OESTE'
     >>> direcao.girar_a_esquerda ()
     >>> direcao.valor
     'SUL'
     >>> direcao.girar_a_esquerda ()
     >>> direcao.valor
     'LESTE'
     >>> direcao.girar_a_esquerda ()
     >>> direcao.valor
     'NORTE'
     >>> carro = Carro(direcao, motor)
     >>> carro.calcular_velocidade()
     0
     >>> carro.acelerar()
     >>> carro.calcular_velocidade()
     1
     >>> carro.acelerar()
     >>> carro.calcular_velocidade()
     2
     >>> carro.frear()
     >>> carro.calcular_velocidade()
     0
     >>> carro.calcular_direcao ()
     >>> 'NORTE'
     >>> carro.girar_a_direita()
     >>> carro.calcular_direcao()
    'Leste'
     >>> carro.girar_a_esquerda()
     >>> carro.calcular_direcao()
    'Norte'
     >>> carro.girar_a_esquerda()
     >>> carro.calcular_direcao()
    'Oeste'









"""