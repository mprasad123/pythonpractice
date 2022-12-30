def printMonth(dn):
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
    else:
        mn= "invalid"
    return mn
for i in range(7):
    inpNum=int(input())
    print(printMonth(inpNum))









    
    
    
    
