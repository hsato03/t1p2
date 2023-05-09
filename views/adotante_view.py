class AdotanteView:
    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- ADOTANTES ----------")
        print("Escolha a opcao")
        print("1 - Incluir Adotante")
        print("2 - Alterar Adotante")
        print("3 - Listar Adotantes")
        print("4 - Excluir Adotante")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def tela_opcoes_tipo_habitacao(self):
        print("\t-------- TIPOS HABITACAO ----------")
        print("\t[1] - Casa")
        print("\t[2] - Apartamento")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def tela_opcoes_tamanho_habitacao(self):
        print("\t-------- TAMANHOS HABITACAO ----------")
        print("\t[1] - Pequeno")
        print("\t[2] - Medio")
        print("\t[3] - Grande")

        opcao = int(input("Escolha a opçao: "))
        return opcao

    def tela_opcoes_possui_animal(self):
        print("\t-------- POSSUI ANIMAL ----------")
        print("\t[1] - Sim")
        print("\t[2] - Nao")

        opcao = int(input("Escolha a opçao: "))
        return opcao

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def pega_dados_adotante(self):
        print("-------- DADOS ADOTANTE ----------")
        cpf = input("CPF: ")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        tipo_habitacao = self.tela_opcoes_tipo_habitacao()
        tamanho_habitacao = self.tela_opcoes_tamanho_habitacao()
        possui_animal = self.tela_opcoes_possui_animal()
        print("\t------ DADOS ENDERECO --------")
        logradouro = input("\tLogradouro: ")
        numero = input("\tNúmero: ")

        return {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "tipo_habitacao": tipo_habitacao,
            "tamanho_habitacao": tamanho_habitacao,
            "possui_animal": possui_animal,
            "logradouro": logradouro,
            "numero": numero,
        }

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def mostra_adotante(self, dados_adotante):
        print("#" * 70)
        print("\t- CPF DO ADOTANTE:", dados_adotante["cpf"])
        print("\t- NOME DO ADOTANTE:", dados_adotante["nome"])
        print("\t- DATA DE NASCIMENTO DO ADOTANTE:", dados_adotante["data_nascimento"])
        print(
            "\t- TIPO DE HABITACAO DO ADOTANTE:", dados_adotante["tipo_habitacao"].name
        )
        print(
            "\t- TAMANHO DE HABITACAO DO ADOTANTE:",
            dados_adotante["tamanho_habitacao"].name,
        )
        print("\t- POSSUI ANIMAL:", dados_adotante["possui_animal"])
        print(f"\t- ENDERECO: {dados_adotante['endereco']}\n")

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def seleciona_adotante(self):
        cpf = input("CPF do adotante que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
