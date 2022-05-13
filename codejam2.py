


testCases = int(input())
  

resultArray=[]
cyanLarge = [];
magentaLarge = [];
yellowLarge = [];
blackLarge = [];
for i in range(testCases):
    for j in range(3):
        printer = input().split();
        cyanLarge.append(int(printer[0]));
        magentaLarge.append(int(printer[1]));
        yellowLarge.append(int(printer[2]));
        blackLarge.append(int(printer[3]));
    

    
for mainLoop in range(testCases):
    cyan =  cyanLarge[0:3];
    magenta = magentaLarge[0:3];
    yellow = yellowLarge[0:3];
    black = blackLarge[0:3];
    del cyanLarge[:3]
    del magentaLarge[:3]
    del yellowLarge[:3]
    del blackLarge[:3]
    
    cyanMin = min(cyan);
    magentaMin = min(magenta)
    yellowMin = min(yellow);
    blackMin = min(black);
 
    if(cyanMin >= 1000000):
        print("Case #"+str(mainLoop+1)+": 1000000 0 0 0")
    elif(magentaMin >= 1000000):
        print("Case #"+str(mainLoop+1)+": 0 1000000 0 0")
    elif(yellowMin >= 1000000):
        print("Case #"+str(mainLoop+1)+": 0 0 1000000 0")
    elif(blackMin >= 1000000):
        print("Case #"+str(mainLoop+1)+": 0 0 0 1000000")
    else:
        thresh = 1000000;
        #chosing cyan
        gap = thresh - cyanMin;
        if(magentaMin >= gap):
            print("Case #" +str(mainLoop+1)+": " + str(cyanMin) + " " + str(gap) + " "+ "0 0");  
        else:
            gap = gap - magentaMin
            if(yellowMin >= gap):
                print("Case #"+str(mainLoop+1)+": " + str(cyanMin) + " " + str(magentaMin) + " " +str(gap) + " "+ "0");  
            else:
                gap = gap - yellowMin
                if(blackMin >= gap):
                    print("Case #"+str(mainLoop+1)+": " + str(cyanMin) + " " + str(magentaMin) + " " +str(yellowMin) + " "+ str(gap));  
                else:
                    print("Case #"+str(mainLoop+1)+": " "IMPOSSIBLE");
                    
        
