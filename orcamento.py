# -*- coding: UTF-8 -*-
# orcamento.py
class Orcamento(object):

    EM_APROVACAO = 1
    APROVADO = 2
    REPROVADO = 3
    FINALIZADO = 4

    def __init__(self):
        self.__itens = []
        self.estado_atual = Orcamento.EM_APROVACAO
        self.__desconto_extra = 0

    def aplica_desconto_extra(self):
        if self.estado_atual == Orcamento.EM_APROVACAO:
            self.__desconto_extra += self.valor * 0.02
        elif self.estado_atual == Orcamento.APROVADO:
            self.__desconto_extra += self.valor * 0.05
        elif self.estado_atual == Orcamento.REPROVADO:
            raise Exception('Orcamentos reprovados não receberam desconto extra')
        elif self.estado_atual == Orcamento.FINALIZADO:
            raise Exception('Orcamentos finalizados não receberam desconto extra')

    # quando a propriedade for acessada, ela soma cada item retornando o valor do orçamento
    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total

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