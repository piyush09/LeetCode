"""
Algo: For each node in s, check if it's subtree equals t.

     Doing it by using isMatch() function, check if s and t match at values of their roots, plus their subtrees are matching.

     In main function check, if 's' and 't' are matching or if 't' is a subtree of child of 's'.

T.C. - O(|s|*|t|) - where |s| and |t| are number of nodes in each tree.
       As for each node in 's', it is matching if it equals to 't', that's why T.C. is          O(s*t)

"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):

        def isMatch(s, t):

            # If both of the trees are not there, then return True
            if not s and not t:
                return True

            # If any of the trees are not there, then just return False
            if not s or not t:
                return False

            if (s.val == t.val):

                if (isMatch(s.left, t.left) and isMatch(s.right, t.right)):
                    return True
                else:
                    return False

        # Checking isMatch() for both 's' and 't'
        if isMatch(s, t):
            return True

        if s is None:
            return False

        # Checking for 't' as subtree on either left or right of 's' tree
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

def main():
    S = TreeNode(3)
    S.left = TreeNode(4)
    S.right = TreeNode(5)
    S.left.left = TreeNode(1)
    S.left.right = TreeNode(2)
    S.left.right.left = TreeNode(0)

    T = TreeNode(4)
    T.left = TreeNode(1)
    T.right = TreeNode(2)

    print("Checking if subtree is there: ")
    print(Solution().isSubtree(S, T))

main()