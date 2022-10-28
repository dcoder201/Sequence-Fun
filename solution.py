#User function Template for python3
import math
class Solution:
	def NthTerm(self, n):
		# Code here
		mod=int(pow(10,9)+7)
		res=1
		for i in range(1,n+1):
		    res=(res*i+1)%mod
		return res
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.NthTerm(n)
		print(ans)

# } Driver Code Ends
