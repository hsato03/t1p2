from views import AnimalView
from model import Cachorro, TamanhoCachorro, Gato, TIPO_CACHORRO, TIPO_GATO
from exceptions import EntidadeNaoEncontradaException, OpcaoInvalidaException


class AnimalController:
    def __init__(self, controlador_sistema):
        self.__gatos = []
        self.__cachorros = []
        self.__controlador_principal = controlador_sistema
        self.__tela_animal = AnimalView()

    def buscar_gato_por_numero_chip(self, numero_chip: str):
        for gato in self.__gatos:
            if gato.numero_chip == numero_chip:
                return gato
        raise EntidadeNaoEncontradaException("ERRO: Gato nao existente")

    def buscar_cachorro_por_numero_chip(self, numero_chip: str):
        for cachorro in self.__cachorros:
            if cachorro.numero_chip == numero_chip:
                return cachorro
        raise EntidadeNaoEncontradaException("ERRO: Cachorro nao existente")

    def incluir_animal(self):
        dados_animal = self.__tela_animal.pega_dados_animal()

        if dados_animal["tipo_animal"] == TIPO_CACHORRO:
            cachorro = Cachorro(
                dados_animal["numero_chip"],
                dados_animal["nome"],
                dados_animal["raca"],
                TamanhoCachorro(dados_animal["tamanho_cachorro"]),
            )
            self.__cachorros.append(cachorro)
        else:
            gato = Gato(
                dados_animal["numero_chip"],
                dados_animal["nome"],
                dados_animal["raca"],
            )
            self.__gatos.append(gato)

    def listar_animais(self):
        tipo_animal = self.__tela_animal.tela_opcoes_tipo_animal()

        if tipo_animal == TIPO_CACHORRO:
            self.listar_cachorros()

        else:
            self.listar_gatos()

    def listar_cachorros(self):
        if self.verifica_nenhum_cachorro_cadastrado():
            return

        for i in range(len(self.__cachorros)):
            cachorro = self.__cachorros[i]
            self.__tela_animal.mostra_mensagem(f"CACHORRO #{i + 1:02d}")
            self.__tela_animal.mostra_animal(
                {
                    "numero_chip": cachorro.numero_chip,
                    "nome": cachorro.nome,
                    "raca": cachorro.raca,
                    "tamanho_cachorro": cachorro.tamanho,
                    "tipo_animal": TIPO_CACHORRO,
                }
            )

    def listar_gatos(self):
        if self.verifica_nenhum_gato_cadastrado():
            return

        for i in range(len(self.__gatos)):
            gato = self.__gatos[i]
            self.__tela_animal.mostra_mensagem(f"GATO #{i + 1:02d}")
            self.__tela_animal.mostra_animal(
                {
                    "numero_chip": gato.numero_chip,
                    "nome": gato.nome,
                    "raca": gato.raca,
                    "tipo_animal": TIPO_GATO,
                }
            )

    def alterar_animal(self):
        tipo_animal = self.__tela_animal.tela_opcoes_tipo_animal()
        self.listar_cachorros() if tipo_animal == TIPO_CACHORRO else self.listar_gatos()
        numero_chip = self.__tela_animal.seleciona_animal()

        if tipo_animal == TIPO_CACHORRO:
            if self.verifica_nenhum_cachorro_cadastrado():
                return

            self.alterar_cachorro(numero_chip)
        else:
            if self.verifica_nenhum_gato_cadastrado():
                return

            self.alterar_gato(numero_chip)

    def alterar_cachorro(self, numero_chip: str):
        cachorro = self.buscar_cachorro_por_numero_chip(numero_chip)
        dados_novos_cachorro = self.__tela_animal.pega_dados_animal_alterar(
            TIPO_CACHORRO
        )
        cachorro.numero_chip = dados_novos_cachorro["numero_chip"]
        cachorro.nome = dados_novos_cachorro["nome"]
        cachorro.raca = dados_novos_cachorro["raca"]
        cachorro.tamanho = TamanhoCachorro(dados_novos_cachorro["tamanho_cachorro"])

    def alterar_gato(self, numero_chip: str):
        gato = self.buscar_gato_por_numero_chip(numero_chip)
        dados_novos_gato = self.__tela_animal.pega_dados_animal_alterar(TIPO_GATO)
        gato.numero_chip = dados_novos_gato["numero_chip"]
        gato.nome = dados_novos_gato["nome"]
        gato.raca = dados_novos_gato["raca"]

    def excluir_animal(self):
        tipo_animal = self.__tela_animal.tela_opcoes_tipo_animal()
        numero_chip = self.__tela_animal.seleciona_animal()

        if tipo_animal == TIPO_CACHORRO:
            if self.verifica_nenhum_cachorro_cadastrado():
                return

            self.listar_cachorros()
            cachorro = self.buscar_cachorro_por_numero_chip(numero_chip)
            self.__cachorros.remove(cachorro)
            self.__tela_animal.mostra_mensagem("Cachorro removido com sucesso.")
        else:
            if self.verifica_nenhum_gato_cadastrado():
                return True

            self.listar_gatos()
            gato = self.buscar_gato_por_numero_chip(numero_chip)
            self.__gatos.remove(gato)
            self.__tela_animal.mostra_mensagem("Gato removido com sucesso.")

    def verifica_nenhum_cachorro_cadastrado(self):
        if len(self.__cachorros) <= 0:
            self.__tela_animal.mostra_mensagem("Nenhum cachorro cadastrado.")
            return True

    def verifica_nenhum_gato_cadastrado(self):
        if len(self.__gatos) <= 0:
            self.__tela_animal.mostra_mensagem("Nenhum gato cadastrado.")
            return True

    def listar_animal_por_numero_chip(self):
        tipo_animal = self.__tela_animal.tela_opcoes_tipo_animal()

        if tipo_animal == TIPO_CACHORRO:
            numero_chip = self.__tela_animal.seleciona_animal()
            cachorro = self.buscar_cachorro_por_numero_chip(numero_chip)

            dados_animal = {
                "numero_chip": cachorro.numero_chip,
                "nome": cachorro.nome,
                "raca": cachorro.raca,
                "tamanho_cachorro": cachorro.tamanho,
                "tipo_animal": TIPO_CACHORRO,
            }
        else:
            numero_chip = self.__tela_animal.seleciona_animal()
            gato = self.buscar_gato_por_numero_chip(numero_chip)
            dados_animal = {
                "numero_chip": gato.numero_chip,
                "nome": gato.nome,
                "raca": gato.raca,
                "tipo_animal": TIPO_GATO,
            }

        self.__tela_animal.mostra_animal(dados_animal)

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_animal,
            2: self.alterar_animal,
            3: self.excluir_animal,
            4: self.listar_animais,
            5: self.listar_animal_por_numero_chip,
            0: self.retornar,
        }

        while True:
            try:
                lista_opcoes[self.__tela_animal.tela_opcoes()]()
            except (OpcaoInvalidaException, EntidadeNaoEncontradaException) as e:
                self.__tela_animal.mostra_mensagem(e)
