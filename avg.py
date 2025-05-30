from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        add_nm = len(rolls) + n
        add_rolls = sum(rolls)
        sum_n = (mean * add_nm) - add_rolls
        if sum_n < 0:
            return []
        return self.get_nums(sum_n, n)

    def get_nums(self, sum_n, n):
        avg = sum_n / n
        diff = avg % n
        avg_int = int(avg)
        if avg > 6 or avg < 1:
            return []

        nums = [avg_int] * n
        if n * avg_int != sum_n:
            # diff = sum_n - n * avg_int
            for i in range(diff):
                nums[i]+=1
        return nums
        # if avg_int*(n-1) < sum_n:
        #     last_number = (sum_n - (avg_int*(n-1)))
        #     list_ = [avg_int] * (n-1)
        #     list_.append(last_number)
        #     return list_
        # print(avg)

print(Solution().missingRolls([4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5], 4, 40)) # [6, 6]
# print(Solution().missingRolls([4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5], 4, 40)) # [6, 6]
# print(Solution().missingRolls([4,2,2,5,4,5,4,5,3,3,6,1,2,4,2,1,6,5,4,2,3,4,2,3,3,5,4,1,4,4,5,3,6,1,5,2,3,3,6,1,6,4,1,3], 2, 53)) # [6, 6]