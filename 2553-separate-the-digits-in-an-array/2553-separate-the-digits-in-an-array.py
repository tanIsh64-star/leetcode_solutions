class Solution:
    def separateDigits(self, nums):
        ans = []

        for num in nums:
            for ch in str(num):
                ans.append(int(ch))

        return ans