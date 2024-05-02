import sys
if len(sys.argv)==3:
    fila=int(sys.argv[1])
    columna=int(sys.argv[2])
    if fila>0 and fila<10 and columna>0 and columna<10:
        for iF in range(fila):
            for iC in range(columna):
                print("*", end="")
            print()
    else:
        print("Error, introduce dos valores entre 1 y 9")
else:
    print("Error, introduce dos valores entre 1 y 9")