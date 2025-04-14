class Filme:
    def __init__(self, nome, ano , duracao, imdb):
        self.__nome = nome
        self.ano = ano
        self.duracao = duracao
        self.imdb = imdb
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes
    
    def def_likes():
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    
    @property
    def imdb(self):
        return self.__imdb

    @nome.setter
    def nome(self, nome):
        self.__nome = nome