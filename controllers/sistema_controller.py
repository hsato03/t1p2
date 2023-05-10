from views.sistema_view import SistemaView
from controllers.adotante_controller import AdotanteController
from exceptions.opcao_invalida_exception import OpcaoInvalidaException


class SistemaController:
    def __init__(self):
        self.__controlador_adotantes = AdotanteController(self)
        self.__tela_sistema = SistemaView()

    @property
    def controlador_adotantes(self):
        return self.__controlador_adotantes

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_adotantes(self):
        self.__controlador_adotantes.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_adotantes, 0: self.encerra_sistema}

        while True:
            try:
                opcao_escolhida = self.__tela_sistema.tela_opcoes()
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            except OpcaoInvalidaException as e:
                print(e)
