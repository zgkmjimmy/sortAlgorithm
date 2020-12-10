def merge_lst(left_lst,right_lst):
    left_index,right_index=0,0
    res_lst=[]
    while left_index<len(left_lst) and right_index<len(right_lst):
        if left_lst[left_index]<right_lst[right_index]:
            res_lst.append(left_lst[left_index])
            left_index+=1
        else:
            res_lst.append(right_lst[right_index])
            right_index+=1
    
    if left_index==len(left_lst):
        res_lst.extend(right_lst[right_index:])
    else:
        res_lst.extend(left_lst[left_index:])

    return res_lst

def merge_sort(lst):
    if len(lst)<=1:
        return lst
    mid=len(lst)//2
    left_lst=merge_sort(lst[:mid])
    right_lst=merge_sort(lst[mid:])
    return merge_lst(left_lst,right_lst)

if __name__ == "__main__":
    lst=[19,23,34,214,52,13,525,63,241,15,52,52,6,2,52,874,74]
    print(merge_sort(lst))

