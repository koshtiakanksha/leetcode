class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        
        primes = [True]*(n+1)                    # assuming all numbers are prime
        
        primes[0]=primes[1]=False                   # discarding 0 and 1
        
        count=0                                    # setting the count to 0
        
        for i in range(2,n):                     # since 0 and 1 are already discarded
            if primes[i]:
                count+=1                        # if primes[i] is true
                for j in range(2*i,n,i):    # discarding the numbers which come in table of i
                    primes[j]=False          
        
        return count          # count of total true
    
    # time complexity  O(sqrt{n}log log n))
    # space complexity O(n)
    