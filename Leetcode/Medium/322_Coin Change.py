from collections import deque
class Solution:
    def coinChange(self, coins, amount):

        visit = set()
        q = deque()
        q.append((amount,0))

        while q:
            cur_sum, cnt = q.popleft()
            if cur_sum == 0:
                return cnt
            for i in coins:
                new_cur = cur_sum - i
                if new_cur in visit or new_cur < 0:
                    continue
                visit.add(new_cur)
                q.append((new_cur,cnt+1))
        return -1