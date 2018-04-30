# my solution
class Solution(object):

    def majorityElement(self, nums):
        unique = []
        count = [0, 0]
        for item in nums:
            if not(item in unique):
                unique.append(item)
                item_counts = len(filter(lambda x: x == item, nums))
                if item_counts > count[1]:
                    count = [item, len(filter(lambda x: x == item, nums))]
        return count[0]

# good solution
# create a dictionary, calcuate each element count
# find the count number larger than n /2 