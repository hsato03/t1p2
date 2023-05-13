from exceptions import OpcaoInvalidaException
from datetime import datetime


class DoadorView:
    def telar_opcoes(self):
        print("\n---------- DOADORES ----------")
        print("[1] -> Incluir Doador")
        print("[2] -> Alterar Doador")
        print("[3] -> Listar Doadores")
        print("[4] -> Excluir Doador")
        print("[5] -> Buscar Doador por CPF")
        print("[0] -> Retornar")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(0, 6):
            raise OpcaoInvalidaException()

        return opcao

    def pegar_dados_doador(self):
        print("\n-------- DADOS DOADOR ----------")
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

        print("DADOS ENDERECO:")
        logradouro = input("\tLogradouro: ")
        numero = input("\tNumero: ")

        return {
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nascimento_convertida,
            "logradouro": logradouro,
            "numero": numero,
        }

    def mostrar_doador(self, dados_doador: dict):
        print("\t- CPF:", dados_doador["cpf"])
        print("\t- NOME:", dados_doador["nome"])
        print("\t- DATA DE NASCIMENTO:", dados_doador["data_nascimento"].strftime('%d/%m/%Y'))
        print(f"\t- ENDERECO: {dados_doador['endereco']}\n")

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def selecionar_doador(self):
        cpf = input("CPF do doador que deseja selecionar: ")
        return cpf

    def mostrar_mensagem(self, msg: str):
        print(msg)
