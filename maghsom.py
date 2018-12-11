def taghsim(m,n):
    list1=[]
    list2=[]
    for i in range (m,1,-1):
        if m%i==0:
            list1.append(i)

    for j in range (n,1,-1):
        if n%j==0:
            list2.append(j)

    return list1,list2

m=int(input("Enter Your Number : "))
n=int(input("Enter Your Number : "))

print(taghsim(m,n))


