from impostos import ISS, ICMS


class CalculadorDeImpostos(object):
    def realiza_calculo(self, orcamento, imposto):

        imposto_calculado = imposto(orcamento)
        print (imposto_calculado)


if __name__ == '__main__':
    print('\n' * 2)
    print('************************************')
    print('Executando calculador_de_impostos.py')
    print('************************************')
    print('\n')

    from orcamento import Orcamento

    calculador = CalculadorDeImpostos()
    orcamento = Orcamento(500)

    calculador.realiza_calculo(orcamento, ISS().calcula_ISS())
    calculador.realiza_calculo(orcamento, ICMS().calcula_ICMS())
