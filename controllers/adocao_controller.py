from views.adocao_view import AdocaoView
from model.adocao import Adocao
from exceptions.entidade_nao_encontrada_exception import EntidadeNaoEncontradaException
from exceptions.opcao_invalida_exception import OpcaoInvalidaException
from datetime import date


class AdocaoController:
    def __init__(self, controlador_principal):
        self.__adocoes = []
        self.__tela_adocao = AdocaoView()
        self.__controlador_principal = controlador_principal

    def buscar_adocao_por_identificador(self, identificador: str, tipo_id: int):
        for adocao in self.__adocoes:
            if tipo_id == 1:
                if adocao.adotante.cpf == identificador:
                    return adocao
            else:
                if adocao.animal.numero_chip == identificador:
                    return adocao
        raise EntidadeNaoEncontradaException("ERRO: Adocao nao existente.")

    def incluir_adocao(self):
        dados_adotante = self.__tela_adocao.pega_dados_adocao()
        adotante = None
        animal = None
        try:
            cpf_adotante = dados_adotante["cpf_adotante"]
            adotante = self.__controlador_principal.controlador_adotantes.buscar_adotante_por_cpf(
                cpf_adotante
            )
            numero_chip = dados_adotante["numero_chip"]
            animal = self.__controlador_principal.controlador_animais.buscar_animal_por_numero_chip(
                numero_chip
            )
        except EntidadeNaoEncontradaException as e:
            self.__tela_adocao.mostra_mensagem(e)

        adocao = Adocao(
            adotante,
            animal,
            date.today(),
            True if dados_adotante["termo_assinado"] == 1 else False,
        )
        self.__adocoes.append(adocao)

    def alterar_adocao(self):
        if len(self.__adocoes) <= 0:
            self.__tela_adocao.mostra_mensagem("Nenhuma adocao cadastrada.")
            return

        try:
            while True:
                try:
                    tipo_id = self.__tela_adocao.tela_opcoes_identificador()
                    break
                except OpcaoInvalidaException as e:
                    self.__tela_adocao.mostra_mensagem(e)
                except ValueError:
                    self.__tela_adocao.mostra_mensagem(
                        "Somente numeros. Tente novamente."
                    )

            id = self.__tela_adocao.seleciona_adocao(tipo_id)
            adocao = self.buscar_adocao_por_identificador(id, tipo_id)
            novos_dados_adocao = self.__tela_adocao.pega_dados_adocao()

            cpf_adotante = novos_dados_adocao["cpf_adotante"]
            adotante = self.__controlador_principal.controlador_adotantes.buscar_adotante_por_cpf(
                cpf_adotante
            )

            numero_chip = novos_dados_adocao["numero_chip"]
            animal = self.__controlador_principal.controlador_animais.buscar_animal_por_numero_chip(
                numero_chip
            )

            adocao.adotante = adotante
            adocao.animal = animal
            adocao.data = novos_dados_adocao["data"]
            adocao.termo_assinado = novos_dados_adocao["termo_assinado"]
        except EntidadeNaoEncontradaException as e:
            self.__tela_adocao.mostra_mensagem(e)

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
                    "termo_assinado": adocao.termo_assinado,
                }
            )

    def excluir_adocao(self):
        if len(self.__adocoes) <= 0:
            self.__tela_adocao.mostra_mensagem("Nenhuma adocao cadastrada.")
            return

        self.listar_adocoes()

        while True:
            try:
                tipo_id = self.__tela_adocao.tela_opcoes_identificador()
                break
            except OpcaoInvalidaException as e:
                self.__tela_adocao.mostra_mensagem(e)
            except ValueError:
                self.__tela_adocao.mostra_mensagem("Somente numeros. Tente novamente.")

        id = self.__tela_adocao.seleciona_adocao(tipo_id)

        try:
            adocao = self.buscar_adocao_por_identificador(id, tipo_id)
            self.__adocoes.remove(adocao)
            self.__tela_adocao.mostra_mensagem("Adocao removida com sucesso.")
        except EntidadeNaoEncontradaException as e:
            self.__tela_adocao.mostra_mensagem(e)

    def listar_adocao_por_identificador(self):
        if len(self.__adocoes) <= 0:
            self.__tela_adocao.mostra_mensagem("Nenhuma adocao cadastrada.")
            return

        while True:
            try:
                tipo_id = self.__tela_adocao.tela_opcoes_identificador()
                break
            except OpcaoInvalidaException as e:
                self.__tela_adocao.mostra_mensagem(e)
            except ValueError:
                self.__tela_adocao.mostra_mensagem("Somente numeros. Tente novamente.")

        id = self.__tela_adocao.seleciona_adocao(tipo_id)
        try:
            adocao = self.buscar_adocao_por_identificador(id, tipo_id)

            self.__tela_adocao.mostra_adocao(
                {
                    "cpf_adotante": adocao.adotante.cpf,
                    "numero_chip": adocao.animal.numero_chip,
                    "data": adocao.data,
                    "termo_assinado": True if adocao.termo_assinado == 1 else False,
                }
            )
        except EntidadeNaoEncontradaException as e:
            self.__tela_adocao.mostra_mensagem(e)

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
            try:
                lista_opcoes[self.__tela_adocao.tela_opcoes()]()
            except OpcaoInvalidaException as e:
                self.__tela_adocao.mostra_mensagem(e)
            except ValueError:
                self.__tela_adocao.mostra_mensagem("Somente numeros. Tente novamente")
