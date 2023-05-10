from model.vacina import Vacina


class HistoricoVacinacao:
    def __init__(self):
        self.__vacinas = []

    @property
    def vacinas(self):
        return self.__vacinas

    def add_vacina(self, vacina: Vacina):
        self.__vacinas.append(vacina)
