# Author: Neelkant Newra
# GitHub: https://github.com/neelkantnewra

def LinearSearch(lst,n):
    '''
    lst: array
    n: number to be find
    return(bool) True/False 
    '''
    for i in range(len(lst)):
        if lst[i]==n:
            return True
    return False
    
def main():
    lst = [1,2,3,4,5,6,7,8,9,10,23,34,45,55,667,888,9999]
    n = 888
    print(LinearSearch(lst,n))
    
main()
