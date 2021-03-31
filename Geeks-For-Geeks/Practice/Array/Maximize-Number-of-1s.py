#User function Template for python3


# m is maximum of number zeroes allowed 
# to flip, n is size of array 
def findZeroes(arr, n, m) : 
	
	# Left and right indexes of current window 
	wL = wR = 0

	# size of the widest window 
	bestWindow = 0

	# Count of zeroes in current window 
	zeroCount = 0

	# While right boundary of current 
	# window doesn't cross right end 
	while wR < n: 
		
		# If zero count of current window is less than m, 
		# widen the window toward right 
		if zeroCount <= m : 
			if arr[wR] == 0 : 
				zeroCount += 1
			wR += 1

		# If zero count of current window is more than m, 
		# reduce the window from left 
		if zeroCount > m : 
			if arr[wL] == 0 : 
				zeroCount -= 1
			wL += 1

		# Updqate widest window if 
		# this window size is more 
		if (wR-wL > bestWindow) and (zeroCount<=m) : 
			bestWindow = wR - wL 

	return bestWindow
    
    
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends