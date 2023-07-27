

# # ! Brute Force
# def containsDuplicate(nums):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] == nums[j]:
#                 return True
#     return False

# # ! Sorting
# def containsDuplicate(nums):
#     nums.sort()
#     for i in range(len(nums)-1):
#         if(nums[i] == nums[i+1]):
#             return True
#     return False

# # ! HashSet
# def containsDuplicate(nums):
#     numsSet = set()
#     for i in nums:
#         if(i in numsSet):
#             return True
#         numsSet.add(i)
#     return False

print(containsDuplicate([4,3,2,1]))
