#User function Template for python3

toMod = 1000000007

class Solution:

	def factorial(self,a, n):
    	# code here
    	
    	maxAns = max(a)
    	
    	aDic = dict()
    	for i in a:
    	    aDic[i] = 0
    	
    	myFac = 1
    	if 0 in aDic:
    	   aDic[0] = myFac 
    	for i in range(1, maxAns + 1):
            myFac = (myFac * i) % toMod
            if i in aDic:
                aDic[i] = myFac % toMod
        
        for i in range(n):
            a[i] = aDic[a[i]]
        return a

#{ 
#  Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        a=list(map(int , input().strip().split()))
        ob = Solution()
        res = ob.factorial(a, n)
        for i in res:
            print(i,end=" ")
        print()
        tc=tc-1
# } Driver Code Ends