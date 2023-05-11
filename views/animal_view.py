from exceptions.opcao_invalida_exception import OpcaoInvalidaException


class AnimalView:
    def tela_opcoes(self):
        print("\n---------- ANIMAIS ----------")
        print("[1] -> Incluir Animal")
        print("[2] -> Alterar Animal")
        print("[3] -> Excluir Animal")
        print("[4] -> Listar Animais")
        print("[5] -> Buscar Animal por N° chip")
        print("[0] -> Retornar")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(0, 6):
            raise OpcaoInvalidaException()

        return opcao

    def tela_opcoes_tipo_animal(self):
        print("TIPO ANIMAL:")
        print("\t[1] - Cachorro")
        print("\t[2] - Gato")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(1, 3):
            raise OpcaoInvalidaException()

        return opcao

    def tela_opcoes_tamanho_cachorro(self):
        print("TAMANHO CACHORRO:")
        print("[1] - Pequeno")
        print("[2] - Medio")
        print("[3] - Grande")

        opcao = int(input("Escolha a opcao: "))
        if opcao not in range(1, 4):
            raise OpcaoInvalidaException()

        return opcao

    def pega_dados_animal(self):
        print("\n-------- DADOS ANIMAL ----------")
        numero_chip = input("N° chip: ")
        nome = input("Nome: ")

        dados_animal = {
            "numero_chip": numero_chip,
            "nome": nome,
        }

        while True:
            try:
                tipo_animal = self.tela_opcoes_tipo_animal()
                dados_animal["tipo_animal"] = tipo_animal
                break
            except OpcaoInvalidaException as e:
                print(e)
            except ValueError:
                print("Somente numeros. Tente novamente.")

        raca = input("Raca: ")
        dados_animal["raca"] = raca

        if tipo_animal == 1:
            while True:
                try:
                    tamanho_cachorro = self.tela_opcoes_tamanho_cachorro()
                    dados_animal["tamanho_cachorro"] = tamanho_cachorro
                    break
                except OpcaoInvalidaException as e:
                    print(e)
                except ValueError:
                    print("Somente numeros. Tente novamente.")

        return dados_animal

    def pega_dados_animal_alterar(self, tipo_animal: int):
        print("\n-------- DADOS ANIMAL ----------")
        numero_chip = input("N° chip: ")
        nome = input("Nome:")

        dados_animal = {
            "numero_chip": numero_chip,
            "nome": nome,
        }

        raca = input("Raca: ")
        dados_animal["raca"] = raca

        if tipo_animal == 1:
            while True:
                try:
                    tamanho_cachorro = self.tela_opcoes_tamanho_cachorro()
                    dados_animal["tamanho_cachorro"] = tamanho_cachorro
                except OpcaoInvalidaException as e:
                    print(e)
                except ValueError:
                    print("Somente numeros. Tente novamente.")

        return dados_animal

    def mostra_animal(self, dados_animal: dict):
        print(f"\t- N° CHIP: {dados_animal['numero_chip']}")
        print(f"\t- NOME: {dados_animal['nome']}")
        print(f"\t- RACA: {dados_animal['raca']}")

        if dados_animal["tipo_animal"] == 1:
            print(f"\t- TAMANHO CACHORRO: {dados_animal['tamanho_cachorro'].name}")

    def seleciona_animal(self):
        numero_chip = input("N° chip do animal que deseja selecionar: ")
        return numero_chip

    def mostra_mensagem(self, msg: str):
        print(msg)
