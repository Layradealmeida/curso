import funcao

a =int(input("digite o valor de a:"))
b =int(input("digite o valor de b:"))
c =int(input("digite o valor de c:"))

print(f'A função definida é {a}x^2+{b}x+{c}')

delta=(b**2) - (4*a*c)

if delta>=0:
    print(" os valores são:",funcao.bhaskarapos(a,b,c))
    print(" os valores são:",funcao.bhaskaraneg(a,b,c))

else:
    print("Delta inválido!")
  