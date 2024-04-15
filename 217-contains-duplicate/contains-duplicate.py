class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        isExist = set()

        for num in nums:
            if num in isExist:
                return True
            else:
                isExist.add(num)
        
        return False