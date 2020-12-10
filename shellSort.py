#希尔排序

lst=[4,23,45,67,8,9,341,354,213,4,52,42,45,2,51,3,1]

length=len(lst)
step=length//2

while step>0:
    for i in range(step):
        for j in range(i+step,length,step):
            k=j
            while k>=step and lst[k-step]>lst[k]:
                lst[k-step],lst[k]=lst[k],lst[k-step]
                k-=step
    step//=2

print(lst)


