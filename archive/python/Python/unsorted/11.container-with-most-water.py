class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def computer_area(left, right, height):
            return (right - left) * min(height[left], height[right])

        left, right, res = 0, len(height) - 1, 0
        while (left <= right):
            new_area = computer_area(left, right, height)
            res = max(res, new_area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res
