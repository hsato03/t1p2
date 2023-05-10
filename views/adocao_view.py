from datetime import date
from controllers.adotante_controller import AdotanteController


class AdocaoView:
    def tela_opcoes(self):
        print("\n---------- ADOCOES ----------")
        print("[1] -> Incluir Adocao")
        print("[2] -> Alterar Adocao")
        print("[3] -> Listar Adocoes")
        print("[4] -> Excluir Adocao")
        print("[0] -> Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def tela_opcoes_termo(self):
        print("ASSINAR TERMO?")
        print("\t[1] -> Sim")
        print("\t[2] -> Nao")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_adocao(self):
        print("\n-------- DADOS ADOCAO ----------")
        cpf_adotante = input("CPF (adotante): ")
        chip_animal = input("N° Chip (animal): ")
        data = date.today()
        termo_assinado = self.tela_opcoes_termo()

        return {
            "cpf_adotante": cpf_adotante,
            "chip_animal": chip_animal,
            "data": data,
            "termo_assinado": termo_assinado
        }

    def mostra_adocao(self, dados_adocao: dict):
        print("\t - CPF ADOTANTE: ", dados_adocao["cpf_adotante"])
        print("\t - N° CHIP ANIMAL: ", dados_adocao["numero_chip"])
        print("\t - DATA DE ADOCAO: ", dados_adocao["data"])
        print("\t - TERMO ASSINADO: ", dados_adocao["termo_assinado"])

    def seleciona_adocao(self):
        id = input("CPF/N° Chip da adocao que deseja selecionar: ")
        return id

    def mostra_mensagem(self, msg: str):
        print(msg)
