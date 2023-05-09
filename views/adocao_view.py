from datetime import date


class AdocaoView:
    def tela_opcoes(self):
        print("---------- ADOCOES ----------")
        print("[1] -> Incluir Adocao")
        print("[2] -> Alterar Adocao")
        print("[3] -> Listar Adocoes")
        print("[4] -> Excluir Adocao")
        print("[0] -> Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def tela_opcoes_termo(self):
        print("ASSINAR TERMO?")
        print("[1] -> Sim")
        print("[2] -> Nao")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_adocao(self):
        print("-------- DADOS ADOCAO ----------")
        cpf_adotante = input("CPF (adotante): ")
        chip_animal = input("N° Chip (animal): ")
        data = date.today()
        termo_assinado = True if self.tela_opcoes_termo() == 1 else False

        return {
            "cpf_adotante": cpf_adotante,
            "chip_animal": chip_animal,
            "data": data,
            "termo_assinado": termo_assinado
        }
