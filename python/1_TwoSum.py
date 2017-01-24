class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        diff = 0
        for i in range(0, len(nums), 1):
            map[str(i)] = nums[i]
        #print map['1']   
        for k in range(0, len(nums), 1):
            #print "======",nums[k],k,"====="
            diff = target - nums[k];
            #print "diff = ", diff, type(diff)
            #print map.get(str(k)), type(map.get(str(k)))
            try:
                index = int(map.keys()[map.values().index(diff)])
                if ( index != (k) ):
                    #print "yes, index= ", map.keys()[map.values().index(diff)]
                    return [k,index]
            except ValueError:
                pass

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

# if __name__ == '__main__':
#     test = Solution()
#     nums = [5,20,75]
#     #nums = [3, 2, 4]
#     print type(nums)
#     target = 95
#     result = test.twoSum(nums, target)
#     print result