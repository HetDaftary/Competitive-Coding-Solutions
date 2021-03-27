#User function Template for python3


def MissingNumber(array,n):
    arrSet = set(array)
    
    for i in range(1, n + 1):
        if not i in arrSet:
            return i

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=MissingNumber(a,n)
    print(s)
# } Driver Code Ends