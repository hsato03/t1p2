import unittest
from unittest.mock import patch
from tests.test_variables import *
from model import TIPO_GATO, TIPO_CPF
from exceptions import EntidadeNaoEncontradaException
from controllers import AdocaoController, SistemaController


class AdocaoTest(unittest.TestCase):
    def setUp(self):
        self.controlador_sistema = SistemaController()

        self.controlador_adocoes = AdocaoController(self.controlador_sistema)

        self.adocao_valida = [TIPO_GATO, cpf, numero_chip, data, termo_assinado]

        self.adocao_atualizada = [
            cpf_atualizado,
            numero_chip_atualizado,
            data,
            termo_assinado,
        ]

        self.adocao_adotante_invalido = [
            TIPO_GATO,
            cpf_invalido,
            numero_chip,
            data,
            termo_assinado,
        ]

        self.adocao_animal_invalido = [
            TIPO_GATO,
            cpf,
            numero_chip_invalido,
            data,
            termo_assinado,
        ]

        self.adocao_termo_assinado_invalido = [
            TIPO_GATO,
            cpf,
            numero_chip,
            data,
            termo_assinado_invalido,
        ]

        self.adotante_valido = [
            cpf,
            nome,
            data,
            tipo_habitacao_casa,
            tamanho_habitacao_pequeno,
            possui_animal,
            logradouro,
            numero,
        ]

        self.adotante_atualizado = [
            cpf_atualizado,
            nome,
            data,
            tipo_habitacao_casa,
            tamanho_habitacao_pequeno,
            possui_animal,
            logradouro,
            numero,
        ]

        self.adotante_invalido = [
            cpf_invalido,
            nome,
            data,
            tipo_habitacao_casa,
            tamanho_habitacao_pequeno,
            possui_animal,
            logradouro,
            numero,
        ]

        self.animal_valido = [numero_chip, nome, tipo_gato, raca]

        self.animal_invalido = [numero_chip_invalido, nome, tipo_gato, raca]

        self.animal_atualizado = [numero_chip_atualizado, nome, tipo_gato, raca]

        self.incluir_adotante_animal_test(self.adotante_valido, self.animal_valido)
        self.incluir_adotante_animal_test(
            self.adotante_atualizado, self.animal_atualizado
        )

    def incluir_adotante_animal_test(self, dados_adotante, dados_animal):
        with patch("builtins.input", side_effect=dados_adotante):
            try:
                self.controlador_sistema.controlador_adotantes.incluir_adotante()
            except EntidadeNaoEncontradaException:
                self.fail("Adotante nao encontrado")

        with patch("builtins.input", side_effect=dados_animal):
            try:
                self.controlador_sistema.controlador_animais.incluir_animal()
            except EntidadeNaoEncontradaException:
                self.fail("Animal nao encontrado")

    def incluir_adocao_test(self, dados_adocao):
        with patch("builtins.input", side_effect=dados_adocao):
            try:
                self.controlador_adocoes.incluir_adocao()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir Adocao")

    def test_incluir_adocao_should_work_when_valid_data_1(self):
        self.incluir_adocao_test(self.adocao_valida)

    def test_incluir_adocao_should_work_when_valid_data_2(self):
        dados_adocao = [
            TIPO_GATO,
            cpf,
            numero_chip,
            data,
            termo_nao_assinado,
        ]
        self.incluir_adocao_test(dados_adocao)

    def test_incluir_adocao_should_raise_exception_when_cpf_invalido(self):
        with patch("builtins.input", side_effect=self.adocao_adotante_invalido):
            with self.assertRaises(EntidadeNaoEncontradaException):
                self.controlador_adocoes.incluir_adocao()

    def test_incluir_adocao_should_raise_exception_when_numero_chip_invalido(self):
        with patch("builtins.input", side_effect=self.adocao_animal_invalido):
            with self.assertRaises(EntidadeNaoEncontradaException):
                self.controlador_adocoes.incluir_adocao()

    def test_incluir_adocao_should_raise_exception_when_assinar_termo_invalido(self):
        with patch("builtins.input", side_effect=self.adocao_termo_assinado_invalido):
            with self.assertRaises(StopIteration):
                self.controlador_adocoes.incluir_adocao()

    def test_excluir_adocao_should_work_when_valid_data(self):
        self.incluir_adocao_test(self.adocao_valida)
        dados_exclusao = [TIPO_CPF, cpf]
        with patch("builtins.input", side_effect=dados_exclusao):
            try:
                self.controlador_adocoes.excluir_adocao()
            except EntidadeNaoEncontradaException:
                self.fail("Ocorreu um erro excluir Adocao: entidade nao encontrada")

    def test_excluir_adocao_should_raise_exception_when_cpf_invalido(self):
        self.incluir_adocao_test(self.adocao_valida)
        dados_exclusao = [TIPO_CPF, cpf_invalido]
        with patch("builtins.input", side_effect=dados_exclusao):
            with self.assertRaises(EntidadeNaoEncontradaException):
                self.controlador_adocoes.excluir_adocao()

    def test_excluir_adocao_should_raise_exception_when_numero_chip_invalido(self):
        self.incluir_adocao_test(self.adocao_valida)
        dados_exclusao = [TIPO_CPF, cpf_invalido]
        with patch("builtins.input", side_effect=dados_exclusao):
            with self.assertRaises(EntidadeNaoEncontradaException):
                self.controlador_adocoes.excluir_adocao()

    def test_excluir_adocao_should_raise_exception_when_tipo_id_invalido(self):
        self.incluir_adocao_test(self.adocao_valida)
        dados_exclusao = [100, cpf]
        with patch("builtins.input", side_effect=dados_exclusao):
            with self.assertRaises(StopIteration):
                self.controlador_adocoes.excluir_adocao()

    def test_alterar_adocao_should_work_when_valid_data(self):
        self.incluir_adocao_test(self.adocao_valida)
        with patch(
            "builtins.input", side_effect=[TIPO_CPF, cpf] + self.adocao_atualizada
        ):
            try:
                self.controlador_adocoes.alterar_adocao()
            except EntidadeNaoEncontradaException:
                self.fail("Ocorreu um erro ao alterar Adocao: entidade nao encontrada")

        try:
            adoacao_atualizada = (
                self.controlador_adocoes.buscar_adocao_por_identificador(
                    cpf_atualizado, TIPO_CPF
                )
            )
        except EntidadeNaoEncontradaException:
            self.fail("Adocao nao alterada.")

        self.assertEqual(cpf_atualizado, adoacao_atualizada.adotante.cpf)
        self.assertEqual(numero_chip_atualizado, adoacao_atualizada.animal.numero_chip)

    def test_alterar_adocao_should_raise_execption_when_cpf_invalido(self):
        self.incluir_adocao_test(self.adocao_valida)
        self.adocao_adotante_invalido.pop(0)
        with patch(
            "builtins.input",
            side_effect=[TIPO_CPF, cpf] + self.adocao_adotante_invalido,
        ):
            with self.assertRaises(EntidadeNaoEncontradaException):
                self.controlador_adocoes.alterar_adocao()

    def test_alterar_adocao_should_raise_execption_when_numero_chip_invalido(self):
        self.incluir_adocao_test(self.adocao_valida)
        self.adocao_animal_invalido.pop(0)
        with patch(
            "builtins.input", side_effect=[TIPO_CPF, cpf] + self.adocao_animal_invalido
        ):
            with self.assertRaises(EntidadeNaoEncontradaException):
                self.controlador_adocoes.alterar_adocao()

    def test_alterar_adocao_should_raise_exception_when_termo_assinado_invalido(self):
        self.incluir_adocao_test(self.adocao_valida)
        self.adocao_termo_assinado_invalido.pop(0)
        with patch(
            "builtins.input",
            side_effect=[TIPO_CPF, cpf] + self.adocao_termo_assinado_invalido,
        ):
            with self.assertRaises(StopIteration):
                self.controlador_adocoes.alterar_adocao()

    def test_alterar_adocao_should_raise_exception_when_tipo_id_invalido(self):
        self.incluir_adocao_test(self.adocao_valida)
        with patch("builtins.input", side_effect=[100, cpf] + self.adocao_atualizada):
            with self.assertRaises(StopIteration):
                self.controlador_adocoes.alterar_adocao()
