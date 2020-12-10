#基数排序
import math
def sort(lst,radix=10):
    K=len(str(max(lst)))
    bucket=[[] for i in range(radix)]
    for i in range(1,K+1):
        for val in lst:
            bucket[val%(radix**i)//(radix**(i-1))].append(val)
        del lst[:]
        for each in bucket:
            lst.extend(each)
        bucket=[[] for i in range(radix)]


lst=[2,1,3,4,6,3,6,8,43,7,23,24,678,8,3,523,7367,363,734,5,352,525,623,763]

sort(lst)

print(lst)
