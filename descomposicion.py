import sys
cade=str(sys.argv[1])
if len(sys.argv) == 2 and int(sys.argv[1]) > 0:
    for conta in range(len(sys.argv[1])):
        num=int(cade[-conta-1])*10**conta
        print("{:0{}d}".format(num,len(sys.argv[1])))
else:
    print("Numero invalido, ingresa un numero entero mayor a 0")
    print("Ejemplo: descomposicion.py [0-9999]")