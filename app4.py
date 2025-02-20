#4o exercício

x = float(input("Forneça a coordenada x: "))
y = float(input("Forneça a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto se encontra no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto se encontra no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto se encontra no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto se encontra no quarto quadrante.")
else:
    print("O ponto está localizado no eixo ou origem.")
