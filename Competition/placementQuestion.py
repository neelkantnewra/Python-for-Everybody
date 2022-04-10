# Create a Substring
def SubString(string):
    return [string[i:j] for i in range(len(string)) for j in range(i+1,len(string)+1)]
    
# Check for the unique alphabet contain text
def check(text):
    for alp in text:
        if text.count(alp)>1:
            return False
    return True
  
def superbString(S):
    sub_string = SubString(S)
    result = -404 
    for string in sub_string:
        if check(string) and len(string)>result:
            result = len(string)
    return result
    



def NthPentonacci(N):
    P = [0,1,2,3,4]
    result = -404
    i = 0 
    while i<N:
        num = P[i] + P[i+1] + P[i+2] + P[i+3] + P[i+4]
        P.append(num)
        i+=1
    return P[N]
    



def changeBy(S):
    result = -404
    sort_string = sorted(list(S))
    unsorted = list(S)
    result = sum([1 for i in range(len(S)) if sort_string[i]!=unsorted[i]])
    return result



def minimumZeroes(S):
    result = -404
    forward_zero = str(int(S))
    reverse_zero = str(int("".join(reversed(forward_zero))))
    result = reverse_zero.count("0")
    return result



def makeItEqual(A,B):
    result = "-404"
    A = list(A)
    B = list(B)
    if len(A) == len(B):
        index = A.index("%")
        A[index] = B[index]
        if A == B:
            return B[index]
        else:
            return -1
    else:
        missing_value = abs(len(A)-len(B))
        index = A.index("%")
        A[index] = B[index]
        ans_str = B[index]
        for i in range(1,missing_value+1):
            A.insert(index+i , B[index+i])
            ans_str = ans_str + B[index+i]
        if A == B:
            result = ans_str
        else:
            return -1
    return result



def minsubarray(arr):
    ans = []
    for i in range(0,len(arr)):
        ans.append(abs(sum(arr[0:i]) - sum(arr[i:])))
    return min(ans)
    
def solve(N,Q,A,query):
    solution = []
    for q in query:
        array = A[:]
        if q[0] == 1:
            for i in range(0,q[1]):
                array.insert(0,array[-1])
                del array[-1]
        else:
            for i in range(0,q[1]):
                array.append(array[0])
                del array[0]
                
        solution.append(minsubarray(array))
        
    return solution
