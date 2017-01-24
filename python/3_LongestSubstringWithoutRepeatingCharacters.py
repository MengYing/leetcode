class Solution:
    def lengthOfLongestSubstring(self, s):
        map, ans, p1, p2 = {}, 0, 0, 0
        while p2 < len(s):
            #print "+++", map, "+++"
            p = map.get(s[p2], None)
            #print "p = ", p, p1, p2, ans
            if p == None:
                map[s[p2]] = p2
                p2 += 1
                ans = max(ans, p2 - p1)
                #print "---",map
            else:
                while p1 <= p:
                    map.pop(s[p1])
                    p1 += 1
                    #print "==",map
        #print map
        return ans
        """
        :type s: str
        :rtype: int
        """

# if __name__ == '__main__':
# 	result = Solution().lengthOfLongestSubstring("abcabcbb")
# 	print result