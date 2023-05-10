from exceptions.opcao_invalida_exception import OpcaoInvalidaException


class SistemaView:
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("---------- MENU PRINCIPAL ----------")
        print("[1] -> Adotantes")
        print("[0] -> Finalizar sistema")
        opcao = int(input("Escolha a opcao: "))

        if opcao not in range(0, 2):
            raise OpcaoInvalidaException()

        return opcao
