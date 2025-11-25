class Aluno:
    def __init__(self, nome, matricula, media):
        self.__nome = nome
        self.__matricula = matricula
        self.__media = media

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_media(self):
        return self.__media

    def esta_aprovado(self):
        if self.__media >= 7:
            print(f"O aluno {self.__nome} está APROVADO.")
        else:
            print(f"O aluno {self.__nome} está REPROVADO.")