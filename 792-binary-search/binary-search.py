class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2 # to prevent overflow for the cases 2^31, use l + ((r-l) // 2)
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return m

        return -1