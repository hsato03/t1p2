from views.animal_view import AnimalView
from model.cachorro import Cachorro
from model.tamanho_cachorro import TamanhoCachorro
from model.gato import Gato
from exceptions.entidade_nao_encontrada_exception import EntidadeNaoEncontradaException


class AnimalController:
    def __init__(self, controlador_principal):
        self.__gatos = []
        self.__cachorros = []
        self.__controlador_principal = controlador_principal
        self.__tela_animal = AnimalView()

    def buscar_animal_por_numero_chip(self, numero_chip: str):
        gato = self.buscar_gato_por_numero_chip(numero_chip)
        if gato is not None:
            return gato
            
        cachorro = self.buscar_cachorro_por_numero_chip(numero_chip)
        if cachorro is not None:
            return cachorro

        raise EntidadeNaoEncontradaException("ERRO: Animal nao existente")
    
    def buscar_gato_por_numero_chip(self, numero_chip: str):
        for gato in self.__gatos:
            if gato.numero_chip == numero_chip:
                return gato
        return None

    def buscar_cachorro_por_numero_chip(self, numero_chip: str):
        for cachorro in self.__cachorros:
            if cachorro.numero_chip == numero_chip:
                return cachorro
        return None

    def incluir_animal(self):
        dados_animal = self.__tela_animal.pega_dados_animal()

        if dados_animal["tipo_animal"] == 1:
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

        if tipo_animal == 1:
            self.listar_cachorros()

        else:
            self.listar_gatos()

    def listar_cachorros(self):
        if len(self.__cachorros) <= 0:
            self.__tela_animal.mostra_mensagem("Nenhum cachorro cadastrado.")
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
                    "tipo_animal": tipo_animal
                }
            )

    def listar_gatos(self):
        if len(self.__gatos) <= 0:
            self.__tela_animal.mostra_mensagem("Nenhum gato cadastrado.")
            return

        for i in range(len(self.__gatos)):
            gato = self.__gatos[i]
            self.__tela_animal.mostra_mensagem(f"GATO #{i + 1:02d}")
            self.__tela_animal.mostra_animal(
                {
                    "numero_chip": gato.numero_chip,
                    "nome": gato.nome,
                    "raca": gato.raca,
                    "tipo_animal": tipo_animal
                }
            )

    # TODO
    def alterar_animal(self):
        pass

    def excluir_animal(self):
        tipo_animal = self.__tela_animal.tela_opcoes_tipo_animal()
        numero_chip = self.__tela_animal.seleciona_animal()

        if tipo_animal == 1:
            if len(self.__cachorros) <= 0:
                self.__tela_animal.mostra_mensagem("Nenhum cachorro cadastrado.")
                return

            try:
                self.listar_cachorros()
                cachorro = self.buscar_cachorro_por_numero_chip(numero_chip)
                self.__cachorros.remove(cachorro)
                self.__tela_animal.mostra_mensagem("Cachorro removido com sucesso.")
            except EntidadeNaoEncontradaException as e:
                print(e)

        else:
            if len(self.__gatos) <= 0:
                self.__tela_animal.mostra_mensagem("Nenhum gato cadastrado")
                return
            
            try:
                self.listar_gatos
                gato = self.buscar_gato_por_numero_chip(numero_chip)
                self.__gatos.remove(gato)
                self.__tela_animal.mostra_mensagem("Gato removido com sucesso.")
            except EntidadeNaoEncontradaException as e:
                print(e)      

    def listar_animal_por_numero_chip(self):
        numero_chip = self.__tela_animal.seleciona_animal()
        try:
            animal = self.buscar_animal_por_numero_chip(numero_chip)   
            dados_animal = {
                "numero_chip": animal.numero_chip,
                "nome": animal.nome,
                "raca": animal.raca,
            }

            if isinstance(animal, Cachorro):
                dados_animal["tipo_animal"] = 1
                dados_animal["tamanho_cachorro"] = animal.tamanho
            else:
                dados_animal["tipo_animal"] = 2
            
            self.__tela_animal.mostra_animal(dados_animal)
        except EntidadeNaoEncontradaException as e:
            print(e)

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
            lista_opcoes[self.__tela_animal.tela_opcoes()]()
