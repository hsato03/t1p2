from views.adocao_view import AdocaoView
from model.adocao import Adocao
from exceptions.entidade_nao_encontrada_exception import EntidadeNaoEncontradaException
from datetime import date


class AdocaoController:
    def __init__(self, controlador_principal):
        self.__adocoes = []
        self.__tela_adocao = AdocaoView()
        self.__controlador_principal = controlador_principal

    def buscar_adocao_por_identificador(self, identificador: str):
        for adocao in self.__adocoes:
            if adocao.adotante.cpf == identificador:
                return adocao
            elif adocao.animal.numero_chip == identificador:
                return adocao
        raise EntidadeNaoEncontradaException("ERRO: Adocao nao existente.")

    def incluir_adocao(self):
        dados_adotante = self.__tela_adocao.pega_dados_adocao()
        adotante = None
        try:
            cpf_adotante = dados_adotante["cpf_adotante"]
            adotante = self.__controlador_principal.controlador_adotantes.buscar_adotante_por_cpf(cpf_adotante)
            numero_chip = dados_adotante["numero_chip"]
            animal = self.__controlador_principal.buscar_animal_por_numero_chip(numero_chip)
        except EntidadeNaoEncontradaException as e:
            print(e)

        adocao = Adocao(
            adotante,
            animal,
            date.today(),
            True if dados_adotante["termo_assinado"] == 1 else False
        )
        self.__adocoes.append(adocao)

    def alterar_adocao(self):
        if len(self.__adocoes) <= 0:
            self.__tela_adocao.mostra_mensagem("Nenhuma adocao cadastrada.")
            return
        
        try:
            id = self.__tela_adocao.seleciona_adocao()
            adocao = self.buscar_adocao_por_identificador(id)
            novos_dados_adocao = self.__tela_adocao.pega_dados_adocao()

            cpf_adotante = novos_dados_adocao["cpf_adotante"]
            adotante = self.__controlador_principal.controlador_adotantes.buscar_adotante_por_cpf(cpf_adotante)

            numero_chip = novos_dados_adocao["numero_chip"]
            animal = self.__controlador_principal.buscar_animal_por_numero_chip(numero_chip)

            adocao.adotante = adotante
            adocao.animal = animal
            adocao.data = novos_dados_adocao["data"]
            adocao.termo_assinado = novos_dados_adocao["termo_assinado"]
        except EntidadeNaoEncontradaException as e:
            print(e)

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
                    "numero_chip": adocao.animal.numero_chip,
                    "data": adocao.data,
                    "termo_assinado": adocao.termo_assinado
                }
            )

    def excluir_adocao(self):
        if len(self.__adocoes) <= 0:
            print("Nenhuma adocao cadastrada.")
            return
        
        self.listar_adocoes()
        id = self.__tela_adocao.seleciona_adocao()

        try:
            adocao = self.buscar_adocao_por_identificador(id)
            self.__adocoes.remove(adocao)
            self.__tela_adocao.mostra_mensagem("Adocao removida com sucesso.")
        except EntidadeNaoEncontradaException as e:
            print(e)

    def listar_adocao_por_identificador(self):
        if len(self.__adocoes) <= 0:
            self.__tela_adocao.mostra_mensagem("Nenhuma adocao cadastrada.")
            return

        id = self.__tela_adocao.seleciona_adocao()
        try:
            adocao = self.buscar_adocao_por_identificador(id)

            self.__tela_adocao.mostra_adocao({
                "cpf_adotante": adocao.adotante.cpf,
                "numero_chip": adocao.animal.numero_chip,
                "data": adocao.data,
                "termo_assinado": adocao.termo_assinado
            })
        except EntidadeNaoEncontradaException as e:
            print(e)


    def retornar(self):
        self.__controlador_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_adocao,
            2: self.alterar_adocao,
            3: self.excluir_adocao,
            4: self.listar_adocoes,
            5: self.listar_adocao_por_identificador,
            0: self.retornar,
        }

        while True:
            lista_opcoes[self.__tela_adocao.tela_opcoes()]()
