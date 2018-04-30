class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ori_rows = len(nums[0])
        ori_cols = len(nums)
        total_items = ori_rows * ori_cols
        if total_items != (r*c):
            return nums
        else:
            new_nums = []
            for i in range(total_items):
                new_num = nums[i / ori_rows][i % ori_rows]
                if i % c == 0:
                    new_nums.append([])
                    new_nums[i / c].append(new_num)
                else:
                    new_nums[i / c].append(new_num)
            return new_nums
