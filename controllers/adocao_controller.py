from views.adocao_view import AdocaoView
from model.adocao import Adocao
from exceptions.entidade_nao_encontrada_exception import EntidadeNaoEncontradaException
from datetime import date


class AdocaoController:
    def __init__(self, controlador_principal):
        self.__adocoes = []
        self.__tela_adocao = AdocaoView()
        self.__controlador_principal = controlador_principal

    def buscar_adocao_por_identificador(self, identificador: int):
        for adocao in self.__adocoes:
            if adocao.adotante.cpf == identificador:
                return adocao
            elif adocao.animal.numero_chip == identificador:
                return adocao
        return None

    def incluir_adocao(self):
        dados_adotante = self.__tela_adocao.pega_dados_adocao()
        adotante = None
        try:
            cpf_adotante = dados_adotante["cpf_adotante"]
            adotante = self.__controlador_principal.controlador_adotantes.buscar_adotante_por_cpf(cpf_adotante)
        except EntidadeNaoEncontradaException as e:
            print(e)

        adocao = Adocao(
            adotante,
            None,
            date.today(),
            True if dados_adotante["termo_assinado"] == 1 else False
        )
        self.__adocoes.append(adocao)

    def alterar_adocao(self):
        pass

    def listar_adocoes(self):
        if len(self.__adocoes) <= 0:
            self.__tela_adocao.mostra_mensagem("Nenhuma adocao cadastrada.")
            return

        for i in range(len(self.__adocoes)):
            self.__tela_adocao.mostra_mensagem(f"ADOCAO #{i + 1:02d}")
            adocao = self.__adocoes[i]
            self.__tela_adocao.mostra_adocao(
                {
                    "cpf_adotante": adocao.adotante.cpf,
                    "numero_chip": None,#adocao.animal.numero_chip,
                    "data": adocao.data,
                    "termo_assinado": adocao.termo_assinado
                }
            )

    def excluir_adocao(self):
        pass

    def listar_adocao_por_identificador(self):
        pass

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_adocao,
            2: self.alterar_adocao,
            3: self.listar_adocoes,
            4: self.excluir_adocao,
            5: self.listar_adocao_por_identificador,
            0: self.retornar,
        }

        while True:
            lista_opcoes[self.__tela_adocao.tela_opcoes()]()
