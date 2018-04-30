class Solution(object):

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_set = set([])
        for num in nums:
            if len(max_set) < 3:
                max_set.add(num)
            else:
                min_num = min(max_set)
                if num > min_num and num not in max_set:
                    max_set.remove(min_num)
                    max_set.add(num)
        if len(max_set) < 3:
            return max(max_set)
        else:
            return min(max_set)

# if __name__ == '__main__':
#     a = Solution()
#     print(a.thirdMax([1, 2, 2, 5, 3, 5]))
