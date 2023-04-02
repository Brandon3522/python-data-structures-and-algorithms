class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Sum all values in tree
# O(n)
def sum_values(root):
    if root is None:
        return 0
    tree_sum = root.data + sum_values(root.left) + sum_values(root.right)
    return tree_sum


# BFS tree sum
# O(n)
def sum_values_BFS(root):
    if root is None:
        return 0

    tree_sum = 0
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        tree_sum += current.data
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return tree_sum


# Depth first search, Binary tree
# O(n), traverse through all nodes
# Use a stack
# Favors the left-hand branch
def DFS_iterative(root):
    result = []
    if root is None:
        return result

    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        result.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result


def DFS_recursive(root):
    if root is None:
        return []

    result = [root.data]

    result.extend(DFS_recursive(root.left))  # Left tree branch
    result.extend(DFS_recursive(root.right))  # Right tree branch
    return result


# Breadth first search, Binary tree
# O(n)
# Use a queue
def BFS_iterative(root):
    if root is None:
        return []
    queue = [root]
    result = []
    while len(queue) > 0:
        current = queue.pop(0)
        result.append(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

# BFS uses a queue, therefore a recursive approach with the call stack is counterproductive
def BFS_recursive(root):
    pass


# Identify if target is in the tree using iterative BFS
# Return boolean
# O(n)
def tree_includes(root: Node, target):
    if root is None:
        return False
    queue = [root]

    while len(queue) > 0:
        current = queue.pop(0)
        if current.data == target:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False


# Same as above function but with DFS recursion
# O(n)
def tree_includes_DFS_recursive(root, target):
    if root is None:
        return False

    if root.data == target:
        return True

    return tree_includes_DFS_recursive(root.left, target) or tree_includes_DFS_recursive(root.right, target)


# Find min val in binary tree
# O(n)
def min_tree_value(root):
    # Iterative version
    # min = root.data
    # stack = [root]
    #
    # while len(stack) > 0:
    #     current = stack.pop()
    #     if current.data < min:
    #         min = current.data
    #     if current.left:
    #         stack.append(current.left)
    #     if current.right:
    #         stack.append(current.right)
    # return min

    # Recursive version
    if root is None:
        return pow(10, 10)

    min_val = root.data
    left_min = min_tree_value(root.left)
    right_min = min_tree_value(root.right)
    return min(min_val, left_min, right_min)

# DFS recursion
# Find the path with the largest sum
# O(n)
def max_path_sum(root):
    if root is None:
        return pow(10, -10)

    if root.left is None or root.right is None:
        return root.data

    left_min = max_path_sum(root.left)  # Get left
    right_min = max_path_sum(root.right)  # Get right
    max_child = max(left_min, right_min)  # Get max of sub children
    return root.data + max_child


# Find max value in tree
# Use recursive DFS approach
# O(n)
def max_val_tree(root):
    if root is None:
        return pow(10, -10)

    max_val = root.data
    left_max = max_val_tree(root.left)
    right_max = max_val_tree(root.right)
    return max(max_val, left_max, right_max)


# 104: Max depth of binary tree
# O(n)
def maxDepth(root):
    if root is None:
        return 0

    left_max = maxDepth(root.left)
    right_max = maxDepth(root.right)
    return 1 + max(left_max, right_max)

#  Our example tree looks like this:
#         2
#       /   \
#      3     4
#     / \     \
#    5   6     7


# 226: Invert binary tree
# O(n)
def invertTree(root: [Node]):
    if root is None:
        return None

    # Swap children
    temp = root.left
    root.left = root.right
    root.right = temp

    invertTree(root.left)
    invertTree(root.right)

    return root


def main():

    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)

    node2.left = node3
    node2.right = node4
    node4.right = node7
    node3.left = node5
    node3.right = node6

    print("Sum of all values of this tree is (should print 27):")
    print(sum_values(node2))

    sum_values_BFS_result = sum_values_BFS(node2)
    print(f'BFS Sum: {sum_values_BFS_result}')

    DFS_iterative_result = DFS_iterative(node2)
    print(f'DFS iterative: {DFS_iterative_result}')

    DFS_recursive_result = DFS_recursive(node2)
    print(f'DFS recursive: {DFS_recursive_result}')

    BFS_iterative_result = BFS_iterative(node2)
    print(f'BFS iterative {BFS_iterative_result}')

    node10 = Node(10)
    tree_includes_result = tree_includes(node2, 10)
    print(f'Tree includes {tree_includes_result}')

    tree_includes_DFS_recursive_result = tree_includes_DFS_recursive(node2, 5)
    print(f'Tree includes DFS recursive {tree_includes_DFS_recursive_result}')

    min_tree_value_result = min_tree_value(node2)
    print(f'Min tree value: {min_tree_value_result}')

    max_path_sum_result = max_path_sum(node2)
    print(f'Max path sum: {max_path_sum_result}')

    max_val_tree_result = max_val_tree(node2)
    print(f'Max value in tree: {max_val_tree_result}')

    maxDepth_result = maxDepth(node2)
    print(f'Max depth of Binary Tree: {maxDepth_result}')

    invert_tree_result = invertTree([2,1,3])
    print(f'Invert binary tree: {invert_tree_result}')




if __name__ == '__main__':
    main()
