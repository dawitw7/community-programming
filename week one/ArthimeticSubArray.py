class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        new = [True]*len(l)

        for i in range(len(l)):
            data = nums[l[i]:r[i]+1]
            data = sorted(data)

            d = []
            for j in range(0,len(data) - 1,1):
                d.append(data[j+1] - data[j])

            d = list(set(d))
            if len(d) != 1:
                new[i] = False
        return new
