class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for n in range(1,n+1):
            if n%15 == 0:
                answer.append("FizzBuzz")
            elif n%5==0:
                answer.append("Buzz")
            elif n%3==0:
                answer.append("Fizz")
            else:
                answer.append("{}".format(n))
        return answer
        
