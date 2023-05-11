from views.main_view import SistemaView
from controllers.adotante_controller import AdotanteController
from controllers.adocao_controller import AdocaoController
from controllers.animal_controller import AnimalController
from exceptions.opcao_invalida_exception import OpcaoInvalidaException


class SistemaController:
    def __init__(self):
        self.__controlador_adotantes = AdotanteController(self)
        self.__controlador_adocoes = AdocaoController(self)
        self.__controlador_animais = AnimalController(self)
        self.__tela_sistema = SistemaView()

    @property
    def controlador_adotantes(self):
        return self.__controlador_adotantes

    @property
    def controlador_adocoes(self):
        return self.__controlador_adocoes

    @property
    def controlador_animais(self):
        return self.__controlador_animais

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_adotantes(self):
        self.__controlador_adotantes.abre_tela()

    def cadastra_adocoes(self):
        self.__controlador_adocoes.abre_tela()

    def cadastra_animais(self):
        self.__controlador_animais.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            3: self.cadastra_animais,
            2: self.cadastra_adocoes,
            1: self.cadastra_adotantes,
            0: self.encerra_sistema,
        }

        while True:
            try:
                opcao_escolhida = self.__tela_sistema.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            except OpcaoInvalidaException as e:
                print(e)
            except ValueError:
                print("Somente numeros. Tente novamente.")
