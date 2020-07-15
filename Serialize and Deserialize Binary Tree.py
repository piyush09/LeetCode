"""
Algo: Serializing and Deserializing using Preorder Traversal.
      You can serialize your data in any order (PreOrder, InOrder, PostOrder), 
      but there is a condition that the order of serialization and deserialization must be same.

"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Codec:

    # Recursive Preorder Traversal
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        # A recursive helper function for serialize() function
        def rserialize(root, string):

            if root is None:  # This is the base case
                string += 'None,'

            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)

            return string

        return rserialize(root, '')

    # Deserializing obtained data_list, which was previously done using preorder traversal.
    # So Deserializing using Preorder traversal.
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        # A recursive helper function for deserialization
        def rdeserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])  # Putting 0th element of the list as root value
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    print("Serialization of this binary tree is: ")
    data = Codec().serialize(root)
    print(data)

    print("Deserialization of this binary tree is: ")
    print(Codec().deserialize(data))

main()