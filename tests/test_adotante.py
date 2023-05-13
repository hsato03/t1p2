import io
import sys
import unittest
from unittest.mock import patch
from controllers import AdotanteController
from exceptions import EntidadeNaoEncontradaException


class AdotanteTest(unittest.TestCase):
    def setUp(self):
        self.controlador_adotantes = AdotanteController(None)
        self.cpf = "27797914036"
        self.cpf_invalido = "1234567890"
        self.nome = "Henrique"
        self.data_nascimento = "03/03/2003"
        self.data_nascimento_invalida = "100/100/10000"
        self.tipo_habitacao_casa = "1"
        self.tipo_habitacao_apartamento = "2"
        self.tipo_habitacao_invalido = "100"
        self.tamanho_habitacao_pequeno = "1"
        self.tamanho_habitacao_medio = "2"
        self.tamanho_habitacao_grande = "3"
        self.tamanho_habitacao_invalido = "100"
        self.possui_animal = "1"
        self.nao_possui_animal = "2"
        self.possui_animal_invalido = "100"
        self.logradouro = "Rua das Flores"
        self.numero = "123A"

    # Os testes test_incluir_adotante_should_work_when_correct_data (1,2,3)
    # percorrem todos os valores validos para incluir um adotante
    def test_incluir_adotante_should_work_when_correct_data_1(self):
        adotante = [
            self.cpf,
            self.nome,
            self.data_nascimento,
            self.tipo_habitacao_casa,
            self.tamanho_habitacao_pequeno,
            self.possui_animal,
            self.logradouro,
            self.numero,
        ]
        with patch("builtins.input", side_effect=adotante):
            try:
                self.controlador_adotantes.incluir_adotante()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir uma pessoa")

    def test_incluir_adotante_should_work_when_correct_data_2(self):
        adotante = [
            self.cpf,
            self.nome,
            self.data_nascimento,
            self.tipo_habitacao_apartamento,
            self.tamanho_habitacao_medio,
            self.nao_possui_animal,
            self.logradouro,
            self.numero,
        ]
        with patch("builtins.input", side_effect=adotante):
            try:
                self.controlador_adotantes.incluir_adotante()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir uma pessoa")

    def test_incluir_adotante_should_work_when_correct_data_3(self):
        adotante = [
            self.cpf,
            self.nome,
            self.data_nascimento,
            self.tipo_habitacao_apartamento,
            self.tamanho_habitacao_grande,
            self.nao_possui_animal,
            self.logradouro,
            self.numero,
        ]
        with patch("builtins.input", side_effect=adotante):
            try:
                self.controlador_adotantes.incluir_adotante()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir uma pessoa")

    def test_incluir_adotante_should_throw_exception_when_data_nascimento_invalida(
        self,
    ):
        adotante = [
            self.cpf,
            self.nome,
            self.data_nascimento_invalida,
            self.tipo_habitacao_casa,
            self.tamanho_habitacao_pequeno,
            self.possui_animal,
            self.logradouro,
            self.numero,
        ]

        with patch("builtins.input", side_effect=adotante):
            with self.assertRaises(StopIteration):
                self.controlador_adotantes.incluir_adotante()

    def test_incluir_adotante_should_raise_exception_when_tipo_habitacao_invalido(
        self,
    ):
        adotante = [
            self.cpf,
            self.nome,
            self.data_nascimento,
            self.tipo_habitacao_invalido,
            self.tamanho_habitacao_pequeno,
            self.possui_animal,
            self.logradouro,
            self.numero,
        ]

        with patch("builtins.input", side_effect=adotante):
            with self.assertRaises(StopIteration):
                self.controlador_adotantes.incluir_adotante()

    def test_incluir_adotante_should_raise_exception_when_tamanho_habitacao_invalido(
        self,
    ):
        adotante = [
            self.cpf,
            self.nome,
            self.data_nascimento,
            self.tipo_habitacao_casa,
            self.tamanho_habitacao_invalido,
            self.possui_animal,
            self.logradouro,
            self.numero,
        ]

        with patch("builtins.input", side_effect=adotante):
            with self.assertRaises(StopIteration):
                self.controlador_adotantes.incluir_adotante()

    def test_incluir_adotante_should_raise_exception_when_possui_animal_invalido(
        self,
    ):
        adotante = [
            self.cpf,
            self.nome,
            self.data_nascimento,
            self.tipo_habitacao_casa,
            self.tamanho_habitacao_pequeno,
            self.possui_animal_invalido,
            self.logradouro,
            self.numero,
        ]

        with patch("builtins.input", side_effect=adotante):
            with self.assertRaises(StopIteration):
                self.controlador_adotantes.incluir_adotante()

    # TODO: Excluir e alterar
    def test_excluir_adotante_should_work_when_correct_data(self):
        adotante = [
            self.cpf,
            self.nome,
            self.data_nascimento,
            self.tipo_habitacao_casa,
            self.tamanho_habitacao_pequeno,
            self.possui_animal,
            self.logradouro,
            self.numero,
        ]

        with patch("builtins.input", side_effect=adotante):
            try:
                self.controlador_adotantes.incluir_adotante()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir uma pessoa")

        try:
            sys.stdin = io.StringIO(self.cpf)
            self.controlador_adotantes.excluir_adotante()
        except EntidadeNaoEncontradaException:
            self.fail("Ocorreu um erro ao excluir uma pessoa")

        with self.assertRaises(EntidadeNaoEncontradaException):
            self.controlador_adotantes.buscar_adotante_por_cpf(self.cpf)

    def test_excluir_adotante_should_raise_exception_when_cpf_invalido(
        self,
    ):
        adotante = [
            self.cpf,
            self.nome,
            self.data_nascimento,
            self.tipo_habitacao_casa,
            self.tamanho_habitacao_pequeno,
            self.possui_animal,
            self.logradouro,
            self.numero,
        ]

        with patch("builtins.input", side_effect=adotante):
            try:
                self.controlador_adotantes.incluir_adotante()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir uma pessoa")

        with self.assertRaises(EntidadeNaoEncontradaException):
            sys.stdin = io.StringIO(self.cpf_invalido)
            self.controlador_adotantes.excluir_adotante()
