class Livro:
    def __init__(self, titulo, autor, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor  

    def get_ano(self):
        return self.__ano 
