# -*- coding: UTF-8 -*-
from impostos import ISS, ICMS, ICPP, IKCV


class CalculadorDeImpostos(object):
    def realiza_calculo(self, orcamento, imposto):

        imposto_calculado = imposto.calcula(orcamento)

        print (imposto_calculado)


if __name__ == '__main__':
    print('\n' * 2)
    print('************************************')
    print('Executando calculador_de_impostos.py')
    print('************************************')
    print('\n')

    from orcamento import Orcamento, Item

    calculador = CalculadorDeImpostos()
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM_1', 50))
    orcamento.adiciona_item(Item('ITEM_2', 200))
    orcamento.adiciona_item(Item('ITEM_3', 250))

    print('ISS e ICMS')
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print('ISS com ICMS')
    calculador.realiza_calculo(orcamento, ISS(ICMS()))

    print('ICPP e IKCV')
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())

    print('ICPP com IKCV')
    calculador.realiza_calculo(orcamento, ICPP(IKCV()))
