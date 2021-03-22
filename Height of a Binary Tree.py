# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if root is None:
        return -1
    left_height = 1 + height(root.left)
    right_height = 1 + height(root.right)
    return max(left_height, right_height)

