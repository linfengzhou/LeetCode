# my solution
class Solution(object):

    def removeDuplicates(self, nums):
        count = 0
        # duplicates = 0
        last_unique = float(nan)
        if not nums:
            return count
        for num in nums:
            if num == last_unique:
                pass
            else:
                nums[count] = num
                count += 1
                last_unique = num
        # for i in range(duplicates):
        #     nums.pop()
        return count
