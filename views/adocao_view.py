from datetime import date
from exceptions import OpcaoInvalidaException


class AdocaoView:
    def telar_opcoes(self):
        print("\n---------- ADOCOES ----------")
        print("[1] -> Incluir Adocao")
        print("[2] -> Alterar Adocao")
        print("[3] -> Excluir Adocao")
        print("[4] -> Listar Adocoes")
        print("[5] -> Listar Adocao por id")
        print("[0] -> Retornar")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(0, 6):
            raise OpcaoInvalidaException()

        return opcao

    def telar_opcoe_termo(self):
        print("ASSINAR TERMO?")
        print("\t[1] - Sim")
        print("\t[2] - Nao")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def telar_opcoes_identificador(self):
        print("BUSCAR POR:")
        print("\t[1] -> CPF")
        print("\t[2] -> N° chip")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(1, 3):
            raise OpcaoInvalidaException()

        return opcao

    def pegar_dados_adocao(self):
        print("\n-------- DADOS ADOCAO ----------")
        cpf_adotante = input("CPF (adotante): ")
        numero_chip = input("N° Chip (animal): ")
        data = date.today()

        while True:
            try:
                termo_assinado = self.telar_opcoe_termo()
                break
            except OpcaoInvalidaException as e:
                print(e)
            except ValueError:
                print("Somente numeros. Tente novamente.")

        return {
            "cpf_adotante": cpf_adotante,
            "numero_chip": numero_chip,
            "data": data,
            "termo_assinado": termo_assinado,
        }

    def mostrar_adocao(self, dados_adocao: dict):
        print("\t - CPF ADOTANTE: ", dados_adocao["cpf_adotante"])
        print("\t - N° CHIP ANIMAL: ", dados_adocao["numero_chip"])
        print("\t - DATA DE ADOCAO: ", dados_adocao["data"])
        print("\t - TERMO ASSINADO: ", dados_adocao["termo_assinado"])

    def selecionar_adocao(self, tipo_id: int):
        if tipo_id == 1:
            id = input("CPF da adocao que deseja selecionar: ")
        else:
            id = input("N° Chip da adocao que deseja selecionar: ")
        return id

    def mostrar_mensagem(self, msg: str):
        print(msg)
