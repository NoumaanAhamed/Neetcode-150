def isAnagram(strA,strB):
    strAList = list(strA)
    strAList.sort()
    strBList = list(strB)
    strBList.sort()
    return strAList == strBList


print(isAnagram("abc","casb"))
