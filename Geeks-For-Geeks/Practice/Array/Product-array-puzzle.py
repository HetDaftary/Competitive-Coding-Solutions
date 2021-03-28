#User function Template for python3

def productExceptSelf(arr, n):
    #code here
    
    if n == 2:
        return [arr[1], arr[0]]
    
    isZero = False
    zeros = 0
    maxPro = 1
    for i in arr:
        if i != 0:
            maxPro *= i
        else:
            zeros += 1
            isZero = True
    
    if isZero: 
        if zeros < 2:
            for i in range(0, n):
                if arr[i] == 0:
                    arr[i] = maxPro
                else:
                    arr[i]  = 0
        else:
            return [0 for i in range(n)]
    else:
        for i in range(0, n):
            arr[i] = maxPro // arr[i]

    return arr
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends