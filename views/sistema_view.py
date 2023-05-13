from exceptions import OpcaoInvalidaException


class SistemaView:
    def tela_opcoes(self):
        print("\n---------- MENU PRINCIPAL ----------")
        print("[1] -> Adotantes")
        print("[2] -> Adocoes")
        print("[3] -> Animais")
        print("[0] -> Finalizar sistema")
        opcao = int(input("Escolha a opcao: "))

        if opcao not in range(0, 4):
            raise OpcaoInvalidaException()

        return opcao
