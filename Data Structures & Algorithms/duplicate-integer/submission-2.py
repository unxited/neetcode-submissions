class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqe_set = set()
        for member in nums:
            if member in uniqe_set:
                return True
            uniqe_set.add(member)
        
        return False

