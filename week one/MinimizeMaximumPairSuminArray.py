class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pairs = 0
        
        i = 0
        j =len(nums)-1
        
        while i<j:
            max_pairs = max(max_pairs,nums[i]+nums[j])
            i+=1
            j-=1
        
        return max_pairs
        
