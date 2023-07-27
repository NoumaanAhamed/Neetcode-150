def containsDuplicate(nums):
        numsSet = set(nums)
        return len(list(numsSet)) != len(nums)

print(containsDuplicate([4,3,2,1,2]))
