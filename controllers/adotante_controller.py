from views import AdotanteView
from model import Adotante, TipoHabitacao, TamanhoHabitacao
from exceptions import EntidadeNaoEncontradaException, OpcaoInvalidaException


class AdotanteController:
    def __init__(self, controlador_sistema):
        self.__adotantes = []
        self.__tela_adotante = AdotanteView()
        self.__controlador_principal = controlador_sistema

    def buscar_adotante_por_cpf(self, cpf: str):
        for adotante in self.__adotantes:
            if adotante.cpf == cpf:
                return adotante
        raise EntidadeNaoEncontradaException("ERRO: Adotante nao existente.")

    def incluir_adotante(self):
        dados_adotante = self.__tela_adotante.pega_dados_adotante()

        adotante = Adotante(
            dados_adotante["cpf"],
            dados_adotante["nome"],
            dados_adotante["data_nascimento"],
            dados_adotante["logradouro"],
            dados_adotante["numero"],
            TipoHabitacao(dados_adotante["tipo_habitacao"]),
            TamanhoHabitacao(dados_adotante["tamanho_habitacao"]),
            True if dados_adotante["possui_animal"] == 1 else False,
        )
        self.__adotantes.append(adotante)

    def alterar_adotante(self):
        if len(self.__adotantes) <= 0:
            self.__tela_adotante.mostra_mensagem("Nenhum adotante cadastrado.")
            return

        self.listar_adotantes()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.buscar_adotante_por_cpf(cpf_adotante)
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



    def listar_adotantes(self):
        if len(self.__adotantes) <= 0:
            raise EntidadeNaoEncontradaException("Nenhum adotante cadastrado.")

        for i in range(len(self.__adotantes)):
            adotante = self.__adotantes[i]
            self.__tela_adotante.mostra_mensagem(f"ADOTANTE #{i + 1:02d}")
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
        if len(self.__adotantes) <= 0:
            self.__tela_adotante.mostra_mensagem("Nenhum adotante cadastrado.")
            return

        self.listar_adotantes()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.buscar_adotante_por_cpf(cpf_adotante)

        self.__adotantes.remove(adotante)
        self.__tela_adotante.mostra_mensagem("Adotante removido com sucesso.")


    def listar_adotante_por_cpf(self):
        if len(self.__adotantes) <= 0:
            self.__tela_adotante.mostra_mensagem("Nenhum adotante cadastrado.")
            return

        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        adotante = self.buscar_adotante_por_cpf(cpf_adotante)

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

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_adotante,
            2: self.alterar_adotante,
            3: self.listar_adotantes,
            4: self.excluir_adotante,
            5: self.listar_adotante_por_cpf,
            0: self.retornar,
        }

        while True:
            try:
                lista_opcoes[self.__tela_adotante.tela_opcoes()]()
            except (OpcaoInvalidaException, EntidadeNaoEncontradaException) as e:
                self.__tela_adotante.mostra_mensagem(e)
            except ValueError:
                self.__tela_adotante.mostra_mensagem(
                    "Somente numeros. Tente novamente."
                )
