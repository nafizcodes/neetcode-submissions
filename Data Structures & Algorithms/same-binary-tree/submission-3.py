# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True
        
        # if p and q and p.val == q.val:
        #     return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)

        # else: 
        #     return False


# DFS
        # stack = [(p,q)]

        # while stack:
        #     node1, node2 = stack.pop()

        #     if not node1 and not node2:
        #         continue

        #     if not node1 or not node2 or node1.val != node2.val:
        #         return False

            
        #     stack.append((node1.right, node2.right))
        #     stack.append((node1.left, node2.left))
        # return True


# BFS

        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                nodeP = q1.popleft()
                nodeQ = q2.popleft()

                if not nodeP and not nodeQ:
                    continue
                if not nodeP or not nodeQ or nodeP.val != nodeQ.val:
                    return False

                q1.append(nodeP.left)
                q1.append(nodeP.right)
                q2.append(nodeQ.left)
                q2.append(nodeQ.right)

        return True