from views.animal_view import AnimalView
from model.cachorro import Cachorro
from model.tamanho_cachorro import TamanhoCachorro
from model.gato import Gato


class AnimalController:
    def __init__(self, controlador_principal):
        self.__gatos = []
        self.__cachorros = []
        self.__controlador_principal = controlador_principal
        self.__tela_animal = AnimalView()

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
            if len(self.__cachorros) <= 0:
                print("Nenhum cachorro cadastrado.")
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

        else:
            if len(self.__gatos) <= 0:
                print("Nenhum gato cadastrado.")
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

    def alterar_animal(self):
        pass

    def excluir_animal(self):
        pass

    def listar_animal_por_chip(self):
        pass

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_animal,
            2: self.alterar_animal,
            3: self.excluir_animal,
            4: self.listar_animais,
            5: self.listar_animal_por_chip,
            0: self.retornar,
        }

        while True:
            lista_opcoes[self.__tela_animal.tela_opcoes()]()
