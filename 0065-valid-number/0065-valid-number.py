class Solution:
    def isNumber(self, s):
        s = s.strip()
        
        seen_digit = False
        seen_dot = False
        seen_e = False
        
        for i in range(len(s)):
            
            if s[i].isdigit():
                seen_digit = True
                
            elif s[i] in ['+', '-']:

                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
                
            elif s[i] == '.':

                if seen_dot or seen_e:
                    return False
                seen_dot = True
                
            elif s[i] in ['e', 'E']:
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False   
                
            else:
                return False
        
        return seen_digit