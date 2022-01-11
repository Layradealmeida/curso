
'''1 - Faça um programa que leia um nome de usuário e a sua senha e 
não aceite a senha igual ao nome do usuário, mostrando uma mensagem 
de erro e voltando a pedir as informações.'''

while True:
    nome = (input("Digite o seu nome de usuario: "))
    senha = (input("Digite sua senha: "))
    if nome!= senha:
        print("Parabéns, a senha é válida! ")
        break
    else:
         print("Continue tentando, insira nome e senha diferentes!")