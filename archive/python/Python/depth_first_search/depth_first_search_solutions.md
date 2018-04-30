## 78 subsets
## 90 subsets ii
- remember sort (wrong second times!)
- return to result at first
- comdition if num is not at the first index and its left num equal to it and is not the start num, continue
## 46 permutation
- return result if len equal to total nums
- condition  using visit!!
## 47= 46 + 90
## 39 combination sum
- loop range last_start to end
- condition target < nums continue
- another solution, use start index (why? should consider duplicates)
  - if the dup number only exit when the previous one already in the set
## 40 combination sum ii 
- subset ii + permutation ii + combination sum
- loop subset ii 
- visit permutation ii 
- sum combination sum
## 77 combination
- dfs O(n!) python version cannot pass
- non-recursion O((n-k)!) (Based on Stack)
  - backtracking condition: when stack.length equal to k or the rest of pool is less than k - stack.length
  	e.g. [1,4]-> [1] -> [2] ->[2,1] ---->[3,4] -> [3] -> [4] -> [] -> end return
## 17 Letter Combinations of a Phone Number
- dfs
- O(3^n)
- no need for backtracking
## 131 partition palindrome
- three part:
  - dfs
  - check_in_valid_parlindrome
  - get_string
- optimization part: is_valid_parlindrome:
  - dynamic programming (re-do this part)

