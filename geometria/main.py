import geometria


op=int(input("1- area quad 2-area cir:"))

if op==1:

    medida = float(input("Digite a medida:"))
    area_quad = geometria.area_quad(medida)

    print("area quadrado:", area_quad)

elif op==2:

    medida = float(input("Digite a medida:"))
    area_cir = geometria.area_cir(medida)

    print("area quadrado:", area_cir)


