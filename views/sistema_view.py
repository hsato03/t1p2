from exceptions.opcao_invalida_exception import OpcaoInvalidaException


class SistemaView:
    def tela_opcoes(self):
        print("---------- MENU PRINCIPAL ----------")
        print("[1] -> Adotantes")
        print("[2] -> Adocoes")
        print("[0] -> Finalizar sistema")
        opcao = int(input("Escolha a opcao: "))

        if opcao not in range(0, 3):
            raise OpcaoInvalidaException()

        return opcao
