class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        if len(strs) <=1: 
            return strs[0] if len(strs) == 1 else ""
        
        contentLen = 

        for i in xrange(0, 1):
        	if 
        
        for i in xrange(strs):


        """
        :type strs: List[str]
        :rtype: str
        """


if __name__ == '__main__':
	strs = ["asdcv", "asdbngr", "asxcegb"]
	result = Solution().longestCommonPrefix(strs)
	print result