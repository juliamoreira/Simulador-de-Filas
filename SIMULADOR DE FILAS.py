fila1 = []
fila2 = []
fila3 = []
senha = 1
rodando = True

def mostrar_filas():        # mostrar as filas
    print("Fila dos idosos:", fila1)
    print("Fila das gravidas:", fila2)
    print("Fila comum: ", fila3)
    
def prox_numero_fila():         # remover da fila
    if len(fila1) > 0:
        return fila1.pop(0)
    elif len(fila2) > 0:
        return fila2.pop(0)
    elif len(fila3) > 0: 
        return fila3.pop(0)
    
# mostrar menu
print ("1 - Mostrar filas")
print ("2 - Retirar senha para fila preferencial a idosos.")
print ("3 - Retirar senha para fila preferencial a gestantes. ")
print ("4 - Retirar senha para fila sem preferências. ")
print ("5 - Próximo numero da fila. ")
print ("6 - Sair ")

while rodando == True :
    option = int(input("Digite uma opcao: "))
    # inserir em uma fila
    if option == 1: 
        mostrar_filas()
    elif option == 2:
        fila1.append(senha)
    elif option == 3: 
        fila2.append(senha)
    elif option ==4:
        fila3.append(senha)
    elif option == 5:
        prox_numero_fila()
    elif option == 6:
        rodando = False
    senha += 1
        

    

