import math

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e 
c.right = f

# depth-first traversal - go furthest downward before going laterally

def depth_first_values(root):
    if root is None:
        return []

    result = []
    stack = [root]

    while len(stack) != 0:
        current = stack.pop()
        
        result.append(current.val)

        # order influences direction of branch reads
        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)
    
    return result

# print(depth_first_values(a))

def depth_first_values_recursively(root):
    if root is None:
        return []
    
    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)

    return [root.val, *left_values, *right_values]

# print(depth_first_values_recursively(a))

# breadth-first traversal

def breadth_first_traversal(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while len(queue) != 0:
        current = queue.pop(0)
        result.append(current.val)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return result

# print(breadth_first_traversal(a))

# includes

def breadth_first_search(root, target):
    if root is None:
        return False

    queue = [root]

    while len(queue) != 0:
        current = queue.pop(0)
        if current.val == target:
            return True

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)
    
    return False

# print(breadth_first_search(a, "h"))

def depth_first_recursive_search(root, target):
    if root is None:
        return False

    if root.val == target:
        return True
    
    return depth_first_recursive_search(root.left, target) or depth_first_recursive_search(root.right, target)

# print(depth_first_recursive_search(a, "h"))

# sum

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def depth_first_recursive_sum(root):
    if root is None:
        return 0
    
    return root.val + depth_first_recursive_sum(root.left) + depth_first_recursive_sum(root.right)

# print(depth_first_recursive_sum(a))

def breadth_first_sum(root):
    if root is None:
        return 0
    
    sum = 0
    queue = [root]

    while len(queue) != 0:
        current = queue.pop(0)
        sum += current.val

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)
    
    return sum

# print(breadth_first_sum(a))

# min

def depth_first_recursive_min(root):
    if root is None:
        return math.inf

    return min(root.val, depth_first_recursive_min(root.left), depth_first_recursive_min(root.right))

# max root to leaf path sum

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def depth_first_recursive_max_path_sum(root):
    if root is None:
        return -math.inf
    
    if root.left is None and root.right is None:
        return root.val
    
    return root.val + max(depth_first_recursive_max_path_sum(root.left), depth_first_recursive_max_path_sum(root.right))

# print(depth_first_recursive_max_path_sum(a))