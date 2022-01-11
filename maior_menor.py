'''Faça um programa que, dado um conjunto de N números, 
determine o menor valor, o maior valor e a soma dos valores.'''



lista=[6,10,5,8]
print('lista:',lista)

lista.sort()

print("O maior é:",lista[-1])
print("O menor é:",lista[0]) 
print('A soma dos valores é:', lista[-1]+lista[0])