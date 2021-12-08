# Author: Neelkant Newra
# GitHub: https://github.com/neelkantnewra

def SelectionSort(lst):
    '''
    input: (lst) unsorted list
    Output: sorted list
    '''
    for i in range(0,len(lst)):
        min_position = i
        for j in range(i,len(lst)):
            if lst[j] < lst[min_position]:
                min_position = j
                
        lst[i],lst[min_position] = lst[min_position],lst[i]
        
    return lst
        
def main():
    lst = [4,3,6,21,33,67,2,43,6,343,7,78,9,10]
    print(SelectionSort(lst))
    
main()
