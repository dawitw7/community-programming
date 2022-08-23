class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        li = []
        x = sorted(nums)
        for i in range(len(x)):
            if x[i]==target:
                li.append(i)
        return sorted(li)        
