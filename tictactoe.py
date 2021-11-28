reference = [['1','2','3'],['4','5','6'],['7','8','9']]
box = [['-','-','-'],['-','-','-'],['-','-','-']]

def display(box):
    for i in range(0,3):
        for j in range(0,3):
            if(j<2):
                print(" "+box [i][j], end=" |")
            else:
                print(" "+box[i][j], end="\n")
        if(i<2):
            print("-----------")
    print("\n")
    return 0

def GameStatus(box):
    #rows
    if((box[0][0]=="x" or box[0][0]=="o") and box[0][0]==box[0][1] and box[0][2]==box[0][1]):
        return True
    elif ((box[1][0]=="x" or box[1][0]=="o") and box[1][0]==box[1][1] and box[1][2]==box[1][1]):
        return True
    elif ((box[2][0]=="x" or box[2][0]=="o") and box[2][0]==box[2][1] and box[2][2]==box[2][1]):
        return True
    
    #columns
    elif ((box[0][0]=="x" or box[0][0]=="o") and box[0][0]==box[1][0] and box[1][0]==box[2][0]):
        return True
    elif ((box[0][1]=="x" or box[0][1]=="o") and box[0][1]==box[1][1] and box[1][1]==box[2][1]):
        return True
    elif ((box[0][2]=="x" or box[0][2]=="o") and box[0][2]==box[1][2] and box[1][2]==box[2][2]):
        return True
    
    #diagonals
    elif ((box[0][0]=="x" or box[0][0]=="o") and box[0][0]==box[1][1] and box[1][1]==box[2][2]):
        return True
    elif ((box[0][2]=="x" or box[0][2]=="0") and box[0][2]==box[1][1] and box[1][1]==box[2][0]):
        return True
    else:
        return False

def PlayerInput(a,chance):
    if(a==1):
        if(box[0][0]=="-"):
            box[0][0]=chance
            return True
        else:
            print("not allowed")
            return False
    elif(a==2):
        if(box[0][1]=="-"):
            box[0][1]=chance
            return True
        else:
            print("not allowed")
            return False
    elif(a==3):
        if(box[0][2]=="-"):
            box[0][2]=chance
            return True
        else:
            print("not allowed")
            return False
    elif(a==4):
        if(box[1][0]=="-"):
            box[1][0]=chance
            return True
        else:
            print("not allowed")
            return False
    elif(a==5):
        if(box[1][1]=="-"):
            box[1][1]=chance
            return True
        else:
            print("not allowed")
            return False
    elif(a==6):
        if(box[1][2]=="-"):
            box[1][2]=chance
            return True
        else:
            print("not allowed")
            return False
    elif(a==7):
        if(box[2][0]=="-"):
            box[2][0]=chance
            return True
        else:
            print("not allowed")
            return False
    elif(a==8):
        if(box[2][1]=="-"):
            box[2][1]=chance
            return True
        else:
            print("not allowed")
            return False
    elif(a==9):
        if(box[2][2]=="-"):
            box[2][2]=chance
            return True
        else:
            print("not allowed")
            return False
    else:
        print("invalid, try again\n")
        return False

print("position reference below")
display (reference)
display (box)
t=0
while(t<9):
    if(t%2==0):
        chance="x";
    else:
        chance="o"
    a=int(input("enter position " ))
    valid=PlayerInput(a,chance)
    if(valid==False):
        continue
    status=GameStatus(box)
    print("\n")
    display(box)
    if(status==True):
        print(chance + " wins")
        break
    t=t+1
if(status==False):
    print("draw\n")
        