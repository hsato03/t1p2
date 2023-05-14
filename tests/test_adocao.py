import unittest
from unittest.mock import patch, Mock
from controllers import AdocaoController
from model import TIPO_CACHORRO, TIPO_GATO, TIPO_CPF, TIPO_N_CHIP
from exceptions import EntidadeNaoEncontradaException


class TestAdocao(unittest.TestCase):
    def setUp(self):
        def buscar_adotante_mock(cpf):
            if cpf == "1" or cpf == "2":
                return self.adotante
            else:
                raise EntidadeNaoEncontradaException("Adotante nao encontrado")

        def buscar_animal_mock(numero_chip):
            if numero_chip == "1" or numero_chip == "2":
                return self.animal
            else:
                raise EntidadeNaoEncontradaException("Animal nao encontrado")

        def buscar_adocao_por_identificador_mock(identificador, tipo_id):
            if tipo_id == TIPO_CPF:
                if identificador == "1" or identificador == "2":
                    return (
                        self.adocao
                        if identificador == "1"
                        else self.adocao_atualizada
                    )
                else:
                    raise EntidadeNaoEncontradaException("Entidade nao encontrada")
            else:
                if identificador == "1" or identificador == "2":
                    return (
                        self.adocao
                        if identificador == "1"
                        else self.adocao_atualizada
                    )
                else:
                    raise EntidadeNaoEncontradaException("Entidade nao encontrada")

        self.controlador_sistema = Mock()
        self.controlador_sistema.controlador_animais = Mock()
        self.controlador_sistema.controlador_adotantes = Mock()

        self.controlador_adocoes = Mock()

        self.adotante = Mock()
        self.adotante.cpf = "1"

        self.adotante_atualizado = Mock()
        self.adotante_atualizado.cpf = "2"

        self.animal = Mock()
        self.animal.numero_chip = "1"

        self.animal_atualizado = Mock()
        self.animal_atualizado.cpf = "2"

        self.controlador_adocoes.buscar_adocao_por_identificador.side_effect = (
            buscar_adocao_por_identificador_mock
        )
        self.controlador_sistema.controlador_adotantes.buscar_adotante_por_cpf.side_effect = (
            buscar_adotante_mock
        )
        self.controlador_sistema.controlador_animais.buscar_cachorro_por_numero_chip.side_effect = (
            buscar_animal_mock
        )
        self.controlador_sistema.controlador_animais.buscar_gato_por_numero_chip.side_effect = (
            buscar_animal_mock
        )

        self.assinar_termo = 1
        self.nao_assinar_termo = 2
        self.assinar_termo_invalido = 3
        self.identificador_invalido = "100"

        self.adocao = Mock()
        self.adocao.adotante = self.adotante
        self.adocao.animal = self.animal
        self.termo_assinado = self.assinar_termo

        self.adocao_atualizada = Mock()
        self.adocao_atualizada.adotante = self.adotante_atualizado
        self.adocao_atualizada.animal = self.animal_atualizado
        self.termo_assinado = self.nao_assinar_termo

        self.adocao_valida = [
            TIPO_CACHORRO,
            self.adotante.cpf,
            self.animal.numero_chip,
            self.assinar_termo,
        ]
        self.adocao_valida_atualizada = [
            TIPO_CACHORRO,
            self.adotante_atualizado,
            self.animal_atualizado,
            self.nao_assinar_termo,
        ]
        self.adocao_cpf_invalido = [
            TIPO_CACHORRO,
            self.identificador_invalido,
            self.animal.numero_chip,
            self.assinar_termo,
        ]
        self.adocao_assinar_termo_invalido = [
            TIPO_CACHORRO,
            self.adotante.cpf,
            self.animal.numero_chip,
            self.assinar_termo_invalido,
        ]
        self.adocao_numero_chip_invalido = [
            TIPO_CACHORRO,
            self.adotante.cpf,
            self.identificador_invalido,
            self.assinar_termo,
        ]

    def incluir_adocao_test(self, dados_adocao):
        with patch("builtins.input", side_effect=dados_adocao):
            try:
                self.controlador_adocoes.incluir_adocao()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir Adocao.")

    def test_incluir_adocao_should_work_when_valid_data_1(self):
        self.incluir_adocao_test(self.adocao_valida)

    def test_incluir_adocao_should_work_when_valid_data_2(self):
        dados_adocao = [
            TIPO_GATO,
            self.adotante.cpf,
            self.animal.numero_chip,
            self.nao_assinar_termo,
        ]
        self.incluir_adocao_test(dados_adocao)

    def test_incluir_adocao_should_throw_exception_when_cpf_invalido(self):
        with patch("builtins.input", side_effect=self.adocao_cpf_invalido):
            with self.assertRaises(EntidadeNaoEncontradaException):
                self.controlador_adocoes.incluir_adocao()

    def test_incluir_adocao_should_throw_exception_when_numero_chip_invalido(self):
        with patch("builtins.input", side_effect=self.adocao_numero_chip_invalido):
            with self.assertRaises(EntidadeNaoEncontradaException):
                self.controlador_adocoes.incluir_adocao()

    def test_incluir_adocao_should_throw_exception_when_assinar_termo_invalido(self):
        with patch("builtins.input", side_effect=self.adocao_assinar_termo_invalido):
            with self.assertRaises(StopIteration):
                self.controlador_adocoes.incluir_adocao()

    # TODO: alterar e excluir
    def test_alterar_adocao_should_work_when_valid_data(self):
        self.incluir_adocao_test(self.adocao_valida)

        with patch("builtins.input", side_effect=self.adocao_valida_atualizada):
            try:
                self.controlador_adocoes.alterar_adocao()
            except EntidadeNaoEncontradaException:
                self.fail("Ocorreu um erro ao alterar Adocao! Entidade nao encontrada")

        try:
            adoacao_atualizada = (
                self.controlador_adocoes.buscar_adocao_por_identificador(
                    self.adotante_atualizado.cpf, TIPO_CPF
                )
            )
        except EntidadeNaoEncontradaException:
            self.fail("Doador nao alterado.")

        self.assertEqual(self.adocao_valida_atualizada[1].cpf, adoacao_atualizada.adotante.cpf)
        self.assertEqual(self.adocao_valida_atualizada[2].numero_chip, adoacao_atualizada.animal.numero_chip)
        self.assertEqual(self.adocao_atualizada.termo_assinado, adoacao_atualizada.termo_assinado)
