def printSeriesDecreasing(ch,n):
    assert isinstance(ch,str),'frst argument should be string'
    assert isinstance(n,int),'second argument should be string'
    for i in range(n,0,-1):
        print(ch*i)
    return None
inpCh=input("enter a character:")
inpNum=int(input("Enter a no:"))

print('-'*40)
try:
    printSeriesDecreasing(inpCh,inpNum)
except AssertionError  as ob:
    print(ob)


