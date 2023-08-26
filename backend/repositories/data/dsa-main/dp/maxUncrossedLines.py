class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def helper(index1, index2):
            if(index1 >= len(nums1) or index2>=len(nums2)): return 0

            if(nums1[index1] == nums2[index2]): return 1+helper(index1+1, index2+1)
            
            ans = -1 * 10**10
            ans = max(ans, helper(index1+1, index2))
            ans = max(ans, helper(index1, index2+1))
            return ans

        return helper(0, 0)

    
    

# class Solution:
#     def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

#         map1 = defaultdict(list)
#         for index, val in enumerate(nums1): map1[val].append(index)
        
#         indexMapper = defaultdict(list)
#         for index, val in enumerate(nums2): 
#             if(val not in map1): continue
#             for i in map1[val]: indexMapper[i].append(index)

#         @cache
#         def helper(index1, index2):
#             if(index1 >= len(nums1) or index2>=len(nums2)): return 0
#             ans = -1 * 10**10
#             ans = max(ans, helper(index1+1, index2))
#             for index in indexMapper[index1]:
#                 if(index<index2): continue
#                 ans = max(ans, 1+helper(index1+1, index+1))
            
#             return ans

#         return helper(0, 0)
