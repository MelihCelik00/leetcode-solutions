class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for idx in range(len(nums)):
            if nums[idx] in hashMap:
                return [hashMap[nums[idx]],idx]
            else:
                hashMap[target-nums[idx]] = idx
