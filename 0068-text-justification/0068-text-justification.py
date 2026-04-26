class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        n = len(words)
        
        while i < n:
            line_len = len(words[i])
            j = i + 1
            
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            line_words = words[i:j]
            num_words = len(line_words)
            total_chars = sum(len(word) for word in line_words)
            total_spaces = maxWidth - total_chars
            
            if j == n or num_words == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            
            else:
                gaps = num_words - 1
                even_space = total_spaces // gaps
                extra_space = total_spaces % gaps
                
                line = ""
                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (even_space + (1 if k < extra_space else 0))
                
                line += line_words[-1]
            
            result.append(line)
            i = j
        
        return result