class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        dic ={}
        for i in nums:
            if i in dic:
                c+=dic[i]
                dic[i]+=1
            else:
                dic[i]=1
                
        return c 
