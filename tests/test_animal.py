import io
import sys
import unittest
from unittest.mock import patch
from controllers import AnimalController
from exceptions import EntidadeNaoEncontradaException, OpcaoInvalidaException


class AnimalTest(unittest.TestCase):
    # TODO: Refatorar input com variaveis no setUp
    def setUp(self):
        self.controlador_animais = AnimalController(None)
        self.numero_chip = "1"
        self.numero_chip_atualizado = "10"
        self.numero_chip_invalido = "100"
        self.nome = "nome"
        self.nome_atualizado = "nomeAtualizado"
        self.tipo_cachorro = 1
        self.tipo_gato = 2
        self.tipo_animal_invalido = 100
        self.raca = "raca"
        self.raca_atualizada = "racaAtualizada"
        self.tamanho_cachorro_pequeno = 1
        self.tamanho_cachorro_medio = 2
        self.tamanho_cachorro_grande = 3
        self.tamanho_cachorro_invalido = 100
        self.cachorro_valido = [
            self.numero_chip,
            self.nome,
            self.tipo_cachorro,
            self.raca,
            self.tamanho_cachorro_pequeno,
        ]
        self.gato_valido = [self.numero_chip, self.nome, self.tipo_gato, self.raca]

    def incluir_cachorro_test(self, dados_cachorro):
        with patch("builtins.input", side_effect=dados_cachorro):
            try:
                self.controlador_animais.incluir_animal()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir o cachorro! Dados invalidos.")

    def incluir_gato_test(self, dados_gato):
        with patch("builtins.input", side_effect=dados_gato):
            try:
                self.controlador_animais.incluir_animal()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir o gato! Dados inválidos.")

    def test_incluir_cachorro_pequeno_should_work_when_valid_data(self):
        cachorro = [
            self.numero_chip,
            self.nome,
            self.tipo_cachorro,
            self.raca,
            self.tamanho_cachorro_pequeno,
        ]
        self.incluir_gato_test(cachorro)

    def test_incluir_cachorro_medio_should_work_when_valid_data(self):
        cachorro = [
            self.numero_chip,
            self.nome,
            self.tipo_cachorro,
            self.raca,
            self.tamanho_cachorro_medio,
        ]
        self.incluir_cachorro_test(cachorro)

    def test_incluir_cachorro_grande_should_work_when_valid_data(self):
        cachorro = [
            self.numero_chip,
            self.nome,
            self.tipo_cachorro,
            self.raca,
            self.tamanho_cachorro_grande,
        ]
        self.incluir_cachorro_test(cachorro)

    def test_incluir_cachorro_should_raise_exception_when_tamanho_cachorro_invalido(
        self,
    ):
        cachorro = [
            self.numero_chip,
            self.nome,
            self.tipo_cachorro,
            self.raca,
            self.tamanho_cachorro_invalido,
        ]
        with patch("builtins.input", side_effect=cachorro):
            with self.assertRaises(StopIteration):
                self.controlador_animais.incluir_animal()

    def test_incluir_gato_should_work_when_valid_data(self):
        gato = [self.numero_chip, self.nome, self.tipo_gato, self.raca]
        self.incluir_gato_test(gato)

    def test_incluir_animal_should_raise_exception_when_tipo_animal_invalido(self):
        animal = [self.numero_chip, self.nome, self.tipo_animal_invalido]
        with patch("builtins.input", side_effect=animal):
            with self.assertRaises(StopIteration):
                self.controlador_animais.incluir_animal()

    def test_excluir_cachorro_should_work_when_valid_data(self):
        self.incluir_cachorro_test(self.cachorro_valido)

        dados_exclusao = [self.tipo_cachorro, self.numero_chip]
        with patch("builtins.input", side_effect=dados_exclusao):
            try:
                self.controlador_animais.excluir_animal()
            except EntidadeNaoEncontradaException:
                self.fail(
                    "Ocorreu um erro ao excluir cachorro! Entidade nao encontrada."
                )

    def test_excluir_cachorro_should_raise_exception_when_numero_chip_invalido(self):
        self.incluir_cachorro_test(self.cachorro_valido)

        dados_exclusao = [self.tipo_cachorro, self.numero_chip_invalido]
        with patch("builtins.input", side_effect=dados_exclusao):
            with self.assertRaises(EntidadeNaoEncontradaException):
                self.controlador_animais.excluir_animal()

    def test_excluir_gato_should_work_when_valid_data(self):
        self.incluir_gato_test(self.gato_valido)

        dados_exclusao = [self.tipo_gato, self.numero_chip]
        with patch("builtins.input", side_effect=dados_exclusao):
            try:
                self.controlador_animais.excluir_animal()
            except EntidadeNaoEncontradaException:
                self.fail("Ocorreu um erro ao excluir gato! Entidade nao encontrada.")

    def test_excluir_gato_should_raise_exception_when_numero_chip_invalido(self):
        self.incluir_gato_test(self.gato_valido)

        dados_exclusao = [self.tipo_gato, self.numero_chip_invalido]
        with patch("builtins.input", side_effect=dados_exclusao):
            with self.assertRaises(EntidadeNaoEncontradaException):
                self.controlador_animais.excluir_animal()

    def test_excluir_animal_should_raise_exception_when_tipo_animal_invalido(self):
        self.incluir_gato_test(self.gato_valido)

        dados_exclusao = [self.tipo_animal_invalido, self.numero_chip]
        with patch("builtins.input", side_effect=dados_exclusao):
            with self.assertRaises(OpcaoInvalidaException):
                self.controlador_animais.excluir_animal()

    def test_alterar_cachorro_should_work_when_valid_data(self):
        self.incluir_cachorro_test(self.cachorro_valido)

        dados_alteracao = [
            self.tipo_cachorro,
            self.numero_chip,
            self.numero_chip_atualizado,
            self.nome_atualizado,
            self.raca_atualizada,
            self.tamanho_cachorro_medio,
        ]
        with patch("builtins.input", side_effect=dados_alteracao):
            try:
                self.controlador_animais.alterar_animal()
            except EntidadeNaoEncontradaException:
                self.fail(
                    "Ocorreu um erro ao alterar cachorro! Entidade nao encontrada."
                )

        try:
            cachorro_atualizado = (
                self.controlador_animais.buscar_cachorro_por_numero_chip(
                    self.numero_chip_atualizado
                )
            )
        except EntidadeNaoEncontradaException:
            self.fail("Cachorro nao alterado.")

        self.assertEqual(dados_alteracao[2], cachorro_atualizado.numero_chip)
        self.assertEqual(dados_alteracao[3], cachorro_atualizado.nome)
        self.assertEqual(dados_alteracao[4], cachorro_atualizado.raca)
        self.assertEqual(dados_alteracao[5], cachorro_atualizado.tamanho.value)

    def test_alterar_cachorro_should_raise_exception_when_tamanho_cachorro_invalido(
        self,
    ):
        self.incluir_cachorro_test(self.cachorro_valido)

        dados_alteracao = [
            self.tipo_cachorro,
            self.numero_chip,
            self.numero_chip_atualizado,
            self.nome_atualizado,
            self.raca_atualizada,
            self.tamanho_cachorro_invalido,
        ]
        with patch("builtins.input", side_effect=dados_alteracao):
            with self.assertRaises(StopIteration):
                self.controlador_animais.alterar_animal()

    def test_alterar_gato_should_work_when_valid_data(self):
        self.incluir_gato_test(self.gato_valido)

        dados_alteracao = [
            self.tipo_gato,
            self.numero_chip,
            self.numero_chip_atualizado,
            self.nome_atualizado,
            self.raca_atualizada,
        ]

        with patch("builtins.input", side_effect=dados_alteracao):
            try:
                self.controlador_animais.alterar_animal()
            except EntidadeNaoEncontradaException:
                self.fail(
                    "Ocorreu um erro ao alterar cachorro! Entidade nao encontrada."
                )

        try:
            gato_atualizado = self.controlador_animais.buscar_gato_por_numero_chip(
                self.numero_chip_atualizado
            )
        except EntidadeNaoEncontradaException:
            self.fail("Gato nao alterado.")

        self.assertEqual(dados_alteracao[2], gato_atualizado.numero_chip)
        self.assertEqual(dados_alteracao[3], gato_atualizado.nome)
        self.assertEqual(dados_alteracao[4], gato_atualizado.raca)

    def test_alterar_animal_should_raise_exception_when_tipo_animal_invalido(self):
        self.incluir_gato_test(self.gato_valido)

        with self.assertRaises(OpcaoInvalidaException):
            sys.stdin = io.StringIO(str(self.tipo_animal_invalido))
            self.controlador_animais.alterar_animal()
