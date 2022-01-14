'''3 - Faça uma função que receba uma lista, percorra a lista e some os números pares dessa 
lista e retorne a soma. 
Imprimir a lista e o resultado da soma ao final do código.'''

lista = [1,2,3,2,1,2,3,4,5,6,5,4,3,2,1,8,10,12]

def soma(lista):
    cont=0
    for i in lista:
        if i%2==0:
            cont=cont+1
        

    return cont


print(lista)

result=soma(lista)

print("A quantidade de numeros pares é:", result)
