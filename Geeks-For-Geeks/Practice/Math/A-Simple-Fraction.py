#User function Template for python3

toRound = 10

class Solution:
	def fractionToDecimal(self, num, den):
		if (num == 0):
            return "0"
 
        sign = -1 if (num < 0) ^ (den < 0) else 1
 
        num = abs(num)
        den = abs(den)
 
        initial = num // den
 
        res = ""
 
        if (sign == -1):
            res += "-"
 
        res += str(initial)
 
        if (num % den == 0):
            return res
 
        res += "."
 
        rem = num % den
        mp = {}
 
        index = 0
        repeating = False
        while (rem > 0 and not repeating) :
            if ( rem in mp):
                index = mp[rem]
                repeating = True
                break
            else:
                mp[rem] = len(res)
 
            rem = rem * 10
 
            temp = rem // den
            res += str(temp )
            rem = rem % den
     
        if (repeating) :
            res += ")"
            x = res[:index]
            x += "("
            x += res[index:]
            res = x
        return res
		
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		numerator, denominator = input().split()
		numerator = int(numerator); denominator = int(denominator)
		ob = Solution()
		ans = ob.fractionToDecimal(numerator, denominator)
		print(ans)
# } Driver Code Ends