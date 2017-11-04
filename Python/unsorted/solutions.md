# 3 longest-substring-without-repeating-characters (two-pointer)
- record **left**: last repeat character next one's index,and can only **increase**
- calculate the len between this char and the left
- compare, record the maximum one (to do)

# 5 Longest Palindromic Substring
- multiple solutions
- first method: brute force(two pointer): 
  - two type of panlidrome: `aba` and `abba`
  - for `aba`, start in the center(left ==right), expand to left-1, and right+1
  - for `abba`, start with two pointer(left:b(1), right:b(2)), expand to left-1 and right+1 (to do)

# 11 Container With Most Water
- two pointer
- need reduce runtime(to do)  

# 14 Longest common prefix
- string

# 19 remove nth node from end of list 
- solution 1: o(2n)
  - first loop find end 
  - second loop deal with delete
- solution 2: o(n)
  - the nth node from end equal to the `total_lenth - n` from start. In this scenario, let a pointer iter n times at first. Then, for antoher pointer, if the first poiter point to None, it would point at the pre node of your delete node(if start at dummy node). (to do )(do this again)
# 20 valid parentheses (to do)
- stack implementation
- watch out return condition
# 22 generate-parenthese (to do)
- backtracking
- time complexity??
- prune condition??
# 24 swap nodes in paris (check solution) (to do)
- swap
# 31 next permutation (to do)
- step 1: loop it find the first number less than next one (reverse loop)
  - if all of them is larger, reverse the whole list,return
  - else
    - find the first element larger than the numbre we find at step 1, swap them
    - reverse  the following array after the first number's index
# 36 valid sudoku (to do)
- create three list of set record each row, col, and grid number
- for loop 2-d array, check whether item already in those three lists
  - if so, return False
  - add this number into three lists
- after loop return True
# 38 count and say (to do)
- check after loop(important!!!)
# 43 multiple string (to do)
- use 99 * 99 as example
- check the iterator after the sub loop(should be the same condition as main loop)(the iterator may beyond the range)(similar as 3sum or 4sum loop condition)
# 48 rotate image  (to do)
- two step: 
  - reverse elements by the diagnal
  - reverse elements by the mid 
- notice:
  - only reverse once(how to write elegant condition)
# 50 power(x, n) (to do)
- binary search
# 55 jump game
- o(n) time, 0(1) space