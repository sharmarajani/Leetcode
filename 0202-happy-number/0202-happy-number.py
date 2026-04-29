class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()        
        while n not in s:
            s.add(n)
            num = 0
            while n:        
                digit = n % 10
                num = num + digit*digit
                n = n // 10
            if num == 1:
                return True
            else:
                n = num
        return False