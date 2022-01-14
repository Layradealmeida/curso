'''Crie um programa em Python que calcule as raizes reais de uma equação do segundo grau.
Ax^2 +Bx + C = 0
x1 e x2'''
import math

def bhaskarapos(a,b,c):

    x1 = (-b+math.sqrt((b**2) - (4*a*c)))/(2*a)

    return x1

def bhaskaraneg(a,b,c):
    x2 = (-b-math.sqrt((b**2) - (4*a*c)))/(2*a)

    return x2



    