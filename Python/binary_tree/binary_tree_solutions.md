# 144 preorder traversal
- while stack
- easy
# 94 inorder traversal
- two while loop
- inside loop, find the leftest node
- general loop, add curent value then go right
- need second times
# 104 maximum depth of binary tree
- divide and conquer
- tree traversal (recursion) : notice int object cannot be reference, check solution 1.py
# 257 binary tree path
- divide and conquer(solution 1)
- three essential elements of recursion:
  step 1: the definition of recursion(for java return type)
  step 2: split the recursion(divide and conquer)
  step 3: the exit of recursion
- other solutions(to_do): bfs+queue dfs+stack (non-recursion)
# 110 balanced binary tree
- most important things for divide and conquer is the first step:
  the definition of the recursion, which means you need to think about the result type.
  - for this question, the result should return two things depends on the problem description:
  whether the subtree is balance, and the difference between left and right subtree is no more than 1
- rest of them are typicall recursion, divide and conquer then write the exit of recursion
# 236 lowest common ancestor
- divide and conquer:  
  - define the return (the definition of recursion whether need addition helper to do that)
  - write divide (split the recursion) and merge(condition to merge left and right part)
  - write the exit of recursion
# 98 validate binary search tree
- divide and conquer:
  - define the return (wether balance or not, the smallest number in tree, the biggest number in tree)
  - write divide and merge(condition, how to return True? -> both parts are balance and left_max < root.val < right.min)
  - write the exit of recursion (root is None)
- tree traversal:
  - inorder: two while loop
  - use tree viz to understand the algo
  - check res list if res[i-1]>= res[i] return False
# 114 flatten binary tree to linked list
- traversal(non-recursion) done!
- divide and conquer to do 
- traversal(recursion) to do