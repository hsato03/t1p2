from datetime import datetime
from exceptions import OpcaoInvalidaException


class AdocaoView:
    def telar_opcoes(self):
        print("\n---------- ADOCOES ----------")
        print("[1] -> Incluir Adocao")
        print("[2] -> Alterar Adocao")
        print("[3] -> Listar Adocoes")
        print("[4] -> Excluir Adocao")
        print("[5] -> Listar Adocao por id")
        print("[6] -> Listar Animais disponiveis para adocao")
        print("[0] -> Retornar")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(0, 7):
            raise OpcaoInvalidaException()

        return opcao

    def telar_opcoes_termo(self):
        print("ASSINAR TERMO?")
        print("\t[1] - Sim")
        print("\t[2] - Nao")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(1, 3):
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
        print("TIPO DO ANIMAL:")
        print("\t[1] -> Cachorro")
        print("\t[2] -> Gato")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(1, 3):
            raise OpcaoInvalidaException()

        return opcao

    def pegar_dados_adocao(self):
        print("\n-------- DADOS ADOCAO ----------")
        cpf_adotante = input("CPF (adotante): ")
        numero_chip = self.pegar_numero_chip()

        while True:
            try:
                data_adocao = input("Data de adocao (dd/mm/yyyy): ")
                data_adocao_convertida = datetime.strptime(
                    data_adocao, "%d/%m/%Y"
                ).date()
                break
            except ValueError:
                print("ERRO: Data em formato invalido! Tente novamente.")

        while True:
            try:
                termo_assinado = self.telar_opcoes_termo()
                break
            except OpcaoInvalidaException as e:
                print(e)
            except ValueError:
                print("Somente numeros. Tente novamente.")

        return {
            "cpf_adotante": cpf_adotante,
            "numero_chip": numero_chip,
            "data": data_adocao_convertida,
            "termo_assinado": termo_assinado,
        }

    def pegar_numero_chip(self):
        while True:
            try:
                numero_chip = int(input("N° chip: "))
                return numero_chip
            except ValueError:
                print("Somente numeros. Tente novamente")

    def mostrar_adocao(self, dados_adocao: dict):
        print("\t - CPF ADOTANTE: ", dados_adocao["cpf_adotante"])
        print("\t - N° CHIP ANIMAL: ", dados_adocao["numero_chip"])
        print("\t - DATA DE ADOCAO: ", dados_adocao["data"].strftime("%d/%m/%Y"))
        print("\t - TERMO ASSINADO: ", dados_adocao["termo_assinado"])

    def selecionar_adocao(self, tipo_id: int):
        if tipo_id == 1:
            identificador = input("CPF da adocao que deseja selecionar: ")
        else:
            while True:
                try:
                    identificador = int(
                        input("N° Chip da doacao que deseja selecionar: ")
                    )
                    break
                except ValueError:
                    print("Somente numeros. Tente novamente")
        return identificador

    def mostrar_mensagem(self, msg: str):
        print(msg)
