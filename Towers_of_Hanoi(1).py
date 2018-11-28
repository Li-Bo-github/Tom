index = 1
frompole[]
topole[]
def moveTower(height,fromPole,withPole,toPole):
    def moveDisk(fromPole,toPole):
        print("moving disk from",fromPole,"to",toPole)
        frompole[index]=fromPole
        topole[index]=toPole
        index = index+1
    if height >= 1:
        moveTower(height-1,fromPole,toPole,withPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,fromPole,toPole)
Height = 3
moveTower(Height,"A","B","C")
def show():
    length = 1
    part[]
    for i in range (Height):
        part[length]= "*"*length
        length = length + 1
    k = 1
    while  k <= index:
        print(" " * (index+5-k) + "*" * (2*k-1) + " " * (index+5-k))
        k += 1      
    

