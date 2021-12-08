# Author: Neelkant Newra
# GitHub: https://github.com/neelkantnewra

def BubbleSort(lst):
    '''
    input: (lst) unsorted list
    Output: sorted list
    '''
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                
    return lst
    
def main():
    lst = [4,3,6,21,33,67,2,43,6,343,7,78,9,10]
    print(BubbleSort(lst))
    
main()
