def mabna(k,n):
    s=0
    i=0
    while(k>0):
        d=k%10
        k=k//10
        s=s+d*(n**i)
        i+=1
    return s

def mabna2(s,m):
    list1=[]
    while(s>0):
        d=s%m
        list1.append(d)
        s=s//m

    list1.reverse()
    
    return list1


k=int(input('Enter Your Number = '))
n=int(input('Enter Your Mabna = '))
m=int(input('Enter Your Mabna2= '))
s=mabna(k,n)
print(mabna2(s,m))
