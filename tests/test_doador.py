import io
import sys
import unittest
from unittest.mock import patch
from datetime import datetime
from controllers import DoadorController
from exceptions import EntidadeNaoEncontradaException


class DoadorTest(unittest.TestCase):
    def setUp(self):
        self.controlador_doadores = DoadorController(None)
        self.cpf = "27797914036"
        self.cpf_invalido = "1234567890"
        self.cpf_atualizado = "78472414043"
        self.nome = "nome"
        self.nome_atualizado = "nomeAtualizado"
        self.data_nascimento = "03/03/2003"
        self.data_nascimento_atualizada = "02/02/2002"
        self.data_nascimento_invalida = "10-10-1000"
        self.logradouro = "Rua das Flores"
        self.logradouro_atualizado = "Rua Atualizada"
        self.numero = "123A"
        self.numero_atualizado = "321B"

        self.doador_valido = [
            self.cpf,
            self.nome,
            self.data_nascimento,
            self.logradouro,
            self.numero,
        ]

        self.doador_data_nascimento_invalida = [
            self.cpf,
            self.nome,
            self.data_nascimento_invalida,
            self.logradouro,
            self.numero,
        ]

    def incluir_doador_test(self, dados_doador):
        with patch("builtins.input", side_effect=dados_doador):
            try:
                self.controlador_doadores.incluir_doador()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir uma pessoa")

    def test_incluir_doador_should_work_when_correct_data_(self):
        self.incluir_doador_test(self.doador_valido)

    def test_incluir_doador_should_throw_exception_when_data_nascimento_invalida(
        self,
    ):
        with patch("builtins.input", side_effect=self.doador_data_nascimento_invalida):
            with self.assertRaises(StopIteration):
                self.controlador_doadores.incluir_doador()

    def test_excluir_doador_should_work_when_correct_data(self):
        self.incluir_doador_test(self.doador_valido)

        try:
            sys.stdin = io.StringIO(self.cpf)
            self.controlador_doadores.excluir_doador()
        except EntidadeNaoEncontradaException:
            self.fail("Ocorreu um erro ao excluir uma pessoa")

        with self.assertRaises(EntidadeNaoEncontradaException):
            self.controlador_doadores.buscar_doador_por_cpf(self.cpf)

    def test_excluir_doador_should_raise_exception_when_cpf_invalido(
        self,
    ):
        self.incluir_doador_test(self.doador_valido)

        with self.assertRaises(EntidadeNaoEncontradaException):
            sys.stdin = io.StringIO(self.cpf_invalido)
            self.controlador_doadores.excluir_doador()

    def test_alterar_doador_should_work_when_correct_data(self):
        self.incluir_doador_test(self.doador_valido)

        dados_alteracao = [
            self.cpf,
            self.cpf_atualizado,
            self.nome_atualizado,
            self.data_nascimento_atualizada,
            self.logradouro_atualizado,
            self.numero_atualizado,
        ]

        with patch("builtins.input", side_effect=dados_alteracao):
            try:
                self.controlador_doadores.alterar_doador()
            except EntidadeNaoEncontradaException:
                self.fail(
                    "Ocorreu um erro ao alterar doador! Entidade nao encontrada."
                )

        try:
            doador_atualizado = self.controlador_doadores.buscar_doador_por_cpf(
                self.cpf_atualizado
            )
        except EntidadeNaoEncontradaException:
            self.fail("Doador nao alterado.")

        self.assertEqual(dados_alteracao[1], doador_atualizado.cpf)
        self.assertEqual(dados_alteracao[2], doador_atualizado.nome)
        self.assertEqual(datetime.strptime(dados_alteracao[3], "%d/%m/%Y").date(),
                         doador_atualizado.data_nascimento)
        self.assertEqual(dados_alteracao[4], doador_atualizado.endereco.logradouro)
        self.assertEqual(dados_alteracao[5], doador_atualizado.endereco.numero)

    def test_alterar_doador_should_raise_exception_when_cpf_invalido(
        self,
    ):
        self.incluir_doador_test(self.doador_valido)

        with self.assertRaises(EntidadeNaoEncontradaException):
            sys.stdin = io.StringIO(self.cpf_invalido)
            self.controlador_doadores.alterar_doador()

    def test_alterar_doador_should_throw_exception_when_data_nascimento_invalida(self):
        self.incluir_doador_test(self.doador_valido)

        with patch("builtins.input", side_effect=self.doador_data_nascimento_invalida):
            with self.assertRaises(StopIteration):
                self.controlador_doadores.alterar_doador()
