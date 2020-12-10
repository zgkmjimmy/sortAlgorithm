#插入排序
def insert(lst,index):    
    for i in range(index,0,-1):
        if lst[i-1]<lst[i]:
            return 
        else:
            lst[i-1],lst[i]=lst[i],lst[i-1]
    # if lst[index-1] < lst[index]:
    #     return

    # tmp = lst[index]
    # tmp_index = index
    # while tmp_index > 0 and lst[tmp_index-1] > tmp:
    #     lst[tmp_index] = lst[tmp_index-1]
    #     tmp_index -= 1
    # lst[tmp_index] = tmp

def sort(lst):
    for i in range(1,len(lst)):
        insert(lst,i)

if __name__ == "__main__":
    lst=[2,1,34,5,677,3,1,34,12,45,76]
    sort(lst)
    print(lst)
