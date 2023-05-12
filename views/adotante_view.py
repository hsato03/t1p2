from exceptions.opcao_invalida_exception import OpcaoInvalidaException
from datetime import datetime


class AdotanteView:
    def tela_opcoes(self):
        print("\n---------- ADOTANTES ----------")
        print("[1] -> Incluir Adotante")
        print("[2] -> Alterar Adotante")
        print("[3] -> Listar Adotantes")
        print("[4] -> Excluir Adotante")
        print("[5] -> Buscar Adotante por CPF")
        print("[0] -> Retornar")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(0, 6):
            raise OpcaoInvalidaException()

        return opcao

    def tela_opcoes_tipo_habitacao(self):
        print("TIPO HABITACAO:")
        print("\t[1] -> Casa")
        print("\t[2] -> Apartamento")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(1, 3):
            raise OpcaoInvalidaException()

        return opcao

    def tela_opcoes_tamanho_habitacao(self):
        print("TAMANHO HABITACAO:")
        print("\t[1] -> Pequeno")
        print("\t[2] -> Medio")
        print("\t[3] -> Grande")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(1, 4):
            raise OpcaoInvalidaException()

        return opcao

    def tela_opcoes_possui_animal(self):
        print("POSSUI ANIMAL:")
        print("\t[1] -> Sim")
        print("\t[2] -> Nao")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(1, 3):
            raise OpcaoInvalidaException()

        return opcao

    def pega_dados_adotante(self):
        tipo_habitacao, tamanho_habitacao, possui_animal = (
            None,
            None,
            None,
        )
        print("\n-------- DADOS ADOTANTE ----------")
        cpf = input("CPF: ")
        nome = input("Nome: ")
        while True:
            try:
                data_nascimento = input("Data de nascimento (dd/mm/yyyy): ")
                data_nascimento_convertida = datetime.strptime(
                    data_nascimento, "%d/%m/%Y"
                ).date()
                break
            except ValueError:
                print("ERRO: Data em formato invalido! Tente novamente.")
        while True:
            try:
                tipo_habitacao = (
                    self.tela_opcoes_tipo_habitacao()
                    if tipo_habitacao is None
                    else tipo_habitacao
                )
                tamanho_habitacao = (
                    self.tela_opcoes_tamanho_habitacao()
                    if tamanho_habitacao is None
                    else tamanho_habitacao
                )
                possui_animal = (
                    self.tela_opcoes_possui_animal()
                    if possui_animal is None
                    else possui_animal
                )
                break
            except OpcaoInvalidaException as e:
                print(e)
            except ValueError:
                print("Somente numeros. Tente novamente.")

        print("DADOS ENDERECO:")
        logradouro = input("\tLogradouro: ")
        numero = input("\tNumero: ")

        return {
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nascimento_convertida,
            "tipo_habitacao": tipo_habitacao,
            "tamanho_habitacao": tamanho_habitacao,
            "possui_animal": possui_animal,
            "logradouro": logradouro,
            "numero": numero,
        }

    def mostra_adotante(self, dados_adotante: dict):
        print("\t- CPF:", dados_adotante["cpf"])
        print("\t- NOME:", dados_adotante["nome"])
        print("\t- DATA DE NASCIMENTO:", dados_adotante["data_nascimento"])
        print("\t- TIPO DE HABITACAO:", dados_adotante["tipo_habitacao"].name)
        print(
            "\t- TAMANHO DE HABITACAO:",
            dados_adotante["tamanho_habitacao"].name,
        )
        print("\t- POSSUI ANIMAL:", dados_adotante["possui_animal"])
        print(f"\t- ENDERECO: {dados_adotante['endereco']}\n")

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_adotante(self):
        cpf = input("CPF do adotante que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg: str):
        print(msg)
