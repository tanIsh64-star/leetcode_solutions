class Solution:
    def minMoves(self, nums, limit):

        n = len(nums)

        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):

            a = nums[i]
            b = nums[n - 1 - i]

            x = min(a, b)
            y = max(a, b)

            # Default 2 moves
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # 1 move range
            diff[x + 1] -= 1
            diff[y + limit + 1] += 1

            # 0 move exact sum
            diff[x + y] -= 1
            diff[x + y + 1] += 1

        ans = float('inf')
        curr = 0

        for s in range(2, 2 * limit + 1):
            curr += diff[s]
            ans = min(ans, curr)

        return ans