class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=0
        li=[]
        for i in nums:
            for j in range(len(nums)):
                if (nums[j]-i)<0:
                    count+=1
            li.append(count)
            count=0
        return li                
                
            
                
