t = int(input());
for i in range(testCases):
    n = int(input())
    towers = input().split();
    z = 0;
    for word in towers:
        isValid = validateWord(word,len(word));
        if(not isValid):
            print("IMPOSSIBLE")
            break;
        else:
            
        




validateWord(word, count):
    letterDic = { }
    for k in range(count):
        if word[k] in letterDic:
            if(letterDic[word[k]] == k-1):
               letterDic[word[k]] = k;
            else:
                return False;
        else:
            letterDic[word[k]] = k;
    return True;
        
