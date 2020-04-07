class Pessoa:
    def __init__(self, *filhos , nome=None, idade=35 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    dean = Pessoa(nome='dean')
    jackson = Pessoa(dean, nome='Jackson')
    print(Pessoa.comprimentar(jackson))
    print(id(jackson))
    print(jackson.comprimentar())
    print(jackson.nome)
    print(jackson.idade)
    for filho in jackson.filhos:
        print(filho.nome)



