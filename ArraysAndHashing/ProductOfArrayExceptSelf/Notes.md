# Product

- [ ] Finished by yourself
- [x] Finished via Solution
- [ ] Revision
- [ ] C Implementation

## My Explanation

To calculate the product array, we can find the left and right product separately and then return the product of the left and right to get the answer.

## Learnings

- Brute-Force : O(n!) for all permutations
- Sorting the strings : O(n\*log(n)) + O(1)
- HashMap/ Dictionary : O(n) + O(n) [n = string1 + string2]

### Key Concept

#### HashMap / Dictionary

- Syntax:

  - myMap = {}
  - myMap['a'] = 3
  - print(len(myMap))
  - myMap['a'] = 4
  - print("a" in myMap)
  - myMap.pop('a')
  - for key in myMap:
    print(key,myMap[key])

- Same length of strings -> one iteration for both strings
- store count(value) of each character(key)
- use map.get(a,0), to set default value of a to 0,if there is no mapping for a.
- sorted(x) -> works on any iterable
- x.sort() -> works only on lists
- Time complexity is O(1) for normal operations like insert,delete and search.
- Space complexity is O(n).

### Implementation
