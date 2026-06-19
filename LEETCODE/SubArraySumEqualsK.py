class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p={0:1}
        c=0
        co=0
        for num in nums:
            c+=num
            if c-k in p:
                co+=p[c-k]
            if c in p:
                p[c]+=1
            else:
                p[c]=1
        return co


            
            
        