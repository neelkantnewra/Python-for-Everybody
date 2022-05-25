# Take 10 number as input and return the sum of all prie number amongs them

# Checking for prime
def checkPrime(num):
    flag = True
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                break
    return flag

def main():
    sum_prime = 0
    for _ in range(10):
        num = int(input())
        if checkPrime(num) == True:
            sum_prime += num 
            
    return sum_prime
    
if __name__ == "__main__":
    print(main())
