# Author: Neelkant Newra
# GitHub: https://github.com/neelkantnewra

def BinarySearch(lst,n):
    '''
    lst: sorted array
    n: number to be found on 
    return(bool) True/False 
    '''
    lower_index = 0 
    upper_index = len(lst)-1
    
    while lower_index <= upper_index:
        mid_index = (lower_index+upper_index)//2 
        if lst[mid_index]==n:
            return True
        elif lst[mid_index]>n:
            upper_index = mid_index-1
        else:
            lower_index = lower_index + 1
            
    return False
    
def main():
    lst = [1,2,3,4,5,6,7,8,9,10,23,34,45,55,667,888,9999]
    n = 11
    print(BinarySearch(lst,n))
    
main()
