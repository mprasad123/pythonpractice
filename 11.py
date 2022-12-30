def printMonth(dn):
    if(dn==1):
        return "january"
    elif(dn==2):
        return "feburary"
    elif(dn==3):
        return "march"
    elif(dn==4):
        return "april"
    elif(dn==5):
        return "may"
    elif(dn==6):
        return "june"
    elif(dn==7):
        return "july"
    else:
        return "invalid"


def printMonth1(dn):
    mn=''
    if(dn==1):
       mn= "january"
    elif(dn==2):
        mn= "february"
    elif(dn==3):
        mn= "march"
    elif(dn==4):
        mn= "april"
    elif(dn==5):
        mn= "may"
    elif(dn==6):
        mn= "june"
    elif(dn==7):
        mn= "july"
    
    return mn

import time
for i in range(7):
    inpNum=int(input())
    start=time.time()
    print(printMonth(inpNum))
    print((time.time()-start)*1000000)
    start=time.time()
    print(printMonth1(inpNum))
    print((time.time()-start)*1000000)
    









    
    
    
    
