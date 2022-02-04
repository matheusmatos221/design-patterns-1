# -*- coding: UTF-8 -*-
# orcamento.py

from abc import ABCMeta, abstractmethod


class EstadoDeUmOrcamento(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass


class EmArovacao(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orçamento em aprovação não pode ir para finalizado')


class Aprovado(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)

    def aprova(self, orcamento):
        raise Exception('Orçamento já está aprovado')

    def reprova(self, orcamento):
        raise Exception('Orçamento aprovado não pode ser reprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Reprovado(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orcamentos reprovados não receberam desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orçamento reprovado não pode ser aprovado')

    def reprova(self, orcamento):
        raise Exception('Orçamento já está reprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


class Finalizado(EstadoDeUmOrcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orcamentos finalizados não receberam desconto extra')

    def aprova(self, orcamento):
        raise Exception('Orçamento finalizado não pode ser aprovado')

    def reprova(self, orcamento):
        raise Exception('Orçamento finalizado não pode ser reprovado')

    def finaliza(self, orcamento):
        raise Exception('Orçamento finalizado não pode ser finalizado novamente')


class Orcamento(object):
    def __init__(self):
        self.__itens = []
        self.estado_atual = EmArovacao()
        self.__desconto_extra = 0

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    # quando a propriedade for acessada, ela soma cada item retornando o valor do orçamento
    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    # retornamos uma tupla, já que não faz sentido alterar os itens de um orçamento
    def obter_itens(self):
        return tuple(self.__itens)

    # perguntamos para o orçamento o total de itens
    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)


# um item criado não pode ser alterado, suas propriedades são somente leitura
class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


if __name__ == '__main__':
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM-1', 100))
    orcamento.adiciona_item(Item('ITEM-2', 50))
    orcamento.adiciona_item(Item('ITEM-3', 400))

    print(orcamento.valor)
    orcamento.aprova()
    orcamento.aplica_desconto_extra()
    print(orcamento.valor)
