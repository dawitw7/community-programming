class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        sorted_piles = sorted(piles)[::-1]

        return sum(sorted_piles[i] for i in range(1, n//3*2+1,2))
