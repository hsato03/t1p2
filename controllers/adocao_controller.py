from views import AdocaoView
from model import Adocao, Cachorro, TIPO_CACHORRO, TIPO_CPF
from exceptions import EntidadeNaoEncontradaException, OpcaoInvalidaException
from datetime import date


class AdocaoController:
    def __init__(self, controlador_sistema):
        self.__adocoes = []
        self.__tela_adocao = AdocaoView()
        self.__controlador_sistema = controlador_sistema

    def buscar_adocao_por_identificador(self, identificador, tipo_id: int):
        for adocao in self.__adocoes:
            if tipo_id == TIPO_CPF:
                if adocao.adotante.cpf == identificador:
                    return adocao
            else:
                if adocao.animal.numero_chip == int(identificador):
                    return adocao
        raise EntidadeNaoEncontradaException("ERRO: Adocao nao existente.")

    def incluir_adocao(self):
        tipo_animal = self.__tela_adocao.telar_opcoes_tipo_animal()
        dados_adocao = self.__tela_adocao.pegar_dados_adocao()

        cpf_adotante = dados_adocao["cpf_adotante"]

        numero_chip = dados_adocao["numero_chip"]
        if tipo_animal == TIPO_CACHORRO:
            animal = self.__controlador_sistema.controlador_animais.buscar_cachorro_por_numero_chip(
                numero_chip
            )
        else:
            animal = self.__controlador_sistema.controlador_animais.buscar_gato_por_numero_chip(
                numero_chip
            )

        adotante = (
            self.__controlador_sistema.controlador_adotantes.buscar_adotante_por_cpf(
                cpf_adotante
            )
        )

        adocao = Adocao(
            adotante,
            animal,
            dados_adocao["data"],
            True if dados_adocao["termo_assinado"] == 1 else False,
        )
        self.__adocoes.append(adocao)

    def alterar_adocao(self):
        if self.verificar_nenhuma_adocao_cadastrada():
            return

        self.listar_adocoes()

        tipo_id = self.get_tipo_id()

        identificador = self.__tela_adocao.selecionar_adocao(tipo_id)
        adocao = self.buscar_adocao_por_identificador(identificador, tipo_id)
        novos_dados_adocao = self.__tela_adocao.pegar_dados_adocao()

        cpf_adotante = novos_dados_adocao["cpf_adotante"]
        adotante = (
            self.__controlador_sistema.controlador_adotantes.buscar_adotante_por_cpf(
                cpf_adotante
            )
        )

        numero_chip = novos_dados_adocao["numero_chip"]

        if isinstance(adocao.animal, Cachorro):
            animal = self.__controlador_sistema.controlador_animais.buscar_cachorro_por_numero_chip(
                numero_chip
            )
        else:
            animal = self.__controlador_sistema.controlador_animais.buscar_gato_por_numero_chip(
                numero_chip
            )

        adocao.adotante = adotante
        adocao.animal = animal
        adocao.data = novos_dados_adocao["data"]
        adocao.termo_assinado = novos_dados_adocao["termo_assinado"]

    def listar_adocoes(self):
        if self.verificar_nenhuma_adocao_cadastrada():
            return

        for i in range(len(self.__adocoes)):
            self.__tela_adocao.mostrar_mensagem(f"ADOCAO #{i + 1:02d}")
            adocao = self.__adocoes[i]
            self.__tela_adocao.mostrar_adocao(
                {
                    "cpf_adotante": adocao.adotante.cpf,
                    "numero_chip": adocao.animal.numero_chip,
                    "data": adocao.data,
                    "termo_assinado": adocao.termo_assinado,
                }
            )

    def excluir_adocao(self):
        if self.verificar_nenhuma_adocao_cadastrada():
            return

        self.listar_adocoes()

        tipo_id = self.get_tipo_id()

        identificador = self.__tela_adocao.selecionar_adocao(tipo_id)
        adocao = self.buscar_adocao_por_identificador(identificador, tipo_id)
        self.__adocoes.remove(adocao)
        self.__tela_adocao.mostrar_mensagem("Adocao removida com sucesso.")

    def listar_adocao_por_identificador(self):
        if self.verificar_nenhuma_adocao_cadastrada():
            return

        while True:
            try:
                tipo_id = self.__tela_adocao.telar_opcoes_identificador()
                break
            except OpcaoInvalidaException as e:
                self.__tela_adocao.mostrar_mensagem(e)
            except ValueError:
                self.__tela_adocao.mostrar_mensagem("Somente numeros. Tente novamente.")

        identificador = self.__tela_adocao.selecionar_adocao(tipo_id)

        adocao = self.buscar_adocao_por_identificador(identificador, tipo_id)

        self.__tela_adocao.mostrar_adocao(
            {
                "cpf_adotante": adocao.adotante.cpf,
                "numero_chip": adocao.animal.numero_chip,
                "data": adocao.data,
                "termo_assinado": True if adocao.termo_assinado == 1 else False,
            }
        )

    def verificar_nenhuma_adocao_cadastrada(self):
        if len(self.__adocoes) <= 0:
            self.__tela_adocao.mostrar_mensagem("Nenhuma adocao cadastrada.")
            return True

    def get_tipo_id(self):
        while True:
            try:
                tipo_id = self.__tela_adocao.telar_opcoes_identificador()
                return tipo_id
            except OpcaoInvalidaException as e:
                self.__tela_adocao.mostrar_mensagem(e)
            except ValueError:
                self.__tela_adocao.mostrar_mensagem("Somente numeros. Tente novamente.")

    def retornar(self):
        self.__controlador_sistema.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {
            1: self.incluir_adocao,
            2: self.alterar_adocao,
            3: self.listar_adocoes,
            4: self.excluir_adocao,
            5: self.listar_adocao_por_identificador,
            0: self.retornar,
        }

        while True:
            try:
                lista_opcoes[self.__tela_adocao.telar_opcoes()]()
            except (OpcaoInvalidaException, EntidadeNaoEncontradaException) as e:
                self.__tela_adocao.mostrar_mensagem(e)
            except ValueError:
                self.__tela_adocao.mostrar_mensagem("Somente numeros. Tente novamente")
