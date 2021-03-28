class Solution:
    def majorityElement(self, A, N):
        #Your code here
        aDir = dict()
        
        for i in A:
            try:
                aDir[i] += 1
                if aDir[i] > N // 2:
                    return i
            except Exception:
                aDir[i] = 1
        
        if N == 1:
            return A[0]
        
        return -1


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends