class Solution(object):

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, c in enumerate(numbers):
            if c in dic:
                return [dic[c], i]
            next_target = target - c
            dic[next_target] = i

# two pointer solution
# create two pointer, one start from left, another start from right
# beacuse sorted, if less than target left + 1 , else right +1


class Solution(object):

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p1, p2 = 0, len(numbers) - 1
        while True:
            if numbers[p1] + numbers[p2] == target:
                return [p1 + 1, p2 + 1]
            elif numbers[p1] + numbers[p2] < target:
                p1 = p1 + 1
            else:
                p2 = p2 - 1


## binary search ?????? 
