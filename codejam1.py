

def printRow(rowIndex,noOfCols):
    if(noOfCols == 0):
        print("")
    elif(rowIndex == 0 or rowIndex == 1):
        if(rowIndex%2 ==0):
            print(".."+ ("+-"*(noOfCols-1))+"+");
        else:
            print(".."+ ("|."*(noOfCols-1))+"|");

    else:
        if(rowIndex%2 == 0):
            print("+-" * noOfCols + "+");
        else:
            print("|." * noOfCols + "|");
            

def getRows(row, col):
    for z in range(row * 2 + 1):
        printRow(z,col);

def getResult(tec, ro, col):
    print("Case #" + str(tec+1) + ":");
    getRows(ro,col);

if __name__ == '__main__':
    tcases = int(input())

    rows = [];
    colums = [];
    
    for i in range(tcases):
        numList = input().split()
        ro = int(numList[0])
        col = int(numList[1])
        rows.append(ro);
        colums.append(col);

    for j in range(tcases):
        getResult(j,rows[j],colums[j]);
        








            
        
    


            


