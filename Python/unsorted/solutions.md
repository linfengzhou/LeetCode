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