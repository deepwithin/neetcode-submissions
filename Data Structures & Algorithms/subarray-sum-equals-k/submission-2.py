class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr_sum = 0

        prefix_sums = {0: 1} # maps gap seen to count

        for i in range(len(nums)):
            curr_sum = curr_sum + nums[i]
            diff = curr_sum - k

            
            res += prefix_sums.get(diff, 0)

            prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)

        return res