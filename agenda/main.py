import menu
import banco


while true:
    op=menu.menu()

    if op==1:
        banco.inserir()
        
    
    elif op==2:
        banco.buscar()

    elif op==3:  
        banco.listar()

    elif op==4:
        banco.deletar()

    elif op==5:
        banco.finalizar()

    else:
        print("Digite uma opção válida!")