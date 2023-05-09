from model.endereco import Endereco
from views.adotante_view import AdotanteView
from model.adotante import Adotante
from datetime import datetime
from model.tipo_habitacao import TipoHabitacao
from model.tamanho_habitacao import TamanhoHabitacao


class AdotanteController:
    def __init__(self, controlador_sistema):
        self.__adotantes = []
        self.__tela_adotante = AdotanteView()
        self.__controlador_sistema = controlador_sistema

    def pega_adotante_por_cpf(self, cpf: int):
        for adotante in self.__adotantes:
            if adotante.cpf == cpf:
                return adotante
        return None

    def incluir_adotante(self):
        dados_adotante = self.__tela_adotante.pega_dados_adotante()
        data_nascimento_formatada = datetime.strptime(
            dados_adotante["data_nascimento"], "%d/%m/%Y"
        )

        adotante = Adotante(
            dados_adotante["cpf"],
            dados_adotante["nome"],
            data_nascimento_formatada.date(),
            dados_adotante["logradouro"],
            dados_adotante["numero"],
            TipoHabitacao(dados_adotante["tipo_habitacao"]),
            TamanhoHabitacao(dados_adotante["tamanho_habitacao"]),
            True if dados_adotante["possui_animal"] == 1 else False,
        )
        self.__adotantes.append(adotante)

    def alterar_adotante(self):
        self.listar_adotantes()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_cpf(cpf_adotante)

        if adotante is not None:
            novos_dados_adotante = self.__tela_adotante.pega_dados_adotante()
            adotante.nome = novos_dados_adotante["nome"]
            adotante.cpf = novos_dados_adotante["cpf"]
            adotante.data_nascimento = novos_dados_adotante["data_nascimento"]
            adotante.tipo_habitacao = TipoHabitacao(
                novos_dados_adotante["tipo_habitacao"]
            )
            adotante.tamanho_habitacao = TamanhoHabitacao(
                novos_dados_adotante["tamanho_habitacao"]
            )
            adotante.possui_animal = (
                True if novos_dados_adotante["possui_animal"] == 1 else False
            )
            adotante.add_endereco(
                novos_dados_adotante["logradouro"], novos_dados_adotante["numero"]
            )
            self.listar_adotantes()
        else:
            self.__tela_adotante.mostra_mensagem("ATENCAO: Adotante não existente")

    # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
    def listar_adotantes(self):
        for adotante in self.__adotantes:
            self.__tela_adotante.mostra_adotante(
                {
                    "cpf": adotante.cpf,
                    "nome": adotante.nome,
                    "data_nascimento": adotante.data_nascimento,
                    "tipo_habitacao": adotante.tipo_habitacao,
                    "tamanho_habitacao": adotante.tamanho_habitacao,
                    "possui_animal": adotante.possui_animal,
                    "endereco": adotante.endereco,
                }
            )

    def excluir_adotante(self):
        self.listar_adotantes()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.pega_adotante_por_cpf(cpf_adotante)

        if adotante is not None:
            self.__adotantes.remove(adotante)
            self.listar_adotantes()
        else:
            self.__tela_adotante.mostra_mensagem("ATENCAO: Amigo não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_adotante,
            2: self.alterar_adotante,
            3: self.listar_adotantes,
            4: self.excluir_adotante,
            0: self.retornar,
        }

        continua = True
        while continua:
            lista_opcoes[self.__tela_adotante.tela_opcoes()]()
