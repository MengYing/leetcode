class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows==1:
            return s
        period= 2*(nRows -1)
        #print period
        lines=["" for i in range(nRows)]
        #print lines
        # record the order of the string.
        d={} # dict remainder:line
        for i in xrange(period):
            if i<nRows:
                d[i]=i
                #print "--", d
            else:
                d[i]=period-i
                #print "==", d

        for i in xrange(len(s)):
            lines[ d[i%period] ] +=s[i]
            #print lines    

        return "".join(lines)    

if __name__ == '__main__':
    result = Solution().convert("rbfcriqifpgynkrrefxsnvucftpwctgtwmxnupycfgcuqunublmoiitncklefszbexrampetvhqnddjeqvu",81)
    print result


# class Solution(object):
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         if numRows == 1: return s
#         rows = [''] * numRows
#         num = (numRows-1)*2
#         for i, item in enumerate(s):
#             if i % num >= numRows:
#                 rows[(num - i % num) % numRows] += item
#             else:
#                 rows[i % num] += item
#         return ''.join(rows)