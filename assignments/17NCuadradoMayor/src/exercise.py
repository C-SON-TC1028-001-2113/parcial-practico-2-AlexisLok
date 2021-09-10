

def main():
    numero = int(input("Escribe un numero : "))
    #escribe tu código abajo de esta línea
    ele = 1
    #Abajo se evalua la variable al cuadrado y se compara con el valor
    while ele**2 <= numero:
        ele += 1 #Si la variable al cuadrado es menor a numero, entonces se suma 1 y se vuelve a probar
    print (ele)

if __name__=='__main__':
    main()
