#User function Template for python3

class Solution:
    def rightRotate(self, arr, n, outOfPlace, cur):
        temp = arr[cur]
        for i in range(cur, outOfPlace, -1):
            arr[i] = arr[i - 1]
        arr[outOfPlace] = temp
        return arr
 
 
    def rearrange(self, arr, n):
        outOfPlace = -1
        for index in range(n):
            if(outOfPlace >= 0):
 
                if((arr[index] >= 0 and arr[outOfPlace] < 0) or
                   (arr[index] < 0 and arr[outOfPlace] >= 0)):
                    arr = self.rightRotate(arr, n, outOfPlace, index)
                    if(index-outOfPlace > 2):
                        outOfPlace += 2
                    else:
                        outOfPlace = - 1
    
            if(outOfPlace == -1):
                if((arr[index] >= 0 and index % 2 == 0) or (arr[index] < 0 and index % 2 == 1)):
                    outOfPlace = index
        return arr
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends