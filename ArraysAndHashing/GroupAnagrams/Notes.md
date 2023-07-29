# Group Anagrams

- [ ] Finished by yourself
- [x] Finished via Solution
- [ ] Revision
- [ ] C Implementation

## My Explanation

Create a CountList which keeps tracks of the count of each letters(a-z) of each string and store that list(in the form of a tuple) as the key of the StrMap whose values are the strings with those counts respectively.

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
