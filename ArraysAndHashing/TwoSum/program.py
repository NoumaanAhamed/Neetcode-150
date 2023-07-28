
# ! Brute-Force

# def twoSum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if(nums[i]+nums[j] == target):
#                 return [i,j]

# ! Two-pointers

# def twoSum(nums,target):
#     nums.sort() #returns the indices of the sorted array
#     start = 0
#     end = len(nums) - 1
#     while(start < end):
#         if(nums[start] +  nums[end] > target):
#             end = end - 1
#         elif (nums[start] + nums[end] < target):
#             start = start + 1
#         else:
#             return [start,end]
        
# ! HashMap

def twoSum(nums,target):
    prevMap = {} # stores the elements, so there is no target for the sum of teh same element
    # as diff exists if we set prevMap 
    for i in range(len(nums)): # ! or for i,n in enumerate(nums)
        diff = target - nums[i]
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[nums[i]] = i

# my_list = [1, 2, 3]
# my_dict = {num: i for i, num in enumerate(my_list)}
# my_dict2 = {i: num for i, num in enumerate(my_list)}

# print(my_dict,my_dict2)



print(twoSum([1,2,3,4],5))

