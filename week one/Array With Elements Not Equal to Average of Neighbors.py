class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        re= []
        l,r = 0, len(nums)-1
        while len(re) != len(nums):
            re.append(nums[l])
            l+=1
            if l<=r:
                re.append(nums[r])
                r-=1
        return re
