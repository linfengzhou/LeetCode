class Solution(object):

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] == nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                print(res)
                res.append(res[j] + [nums[i]])
        return res

if __name__ == '__main__':
    a = Solution()
    print(a.subsetsWithDup([1, 2, 2]))
