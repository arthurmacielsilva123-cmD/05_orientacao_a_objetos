class Pessoa:
    # construtor
    def __init__(self, nome, idade, genero, telefone):
        self._nome = nome
        self._idade = idade
        self._genero = genero
        self._telefone = telefone

    # métodos especiais
    def __str__(self):
        return f"Olá, meu nome é {self._nome}, tenho {self._idade} anos, sou do gênero {self._genero} e meu telefone é {self._telefone}."
    

    def __len__(self):
        return self.__idade





    # métodos set e get
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone
