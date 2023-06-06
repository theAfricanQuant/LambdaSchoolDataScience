class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        visited = []
        current = self
        while current:
            cb(current.value)

            if current.left:
                visited.append(current)
                current = current.left
            elif current.right:
                current = current.right
            elif len(visited) > 0:
                parent = visited.pop()
                current = parent.right
            else:
                break

    def breadth_first_for_each(self, cb):
        visited = []
        visited_left_child = []
        current = self
        go_to_next_level = False

        while current or visited or visited_left_child:
            if current:
                cb(current.value)
                visited.append(current)

            if visited_left_child:
                parent = visited_left_child.pop(0)
                current = parent.right
            elif len(visited) > 0:
                parent = visited.pop(0)
                visited_left_child.append(parent)
                current = parent.left
            else:
                break

            

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if self.left:
                self.left.insert(value)
            else:
                self.left = new_tree
        elif not self.right:
            self.right = new_tree
        else:
            self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
