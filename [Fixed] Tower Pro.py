c=''
while True:
    layernum=input("Please type in the number of layer: ")
    layernum=int(layernum)
    if c == 'x':
        layernum=100*layernum
    layernumtemp=layernum

    A=[]
    TempA=[]
    while layernumtemp>0:
        for i in range(layernum-layernumtemp+1):
            TempA.append(' ')
        for i in range(layernumtemp*2-1):
            TempA.append('*')
        for i in range(layernum-layernumtemp+1):
            TempA.append(' ')
        A.append(''.join(TempA))
        TempA =[]
        layernumtemp=layernumtemp-1

    M=[]
    TempM=[]
    for i in range(layernum):
        TempM.append(' ')
    TempM.append('|')
    for i in range(layernum):
        TempM.append(' ')
    JoinM=''.join(TempM)
    for i in range(layernum):
        M.append(JoinM)
    B=[]
    C=[]

    Table=[]
    for i in range(layernum*6+3):
        Table.append('=')
    Platform=''.join(Table)

    p=layernum-1
    while p>-1:
        print(A[p],M[p],M[p],sep = '')
        p=p-1

    print(Platform)
    
    ###
    #A = ['*********',' ******* ','  *****  ','   ***   ','    *    ']
    #B = ['    |    ','    |    ','    |    ','    |    ','    |    ']
    #C = ['    |    ','    |    ','    |    ','    |    ','    |    ']

    #print(A[len(A)-1],B[len(B)-1],C[len(C)-1],sep = '')
    #print(A[len(A)-2],B[len(B)-2],C[len(C)-2],sep = '')
    #print(A[len(A)-3],B[len(B)-3],C[len(C)-3],sep = '')
    #print(A[len(A)-4],B[len(B)-4],C[len(C)-4],sep = '')
    #print(A[len(A)-5],B[len(B)-5],C[len(C)-5],sep = '')
    #print('===========================')

    #layernum = 5
            
    def move(n, source, target, auxiliary):
        if n > 0:
            
            move(n-1, source, auxiliary, target)
            target.append(source.pop())

            ####################

            #AX=['    |    ','    |    ','    |    ','    |    ','    |    ']
            #BX=['    |    ','    |    ','    |    ','    |    ','    |    ']
            #CX=['    |    ','    |    ','    |    ','    |    ','    |    ']

            AX=[]
            TempM=[]
            for i in range(layernum):
                TempM.append(' ')
            TempM.append('|')
            for i in range(layernum):
                TempM.append(' ')
            JoinM=''.join(TempM)
            for i in range(layernum):
                AX.append(JoinM)

            BX=[]
            TempM=[]
            for i in range(layernum):
                TempM.append(' ')
            TempM.append('|')
            for i in range(layernum):
                TempM.append(' ')
            JoinM=''.join(TempM)
            for i in range(layernum):
                BX.append(JoinM)

            CX=[]
            TempM=[]
            for i in range(layernum):
                TempM.append(' ')
            TempM.append('|')
            for i in range(layernum):
                TempM.append(' ')
            JoinM=''.join(TempM)
            for i in range(layernum):
                CX.append(JoinM)
            
            ALen=len(A)-1
            BLen=len(B)-1
            CLen=len(C)-1

            i=0
            e=0
            while i <= layernum:
                o=e
                while o <= ALen:
                    if A[o]!=JoinM:
                        AX[i]=A[o]
                        e=o+1
                        break
                    o=o+1
                i=i+1

            i=0
            e=0
            while i <= layernum:
                o=e
                while o <= BLen:
                    if B[o]!=JoinM:
                        BX[i]=B[o]
                        e=o+1
                        break
                    o=o+1
                i=i+1
            i=0
            e=0
            while i <= layernum:
                o=e
                while o <= CLen:
                    if C[o]!=JoinM:
                        CX[i]=C[o]
                        e=o+1
                        break
                    o=o+1
                i=i+1

            #print(AX[4],BX[4],CX[4],sep = '')
            #print(AX[3],BX[3],CX[3],sep = '')
            #print(AX[2],BX[2],CX[2],sep = '')
            #print(AX[1],BX[1],CX[1],sep = '')
            #print(AX[0],BX[0],CX[0],sep = '')
            #print('===========================')
            ####################

            p=layernum-1
            while p>-1:
                print(AX[p],BX[p],CX[p],sep = '')
                p=p-1

            print(Platform)

            ###
            
            move(n - 1, auxiliary, target, source)

    move(layernum, A, C, B)
    
    print("Press any key to run again; To fill your RAM please type in 'x'; To quit please type in 'exit'.")
    c = input()
    if c == 'exit':
        break
