'''1 - Crie um programa que peça o ano de nascimento e calcule a idade e verifique SE a pessoa é maior de idade.
MAIOR DE IDADE: idade >= 18
MENOR DE IDADE: < 18
Saída: 
Imprimir a idade
Imprimir a mensagem dizendo se é maior ou menor de idade'''

ano =int(input('Qual o ano de nascimento?')) 

idade = 2022- ano

if idade >= 18:
    print("A idade é:", idade)
    print("Maior de idade")

  
if idade <	18:
    print("A idade é:", idade)
    print("Menor de idade")


print('FIM')