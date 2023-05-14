from datetime import datetime
from model import TIPO_CPF
from exceptions import OpcaoInvalidaException


class DoacaoView:
    def telar_opcoes(self):
        print("\n---------- DOACOES ----------")
        print("[1] -> Incluir Doacao")
        print("[2] -> Alterar Doacao")
        print("[3] -> Listar Doacoes")
        print("[4] -> Excluir Doacao")
        print("[5] -> Listar Doacao por id")
        print("[0] -> Retornar")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(0, 6):
            raise OpcaoInvalidaException()

        return opcao

    def telar_opcoes_identificador(self):
        print("BUSCAR POR:")
        print("\t[1] -> CPF")
        print("\t[2] -> N° chip")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(1, 3):
            raise OpcaoInvalidaException()

        return opcao

    def telar_opcoes_tipo_animal(self):
        print("TIPO DO ANIMAL QUE DESEJA DOAR:")
        print("\t[1] -> Cachorro")
        print("\t[2] -> Gato")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(1, 3):
            raise OpcaoInvalidaException()

        return opcao

    def pegar_dados_doacao(self):
        print("\n-------- DADOS DOACAO ----------")
        cpf_doador = input("CPF (doador): ")
        numero_chip = self.pegar_numero_chip()

        while True:
            try:
                data_doacao = input("Data de adocao (dd/mm/yyyy): ")
                data_doacao_convertida = datetime.strptime(
                    data_doacao, "%d/%m/%Y"
                ).date()
                break
            except ValueError:
                print("ERRO: Data em formato invalido! Tente novamente.")

        motivo = input("Motivo: ")

        return {
            "cpf_doador": cpf_doador,
            "numero_chip": numero_chip,
            "data": data_doacao_convertida,
            "motivo": motivo,
        }

    def pegar_numero_chip(self):
        while True:
            try:
                numero_chip = int(input("N° chip: "))
                return numero_chip
            except ValueError:
                print("Somente numeros. Tente novamente")

    def mostrar_doacao(self, dados_doacao: dict):
        print("\t - CPF DOADOR: ", dados_doacao["cpf_doador"])
        print("\t - N° CHIP ANIMAL: ", dados_doacao["numero_chip"])
        print("\t - DATA DE DOACAO: ", dados_doacao["data"].strftime("%d/%m/%Y"))
        print("\t - TERMO ASSINADO: ", dados_doacao["motivo"])

    def selecionar_doacao(self, tipo_id: int):
        if tipo_id == TIPO_CPF:
            identificador = input("CPF da doacao que deseja selecionar: ")
        else:
            while True:
                try:
                    identificador = int(input("N° Chip da doacao que deseja selecionar: "))
                    break
                except ValueError:
                    print("Somente numeros. Tente novamente")
        return identificador

    def mostrar_mensagem(self, msg: str):
        print(msg)
