def taghsim(m,n):
    list1=[]
    list2=[]
    list3=[]
    for i in range (m,1,-1):
        if m%i==0:
            list1.append(i)

    for j in range (n,1,-1):
        if n%j==0:
            list2.append(j)

    for i in list1:
        if i in list2:
            list3.append(i)
    return list3

m=int(input("Enter Your Number : "))
n=int(input("Enter Your Number : "))

print(taghsim(m,n))


