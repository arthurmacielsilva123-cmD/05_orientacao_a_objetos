# classes
class Pessoa:
    def __init__(self, email, telefone):
        self.email = email
        self.telefone = telefone
    

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, idade, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        super().__init__(email=email, telefone=telefone)

        
    def exibir_dados(self):
        print(f"Nome: {self.Nome}")
        print(f"CPF: {self.cpf}")
        print(f"Idade: {self.Idade}")
        super().exibir_dados()


class PessoaJuridica(Pessoa):
    def __init__(self, nome_fantasia, cnpj, email, telefone):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(email=email, telefone=telefone)

    def exibir_dados(sefl):
        print(f"Nome da empresa:{sefl.nome_fantasia}")
        print(f" CNPJ:{sefl.cnpj}")
        super().exibir_dados()

