from gobblet_node import GobbletNode

class GobbletStack:

    def __init__(self):
        self.head = GobbletNode("head", "z")  # Dummy node
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += f"({cur.length}, {cur.color}) -> "
            cur = cur.next
        return out[:-4]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def top(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        temp_node = self.head.next
        return temp_node

    def push(self, node: GobbletNode):
        temp = GobbletNode(node.length, node.color)
        temp.next = self.head.next
        self.head.next = temp
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove


# Driver Code
if __name__ == "__main__":
    print("ssssssssss")
    gobblet_stack = GobbletStack()
    node1 = GobbletNode(3, 'R')
    print("aaaaa")
    gobblet_stack.push(node1)
    gobblet_stack.push(node1)
    gobblet_stack.push(node1)
    print(f"Gobblet Stack: {gobblet_stack}")
    print("dddddddd")

    print(gobblet_stack.top().color)

    print(gobblet_stack.getSize())

    removed_node = gobblet_stack.pop()
    print(f"Pop: ({removed_node.length}, {removed_node.color})")
    print(f"Gobblet Stack: {gobblet_stack}")
