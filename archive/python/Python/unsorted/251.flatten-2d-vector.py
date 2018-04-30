class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec = vec2d
        self.next_index = 0
        self.list_index = 0
        self.list_len = [len(one) for one in vec2d]

    def next(self):
        """
        :rtype: int
        """
        if self.next_index == self.list_len[self.list_index] - 1:
            num = self.vec[self.list_index][self.next_index]
            self.next_index = 0
            self.list_index += 1
        else:
            num = self.vec[self.list_index][self.next_index]
            self.next_index += 1
        return num

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.vec and self.list_index < len(self.vec):
            if self.vec[self.list_index] == []:
                self.list_index += 1
                continue
            elif self.list_index >= len(self.vec) - 1 and self.next_index >= len(self.vec[-1]):
                return False
            else:
                return True
        return False


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
