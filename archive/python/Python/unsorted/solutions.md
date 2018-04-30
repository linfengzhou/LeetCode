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
# 13 Roman to Integer
- if left char is smaller than right char, res = right - left(V: 5 VI: 6, IV: 4)

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
# 49 Group Anagram
- review the definition of anagram
- how to group the same anagram together?(check sample output) 
# 50 power(x, n) (to do)
- binary search
# 55 jump game
- o(n) time, 0(1) space
# 56 merge intervals
- sort first
- draw their condition
# 58 length_of_last_word
- need bug free
- run own test
# 60 permutation-sequence (to do)(40%)
- factorial
- math
# 61 rotate-list 
- my solution: find mid-> cal length->find breakpoint
- better: generate a cycle, go len - k
- notice: k might larger than length
# 66 plus one
- carry, corner case 99, 999 
# 67 add binary(check solutions)
# 71 simplify-path
- split is bulit-in 
# 73
- space o(m+n): store first row and col zero
- space constant: whether first row and cal zero or not 
# 89 gray code
- first solution: mathematical eq:
  - ```for i range(1<<n)```, ```i ^ i //2 ```
- reflect and prefix method (recursion) 
  - get garycode(n-1) list
  - reverse it 
  - add 1 to highest position (1<<(n-1) | i)
# 92(to do)
- four node swap
- corner case
# 100 same-tree
- dfs
- iteration TLE??
# 101 symmertric-tree
- dfs
- iteration
- condition (both none, one of them is none, equal val)
# 105 construct binary tree from preorder and inorder traversal
- dfs + divide and conquer 
- use preorder to get root val, then find its position at inorder
- find the start end index of left branch and right branch
- corner case, exit of recursion?
# 106 construct binary tree from inorder and postorder traversal
- same as 105
- better solutions?
# 108 convert sorted array to binary search tree
- binary search
# 109 
# 111 to do 
- how to minimum the path(if it is not a leaf, should be what?)
# 116 populating next right pointers in each node
- recursion
- iteration(o(1) space??)
# 117 (to do) 
# 118 pascal triangle
- dp 
# 119 
- dp 
# 121 Best Time to Buy and Sell Stock
- greedy
- maximum is between previous profit and profit calculated by the current price and previous lowest price
# 122 Best Time to Buy and Sell Stock II 
- greedy
- all of diff larger than 0
# 129 
- dfs, divide and conquer
- time(from top to bot, just sum) o(n), space(log n)
# 137 single number ii 
- solution 1: 
  - use ones to record element only appear once(three times may also include, we discuss it later)
  - use twos to record element only show twice
  - every time element come, xor ones array(if no exist, became 1, if exist, became 0)
    - if no exist(show twice), which means we need to rule out it didn't show at twos &(~ twos)
  - the same operation of twos
- solution 2:
  - create ones, twos, threes to record element appear 
  - first update twos (twos | (ones & i)) (if element exist in ones, should be in twos)
  - then update ones with xor 
  - update threes 
  - delete element from ones and twos if there exist in threes
# 142 
- math deduction
# 143
- 3 parts:
  - find mid position, cut to two parts
  - reverse second part(how to reverse a linked list? must hold head and tail)
  - merge 
# 151 
- easy, strip split reverse
# 160 
- find A tail and linked it to B
- find entrance of circle
- retain their original structure
# 165
- to do again
# 168 
- converter(for this case, 10 -> 26)
- recursion 
# 172 
- only need to check how many 5 in n (log5N)
# 191 
- n & (n-1) find last 1 
- n % 2 n >> 1 
# 201 
- Solution 1:
  - use a mask (111111111) to find the leftest common digits of m and n 
  - m = 1110001, n = 1110111, mask = 1110000 
- Solution 2:
  - if n > m, which means the last digit for the answer is zero 
  - move m, n to one step left, to do the same test (also need to add a zero to right)
# 202 
- use a hash table store result
# 203
- what if there are consequtive series of val need to be delete?(in what circumstance you should move head to right?)
# 230 
- inorder (must hand write again!)




