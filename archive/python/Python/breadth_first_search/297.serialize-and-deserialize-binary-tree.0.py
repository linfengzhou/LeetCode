class Codec:

    def serialize(self, root):
        data = []
        node_queue = [root]
        start = 0
        while start < len(node_queue):
            node = node_queue[start]
            start += 1
            if node:
                data.append(str(node.val))
                node_queue.append(node.left)
                node_queue.append(node.right)
            else:
                data.append("null")
        # Remove the tail null node.
        while data and data[-1] == "null":
            del data[-1]
        return ",".join(data)

    def deserialize(self, data):
        if not data:
            return None

        # Get all the nodes.
        data_list = data.split(",")
        length = len(data_list)
        node_list = [0] * length
        for i in range(length):
            if data_list[i] == "null":
                node_list[i] = None
            else:
                node_list[i] = TreeNode(int(data_list[i]))

        # Build the tree.
        offset = 1
        cur_pos = 0
        while offset < length:
            if node_list[cur_pos]:
                node_list[cur_pos].left = node_list[offset]
                offset += 1
                if offset < length:
                    node_list[cur_pos].right = node_list[offset]
                    offset += 1
                else:
                    break
            else:
                pass
            cur_pos += 1

        return node_list[0]
