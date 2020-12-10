#冒泡排序
def move_max(lst,max_index):
    for i in range(max_index):
        if lst[i]>lst[i+1]:
            lst[i],lst[i+1]=lst[i+1],lst[i]

def pop_sort(lst):
    for i in range(len(lst)-1,0,-1):
        move_max(lst,i)

if __name__=='__main__':
    lst=[4,2,5,6,9,6,7,23,45,234,566,24,12,45]
    # length=len(lst)-1
    # for i in range(length):
    #     move_max(lst,length)
    #     length-=1
    pop_sort(lst)
    print(lst)
