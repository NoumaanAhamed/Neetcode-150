# def topKFrequent(nums,k):
#     numsMap = {}
#     for num in nums:
#         if num in numsMap:
#             numsMap[num] += 1
#         else:
#             numsMap[num] = 1
#     numsMap = sorted(numsMap.items(),key=lambda x : x[1],reverse=True)
#     result= []
#     count = 0
#     for i in numsMap:
#         if count != k:
#             result.append(i[0])
#             count += 1
#     return (result)

def topKFrequent(nums,k):
    numsMap = {}
    for num in nums:
        if num in numsMap:
            numsMap[num] += 1
        else:
            numsMap[num] = 1
    
    buckets = [[] for i in range(len(nums) + 1)]

    for key in numsMap:
        buckets[numsMap[key]].append(key)

    # print(buckets)
    # buckets = [[3], [], [], [1], [2], [3]]

    nonEmptyBuckets = []
    for list in buckets:
        if list:
            nonEmptyBuckets.append(list)

    result = []
    for i in range(len(nonEmptyBuckets) - 1,-1,-1):
        # print(i)
        for n in nonEmptyBuckets[i]:
            result.append(n)
            if (len(result) == k):
                return result


    


print(topKFrequent([1,1,1,2,2,3,4,4],2))