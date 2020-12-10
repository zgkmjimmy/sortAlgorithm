#快速排序
def quick_sort(lst,start,end):
    if start>=end:
        return
    
    mid=lst[start]
    low=start
    high=end
    while low<high:
        while low<high and mid<=lst[high]:
            high-=1
        lst[low]=lst[high]

        while low<high and lst[low]<mid:
            low+=1
        lst[high]=lst[low]

    lst[low]=mid

    quick_sort(lst,start,low-1)

    quick_sort(lst,low+1,end)


if __name__ == "__main__":
    lst=[54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(lst,0,len(lst)-1)

    print(lst)
