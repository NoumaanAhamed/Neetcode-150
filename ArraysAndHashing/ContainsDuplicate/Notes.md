# Contains Duplicate

- [x] Finished by yourself
- [ ] Finished via Solution
- [ ] Revision
- [ ] C Implementation

## My Explanation

Given the array,Use a HashSet to keep track of the elements.
Iterate through the array and check whether the element is present in the Set.
if yes, return True, else , add the element to the set.
return False at last.

## Learnings

- Brute-Force : O(n^2) + O(1)
- Sorting(comparing adjacent elements) : O(n\*log(n)) + O(1)
- HashSet : O(n) + O(n)

### Key Concept

#### HashSet

- Syntax :

  - mySet = set()
  - mySet.add(1)
  - print(len(mySet))
  - print(1 in mySet)
  - mySet.remove(1)

- Has unique elements/no duplicates
- HashSet (Python set) provides constant-time average-case complexity for most operations (add, remove, length and checking for existence) when there are no hash collisions. However, in the worst-case scenario (when there are many hash collisions or resizing is required), these operations(including iterating) can take linear time, making it behave like a dynamic array (list).
- 'in' operations has O(n) for arrays but O(1) for HashSets.
- Preferred over arrays, due to O(1) Time complexity.
- Space complexity is O(n).

### Implementation
