#User function Template for python3

class Solution:
    def trailingZeroes(self, N):
    	toCom = 1
    	ans = 0
    	
    	while True:
    	    toCom *= 5
    	    
    	    if N // toCom == 0:
    	        return ans
    	    ans += N //toCom
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input()) 
        ob = Solution()
        ans = ob.trailingZeroes(N)
        print(ans)
# } Driver Code Ends