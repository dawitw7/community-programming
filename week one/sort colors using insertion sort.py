class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            j = i
            while(nums[j-1]>nums[j])&(j>0):
                nums[j-1],nums[j]=nums[j],nums[j-1]
                j-=1
        print(nums)            
        