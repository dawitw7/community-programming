class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counts = collections.Counter(arr)
        f = sorted(counts.values(),key = lambda x: -x)
        
        
        t = n
        for i,x in enumerate(f):
            t-=x
            if t*2 <= n:
                return i+1
                
