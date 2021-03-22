# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    i = 0
    tmp = head
    while i != position - 1:
        tmp = tmp.next
        i += 1
    tmp2 = SinglyLinkedListNode(data)
    tmp2.next = tmp.next
    tmp.next = tmp2
    return head

