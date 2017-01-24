class Solution(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
        	return True
        else:
        	return False
        """
        :type x: int
        :rtype: bool
        """
       
if __name__ == '__main__':
	result = Solution().isPalindrome(12321)
	print result
