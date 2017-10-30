# 3 longest-substring-without-repeating-characters (two-pointer)
- record **left**: last repeat character next one's index,and can only **increase**
- calculate the len between this char and the left
- compare, record the maximum one 

# 5 Longest Palindromic Substring
- multiple solutions
- first method: brute force(two pointer): 
  - two type of panlidrome: `aba` and `abba`
  - for `aba`, start in the center(left ==right), expand to left-1, and right+1
  - for `abba`, start with two pointer(left:b(1), right:b(2)), expand to left-1 and right+1  
