class Solution:
    def isMatch(self, s, p):
        s_ptr = 0
        p_ptr = 0
        star_idx = -1
        match = 0
        
        while s_ptr < len(s):
            
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_idx = p_ptr
                match = s_ptr
                p_ptr += 1
            
            elif star_idx != -1:
                p_ptr = star_idx + 1
                match += 1
                s_ptr = match
            
            else:
                return False
        
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
        
        return p_ptr == len(p)