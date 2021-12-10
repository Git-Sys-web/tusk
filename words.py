l=['c','b','e','j','k']
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[i]<l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp

print(l)