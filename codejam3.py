testCases = int(input())
for i in range(testCases):
    dics = int(input());
    sides = list(map(int, input().rstrip().split()))
    sortedArray = sorted(sides);

    if(dics == 1):
        print("Case #" + str(i+1)+": 1")
        continue
    
    minValue = sortedArray[0];
    maxValue = sortedArray[-1];

    count = 0;
    for k in range (dics):
        dice = sortedArray.pop(0);
        if(dice >= count+1):
            count += 1;

    print("Case #" + str(i+1)+": "+str(count));
        
        
    
