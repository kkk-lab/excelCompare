class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        temp=set(J)
        print(temp)
        return sum(x in temp for x in S)

a=Solution()
print(a.numJewelsInStones('ab','abcdef'))
