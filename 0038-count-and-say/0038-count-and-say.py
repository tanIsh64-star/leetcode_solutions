class Solution:
    def countAndSay(self, n):
        result = "1"
        
        for _ in range(n - 1):
            new_string = ""
            count = 1
            
            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    new_string += str(count) + result[i - 1]
                    count = 1
            
            new_string += str(count) + result[-1]
            result = new_string
        
        return result