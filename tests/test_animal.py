import unittest
from unittest.mock import patch
from controllers import AnimalController


class AnimalTest(unittest.TestCase):
    # TODO: Refatorar input com variaveis no setUp
    def setUp(self):
        self.controlador_animais = AnimalController(None)

    def test_incluir_cachorro_pequeno_should_work_when_correct_data(self):
        cachorro = ["1", "zezim", "1", "vira-lata", "1"]
        with patch("builtins.input", side_effect=cachorro):
            try:
                self.controlador_animais.incluir_animal()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir cachorro pequeno!")

    def test_incluir_cachorro_medio_should_work_when_correct_data(self):
        cachorro = ["1", "zezim", "1", "vira-lata", "2"]
        with patch("builtins.input", side_effect=cachorro):
            try:
                self.controlador_animais.incluir_animal()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir cachorro médio!")

    def test_incluir_cachorro_grande_should_work_when_correct_data(self):
        cachorro = ["1", "zezim", "1", "vira-lata", "3"]
        with patch("builtins.input", side_effect=cachorro):
            try:
                self.controlador_animais.incluir_animal()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir cachorro grande!")

    def test_incluir_cachorro_should_raise_exception_when_incorrect_tamanho_cachorro(self):
        cachorro = ["1", "zezim", "1", "vira-lata", "100"]
        with patch("builtins.input", side_effect=cachorro):
            with self.assertRaises(StopIteration):
                self.controlador_animais.incluir_animal()

    def test_incluir_gato_should_work_when_correct_data(self):
        gato = ["1", "miau", "2", "persa"]
        with patch("builtins.input", side_effect=gato):
            try:
                self.controlador_animais.incluir_animal()
            except StopIteration:
                self.fail("Ocorreu um erro ao incluir gato!")

    def test_incluir_animal_should_raise_exception_when_incorrect_tipo_animal(self):
        cachorro = ["1", "zezim", "100"]
        with patch("builtins.input", side_effect=cachorro):
            with self.assertRaises(StopIteration):
                self.controlador_animais.incluir_animal()

    # TODO: Excluir e alterar animal
