# def groupAnagrams(strs):
#     strsMap ={}
#     for str in strs:
#         sortedStr = "".join(sorted(str))
#         if sortedStr in strsMap:
#             strsMap[sortedStr].append(str)
#         else:
#             strsMap[sortedStr] = [str]
    
#     result = []
#     for key in strsMap:
#         result.append(strsMap[key])
    
#     return result

def groupAnagrams(strs):
    strsMap = {}
    for str in strs:
        countMap =[0] * 26
        for i in str:
            # if i in countMap:
            countMap[ord(i) - ord('a')] += 1
            # else:
            #     countMap[ord(i) - ord('a')] = 1
        newMap = tuple(countMap)
        print(newMap)
        if newMap in strsMap:
            strsMap[newMap].append(str)
        else:
            strsMap[newMap] = [str]
    result = []
    for key in strsMap:
        result.append(strsMap[key])
    print(result)


groupAnagrams(["ddddddddddg","dgggggggggg"])