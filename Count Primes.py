class Solution:
    def countPrimes(self, n):
        
        if n < 2:
            return 0
        
        prime = [True] * (n+1)
        
        p =2
        
        # Using Sieve of Eratosthenes algorithm
        while(p*p <= n):
            
            if (prime[p] == True):
                
                for i in range(p*p, n+1, p):
                    prime[i] = False
            
            p += 1
        
        count = 0 # Initialising the count of prime numbers as 0
        
        for p in range(2,n): # Iterating over numbers from 2 to n-1 to check for which prime[] is true
             if (prime[p] == True):
                count += 1
                
        return count

n = 10
print(Solution().countPrimes(n))
                    
                    
        