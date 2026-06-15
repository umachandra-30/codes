class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        initial={}
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in initial:
                return [initial[comp],i]
            initial[nums[i]]=i  
    