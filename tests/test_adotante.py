import io
import sys
import unittest
from unittest.mock import patch
from datetime import datetime
from controllers import AdotanteController
from exceptions import EntidadeNaoEncontradaException


class AdotanteTest(unittest.TestCase):
    def setUp(self):
        self.controlador_adotantes = AdotanteController(None)
        self.cpf = "27797914036"
        self.cpf_invalido = "1234567890"
        self.cpf_atualizado = "78472414043"
        self.nome = "nome"
        self.nome_atualizado = "nomeAtualizado"
        self.data_nascimento = "03/03/2003"
        self.data_nascimento_atualizada = "02/02/2002"
        self.data_nascimento_invalida = "10-10-1000"
        self.tipo_habitacao_casa = 1
        self.tipo_habitacao_apartamento = 2
        self.tipo_habitacao_invalido = 100
        self.tamanho_habitacao_pequeno = 1
        self.tamanho_habitacao_medio = 2
        self.tamanho_habitacao_grande = 3
        self.tamanho_habitacao_invalido = 100
        self.possui_animal = 1
        self.nao_possui_animal = 2
        self.possui_animal_invalido = "100"
        self.logradouro = "Rua das Flores"
        self.logradouro_atualizado = "Rua Atualizada"
        self.numero = "123A"
        self.numero_atualizado = "321B"

        self.adotante_valido = [
            self.cpf,
            self.nome,
            self.data_nascimento,
            self.tipo_habitacao_casa,
            self.tamanho_habitacao_pequeno,
            self.possui_animal,
            self.logradouro,
            self.numero,
        ]

        self.adotante_data_nascimento_invalida = [
            self.cpf,
            self.nome,
            self.data_nascimento_invalida,
            self.tipo_habitacao_casa,
            self.tamanho_habitacao_pequeno,
            self.possui_animal,
            self.logradouro,
            self.numero,
        ]

        self.adotante_tipo_habitacao_invalido = [
            self.cpf,
            self.nome,
            self.data_nascimento,
            self.tipo_habitacao_invalido,
            self.tamanho_habitacao_pequeno,
            self.possui_animal,
            self.logradouro,
            self.numero,
        ]

        self.adotante_tamanho_habitacao_invalido = [
            self.cpf,
            self.nome,
            self.data_nascimento,
            self.tipo_habitacao_casa,
            self.tamanho_habitacao_invalido,
            self.possui_animal,
            self.logradouro,
            self.numero,
        ]

        self.adotante_possui_animal_invalido = [
            self.cpf,
            self.nome,
            self.data_nascimento,
            self.tipo_habitacao_casa,
            self.tamanho_habitacao_pequeno,
            self.possui_animal_invalido,
            self.logradouro,
            self.numero,
        ]

    def incluir_adotante_test(self, dados_adotante):
        with patch("builtins.input", side_effect=dados_adotante):
            try:
                self.controlador_adotantes.incluir_adotante()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir uma pessoa")

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
        self.incluir_adotante_test(adotante)

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
        self.incluir_adotante_test(adotante)

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
        self.incluir_adotante_test(adotante)

    def test_incluir_adotante_should_throw_exception_when_data_nascimento_invalida(
        self,
    ):
        with patch("builtins.input", side_effect=self.adotante_data_nascimento_invalida):
            with self.assertRaises(TypeError):
                self.controlador_adotantes.incluir_adotante()

    def test_incluir_adotante_should_raise_exception_when_tipo_habitacao_invalido(
        self,
    ):
        with patch("builtins.input", side_effect=self.adotante_tipo_habitacao_invalido):
            with self.assertRaises(StopIteration):
                self.controlador_adotantes.incluir_adotante()

    def test_incluir_adotante_should_raise_exception_when_tamanho_habitacao_invalido(
        self,
    ):
        with patch("builtins.input", side_effect=self.adotante_tamanho_habitacao_invalido):
            with self.assertRaises(StopIteration):
                self.controlador_adotantes.incluir_adotante()

    def test_incluir_adotante_should_raise_exception_when_possui_animal_invalido(
        self,
    ):
        with patch("builtins.input", side_effect=self.adotante_possui_animal_invalido):
            with self.assertRaises(StopIteration):
                self.controlador_adotantes.incluir_adotante()

    def test_excluir_adotante_should_work_when_correct_data(self):
        self.incluir_adotante_test(self.adotante_valido)

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
        self.incluir_adotante_test(self.adotante_valido)

        with self.assertRaises(EntidadeNaoEncontradaException):
            sys.stdin = io.StringIO(self.cpf_invalido)
            self.controlador_adotantes.excluir_adotante()

    def test_alterar_adotante_should_work_when_correct_data(self):
        self.incluir_adotante_test(self.adotante_valido)

        dados_alteracao = [
            self.cpf,
            self.cpf_atualizado,
            self.nome_atualizado,
            self.data_nascimento_atualizada,
            self.tipo_habitacao_apartamento,
            self.tamanho_habitacao_grande,
            self.nao_possui_animal,
            self.logradouro_atualizado,
            self.numero_atualizado,
        ]

        with patch("builtins.input", side_effect=dados_alteracao):
            try:
                self.controlador_adotantes.alterar_adotante()
            except EntidadeNaoEncontradaException:
                self.fail(
                    "Ocorreu um erro ao alterar adotante! Entidade nao encontrada."
                )

        try:
            adotante_atualizado = self.controlador_adotantes.buscar_adotante_por_cpf(
                self.cpf_atualizado
            )
        except EntidadeNaoEncontradaException:
            self.fail("Adotante nao alterado.")

        self.assertEqual(dados_alteracao[1], adotante_atualizado.cpf)
        self.assertEqual(dados_alteracao[2], adotante_atualizado.nome)
        self.assertEqual(datetime.strptime(dados_alteracao[3], "%d/%m/%Y").date(),
                         adotante_atualizado.data_nascimento)
        self.assertEqual(dados_alteracao[4], adotante_atualizado.tipo_habitacao.value)
        self.assertEqual(dados_alteracao[5], adotante_atualizado.tamanho_habitacao.value)
        self.assertEqual(True if dados_alteracao[6] == 1 else False,
                         adotante_atualizado.possui_animal)
        self.assertEqual(dados_alteracao[7], adotante_atualizado.endereco.logradouro)
        self.assertEqual(dados_alteracao[8], adotante_atualizado.endereco.numero)

    def test_alterar_adotante_should_raise_exception_when_cpf_invalido(
        self,
    ):
        self.incluir_adotante_test(self.adotante_valido)

        with self.assertRaises(EntidadeNaoEncontradaException):
            sys.stdin = io.StringIO(self.cpf_invalido)
            self.controlador_adotantes.alterar_adotante()

    def test_alterar_adotante_should_throw_exception_when_data_nascimento_invalida(self):
        self.incluir_adotante_test(self.adotante_valido)

        with patch("builtins.input", side_effect=self.adotante_data_nascimento_invalida):
            with self.assertRaises(TypeError):
                self.controlador_adotantes.alterar_adotante()

    def test_alterar_adotante_should_throw_exception_when_tipo_habitacao_invalido(self):
        self.incluir_adotante_test(self.adotante_valido)

        with patch("builtins.input", side_effect=[self.cpf]+self.adotante_tipo_habitacao_invalido):
            with self.assertRaises(StopIteration):
                self.controlador_adotantes.alterar_adotante()

    def test_alterar_adotante_should_throw_exception_when_tamanho_habitacao_invalido(self):
        self.incluir_adotante_test(self.adotante_valido)

        with patch("builtins.input", side_effect=[self.cpf]+self.adotante_tamanho_habitacao_invalido):
            with self.assertRaises(StopIteration):
                self.controlador_adotantes.alterar_adotante()

    def test_alterar_adotante_should_throw_exception_when_possui_animal_invalido(self):
        self.incluir_adotante_test(self.adotante_valido)

        with patch("builtins.input", side_effect=[self.cpf]+self.adotante_possui_animal_invalido):
            with self.assertRaises(StopIteration):
                self.controlador_adotantes.alterar_adotante()
