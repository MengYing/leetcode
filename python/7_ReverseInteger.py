class Solution(object):
    def reverse(self, x):
    	rev, flag = 0, 0
    	MaxInt = (1 << 31) - 1
    	if (x < 0):
    		x = x * -1
    		flag = 1
        while (x != 0):
        	rev = rev*10 + x%10
        	x = x/10
        if ( rev >= MaxInt): return 0
        return rev if flag == 0 else rev*-1

        """
        :type x: int
        :rtype: int
        """
        
if __name__ == '__main__':
	result = Solution().reverse(1000000003)
	print result
