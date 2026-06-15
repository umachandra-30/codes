class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for c in freq.values():
            if c>1:
                return True
        return False

        