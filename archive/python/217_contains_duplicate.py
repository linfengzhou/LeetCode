# My solution
class Solution(object):

    def containsDuplicate(self, nums):
        nums_count = {}
        for item in nums:
            if not(str(item) in nums_count):
                nums_count[str(item)] = 1
            else:
                nums_count[str(item)] += 1
        for count in nums_count.values():
            if count > 1:
                return True
                break
        return False


# Good solution
class Solution(object):

    def containsDuplicate(self, nums):
        nums_unique = set()
        for item in nums:
            if not(item in nums_unique):
                nums_unique.add(item)
            else:
                return True
                break
        return False

# Question why set faster than list??????
