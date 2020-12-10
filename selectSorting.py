#选择排序
def select(lst):
    for i in range(len(lst)):
        min=i
        for j in range(i,len(lst)):
            if lst[min]>lst[j]:
                min=j
        lst[i],lst[min]=lst[min],lst[i]

lst=[9,6,3,2,5,78,23,6,8,3,2,45,76]
select(lst)
print(lst)
