class Solution:
    def maxPoints(self, points):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        n = len(points)
        if n <= 2:
            return n
        
        result = 0
        
        for i in range(n):
            slopes = {}
            same = 1
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                dx = x2 - x1
                dy = y2 - y1
                
                if dx == 0 and dy == 0:
                    same += 1
                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g
                    
                    if dx < 0:
                        dx *= -1
                        dy *= -1
                    elif dx == 0:
                        dy = 1
                    
                    slopes[(dx, dy)] = slopes.get((dx, dy), 0) + 1
            
            current_max = same
            for count in slopes.values():
                current_max = max(current_max, count + same)
            
            result = max(result, current_max)
        
        return result