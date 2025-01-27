a = 1
value = input('Ingresa un valor por favor')
value = int(value)

while a == 1:
    for i in range(1,value+1):
        conta = 0
        for n in range(1, i+1):
            residue = i%n
            if residue == 0:
                conta = conta + 1
            
            ### print("i = ", i)
            ### print("n = ", n)
            ### print("residue = ", residue)
            ### print("conta = ", conta)

  
    if conta == 2:
       print(f'{i} es un primo')
       print("\n")
    else:
       print(f'{i} lastimosamente no es un primo')
       print("\n")

    print('Quieres continuar? Presiona 1 para hacerlo')
    a = input()
    a = int(a)

    if a != 1:
        break

    value = input('Ingresa un valor por favor')
    value = int(value)
