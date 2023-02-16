class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lst = list()
        i = 0
        while i < n:
            i += 1
            if i % 3 == 0 and i % 5 == 0:
                lst.append("FizzBuzz")
            elif i % 3 == 0:
                lst.append("Fizz")
            elif i % 5 == 0:
                lst.append("Buzz")
            else:
                lst.append(str(i))
        return lst


a = Solution()
print(a.fizzBuzz(3))  # ["1","2","Fizz"]
print(a.fizzBuzz(5))  # ["1","2","Fizz","4","Buzz"]
print(a.fizzBuzz(15))  # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
