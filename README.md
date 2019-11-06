

#Counting Valley

def countingValleys(n, s):
    sea_level=0
    down_hill=0
    d,u=0,1
    for i in range (n):
        if s[i]=='U':
            sea_level+=1
            if sea_level==0:
                down_hill+=1
        else:
            sea_level-=1
    return down_hill
