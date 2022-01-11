def soma(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2
    
# Entrada
print("Escolha quan opeção deseja realizar: ")
opcao = input("+, -, /, x:")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == "+":
    valor_soma = soma(num1, num2)
    print(f"{num1} + {num2} == {valor_soma}")

elif opcao == "-":
    valor_sub = sub(num1, num2)
    print(f"{num1} - {num2} == {valor_sub}")

elif opcao == "x":
    valor_mult = mult(num1, num2)
    print(f"{num1} x {num2} == {valor_mult}")

elif opcao == "/":
    valor_div = div(num1, num2)
    print(f"{num1} / {num2} == {valor_div}")