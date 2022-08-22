class Solution:
    def sortSentence(self, s: str) -> str:
        x = list(s.split())
        di= {}
       
        for i in x:
            di[i[-1]]=i[:-1]
        r = [w for k,w in sorted(di.items())]
        return " ".join(r)
