class Solution:
    def longestConsecutive(self, nums):
        nums_dict = {}
        ans = 0
        if not nums:
            return ans
        for i in nums:  # O(N)
            nums_dict[i] = 0

        for n in nums_dict:
            cnt = 0
            target = n
            if n - 1 not in nums_dict:
                while target in nums_dict:
                    target = target + 1
                    cnt +=1
                if cnt >0:
                    ans = max(cnt,ans)
        return ans