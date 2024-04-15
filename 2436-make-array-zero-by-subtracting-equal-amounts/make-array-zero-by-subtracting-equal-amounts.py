class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        non_unique_elems = set()

        if [0]*len(nums) == nums:
            return 0

        if len(nums) == 1:
            return 1
        
        for i in range(len(nums)):
            if nums[i] != 0:
                if nums[i] in non_unique_elems:
                    pass
                else:
                    non_unique_elems.add(nums[i])

        return len(non_unique_elems)
                
        