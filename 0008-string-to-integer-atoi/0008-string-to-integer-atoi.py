class Solution:
    def myAtoi(self, s):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        i = 0
        n = len(s)
        
        while i < n and s[i] == ' ':
            i += 1
        
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result