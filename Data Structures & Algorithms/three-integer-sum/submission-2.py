class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2 pointer question
        # sort the numbers
        # pick the first no.
        # go over remaining no.s from both sides, till pointers meet
        # then next, so on
        nums.sort()

        triplet = set()
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    triplet.add((nums[i], nums[l], nums[r]))
                    l += 1
                    # r -= 1

        return [list(t) for t in triplet]