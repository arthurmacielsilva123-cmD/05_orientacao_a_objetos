from classes import pessoa

def main():
    usuario = pessoa(nome="", cpf="")

    usuario.nome = input("informe seu nome: ").strip().title()
    usuario.cpf = input("informe seu cpf: ").strip()


    print(f"nome: {usuario.nome}")
    print(f"cpf: {usuario.cpf}")

if __name__ == "__main__":
    main()