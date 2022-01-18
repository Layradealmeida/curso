class Pessoa:

    def __init__(self, id, nome, idade, cidade, genero):
        self.id= id
        self.nome=nome
        self.idade=idade
        self.cidade=cidade
        self.genero=genero

    def __str__(self):
        return f'Pessoa com nome:{self.nome}|{self.id}, {self.idade},{self.cidade},{self.genero}'


    def comer(self, alimento):
        print(f"{self.nome} está comendo {alimento}")

    
    def estudar(self, conteudo):
        print(f"{self.nome} está estudando {conteudo}")


    def dormir(self):
        print(f"{self.nome} está dormindo")


    def jogar(self, jogo):
        print(f"{self.nome} está jogando {jogo}")


id = input("Digite o CPF:")
nome = input("Digite o nome:")
idade = input("Digite a idade:")
cidade = input("Digite a cidade:")
genero = input("Digite o gênero:")

pessoa=Pessoa(id, nome, idade, cidade, genero)


print(pessoa)
pessoa.comer("maçã")
pessoa.estudar("python")
pessoa.dormir()
pessoa.jogar("xadrez")
