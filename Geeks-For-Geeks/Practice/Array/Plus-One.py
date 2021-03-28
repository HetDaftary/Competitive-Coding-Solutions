#User function Template for python3

class Solution:
    def increment(self, arr, N):
        # code here 
    
        i = N - 1
        arr[i] += 1
        while i > 0 and arr[i] > 9:
            arr[i] = 0
            arr[i - 1] += 1
            i -= 1
            
        if arr[0] > 9:
            arr[0] = 0
            arr.insert(0, 1)
        
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
# } Driver Code Ends