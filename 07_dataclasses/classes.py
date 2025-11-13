from dataclasses import dataclass

# classes
@dataclass
class Pessoa:
    # atributos
    nome: str
    idade: int
    altura: float


    def __str__(self):
        return f"nome: {self.nome}\nIdade: {len(self)}\nAltura: {self.altura}"

    def __len__(self):
        return self.idade
    
    def verificar_maioridade():
        return "È maior de idade" if len() >= 18 else "não é maior de idade "